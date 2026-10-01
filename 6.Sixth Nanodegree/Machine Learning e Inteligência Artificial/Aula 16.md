# Aula 16

## Modelo de Séries Temporais
* A sazonal ingenua não sabe que o negócio cresce.
  * Não sabe de datas especiais e diferentes, como Natal, Páscoa, etc.
* Usa a regressão múltipla.
* Tendência com números de dias, semana e ano com variáveis indicadores do da da semana e do mês, e uma coluna feriado, com 0 e 1.
  * Regressão com calendário.
    * Diz exatamente qual o dia da semana.
  * Porém isso não ta pegando o valor anterior da série.
    * Um algoritmo que usa isso, é auto regressivo (como um LLM).
* ARIMA.
  * Uma regressão comum, em que as colunas de entrada são as vendas dos dias anteriores.
  * Consegue prever as mudanças, não exatamente os valores do dia de amanhã.
    * "Quando vai vender amanhã com relação de hoje".
  * Pode incluir no modelo, o erro de previsão do dia de ontem.
  * Vai melhorando ao longo da série.
  * Modelo ARIMA p, d, q.
* Dois jeitos: regressão com calendário ou ARIMA.
  * A com calendário, vai precisar montar as colunas.
* Dá pra colocar sentimentos para que o modelo aprenda ainda mais com notícias.

## Técnicas Modernas

### Prophet
* Uma biblioteca que monta a regressão com o calendário.
* Biblioteca da Meta.
* Usa tendência, semana, ano e feriados.
* Passa uma coluna com timestamp e o valor a ser previsto.
* Cria o modelo, treina no passado (com `fit`), monta a tabela com datas futuras e prevê.
* Simplifica pois monta tudo para nós.
* A saída traz `yhat` (a previsão) e as bordas com `yhat_lower` e `yhat_upper`.
  * As bordas são a faixa de incerteza, com maior e menor cenário.

### TimesFM
* Um modelo da Google que já viu milhões de séries temporais e prevê sem treinar nada.
* Ele é mais pesado.
* Ele prevê uma série nova sem treinar nela.
  * Isso se chama zero-shot.
* Consegue pegar uma série que recém está começando, e começa a prever a partir disso.
* Baixar o modelo do Hugging Face (`from_pretrained`).
* Entregar o histórico em forma de tensor no `PyTorch`.