--1 
CREATE OR REPLACE FUNCTION f_desconto (pagamento NUMERIC, percentual_desconto NUMERIC)
RETURNS NUMERIC AS $$ 
	DECLARE
		valor_final NUMERIC;
	BEGIN
		IF percentual_desconto > 100 THEN
			RAISE EXCEPTION 'Percentual de desconto maior que 100%%!';
		END IF;
		valor_final := pagamento-(pagamento*percentual_desconto)/100;
		return ROUND(valor_final, 2);
	END;
$$ LANGUAGE plpgsql;

SELECT f_desconto(160.00, 50.0);

--2
CREATE OR REPLACE FUNCTION f_acrescimo (pagamento NUMERIC, percentual_acrescimo NUMERIC)
RETURNS NUMERIC AS $$ 
	DECLARE
		valor_final NUMERIC;
	BEGIN
		IF percentual_acrescimo < 0 THEN
			RAISE EXCEPTION 'O acréscimo não pode ser negativo!';
		END IF;
		valor_final := pagamento+(pagamento*percentual_acrescimo)/100;
		return ROUND(valor_final, 2);
	END;
$$ LANGUAGE plpgsql;

SELECT f_acrescimo(220.00, 2.0);

--3
CREATE OR REPLACE FUNCTION f_atualiza_boleto (valor_original NUMERIC, data_ven_boleto DATE,
data_pagamento DATE, percentual_multa NUMERIC, percentual_mora_diaria NUMERIC)
RETURNS NUMERIC AS $$ 
	DECLARE
		diff_dias NUMERIC;
		valor_atualizado NUMERIC;
		percentual_mora_total NUMERIC;
	BEGIN
		--CALCULAR O ACRESCIMO DA MULTA - ok
		--CALCULAR O NOVO VALOR TOTAL - ok
		--VERIFICAR A DIFERENCA DE TEMPO, OU SEJA, QUANTOS DIAS PASSARAM DESDE O PAGAMENTO ATE O VENCIMENTO - ok
		--PEGAR QUANTO DE PERCENTUAL ISSO VAI SER - ok
		--ACRESCENTAR ESSE NOVO VALOR NO VALOR FINAL - ok
		valor_atualizado := f_acrescimo(valor_original, percentual_multa);
		diff_dias := data_pagamento - data_ven_boleto;
		percentual_mora_total := diff_dias*percentual_mora_diaria;
		return f_acrescimo(valor_atualizado, percentual_mora_total);
	END;
$$ LANGUAGE plpgsql;

SELECT f_atualiza_boleto(247.00, to_date('07/10/2024', 'dd/mm/yyy'), to_date('10/10/2024', 'dd/mm/yyy'), 1, 0.5);