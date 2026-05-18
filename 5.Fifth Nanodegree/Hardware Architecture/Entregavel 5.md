# Contador Simples

* Mário Bernardo Balen (1136196)
* Pablo Henrique Strücker Sarturi (1136331)

| Item                        | Resposta |
|-----------------------------|-----------|
| Código escolhido            |    Contador simples       |
| Entradas                    |     clk (bit) e reset (bit)      |
| Saídas                      |     Q (integer)      |
| Tipo de circuito            |     Sequencial      |
| Possui clock?               |     Sim      |
| Guarda estado/memória?      |     Sim      |
| Hardware representado       |     Contador      |
| Existe erro ou risco?       |     Sim, o `rising_edge` como bit pode causar incompatibilidade    |

## Correção do Código
```VHDL
entity contador is
  port(
    clk   : in std_logic;
    reset : in std_logic;
    Q     : out integer
  );
end contador;

architecture comportamento of contador is
  signal valor : integer := 0;
begin
  process(clk, reset)
  begin
    if reset = '1' then
      valor <= 0;
    elsif rising_edge(clk) then
      valor <= valor + 1;
    end if;
  end process;

  Q <= valor;
end comportamento;
```

## Conclusão
O código em si está quase perfeito, porém é preferível ter o `std_logic` para evitar possíveis problemas futuros. No mais, ele representa de forma simples e funcional um contador.