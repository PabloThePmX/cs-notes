# Aula 15

## Séries Temporais
* Ao longo do tempo está aumentando/descendendo = tendência.
* O padrão que se repete em um intervalo fixo é a sazonalidade.
* Tem o resto também, que é a parte "aleatória" de um gráfico.
* Uma série temporal é uma união desses 3 padrões, dessa forma, podemos separar uma série nessas partes.
* A média móvel é usada em séries temporais.
  * Se uma série vai aumentar ou diminuir.
  * `k` é o tamanho do período.
* Uma janela maior equivale a uma linha mais lisa e menos detalhes.
* A regra mais importante: o corte é no tempo.
  * Pra treino e pra testes.
* Três baselines (para tentar bater com o modelo):
  * Ingênua (Naive).
    * O valor de amanhã é igual ao de hoje.
    * A "melhor".
  * Média móvel.
    * Usa o padrão de tendência para fazer a previsão.
  * Sazonal Ingênua.
    * Amanhã vai ser igual ao mesmo dia da semana passada.
* Métricas de avaliação
  * MAPE.
    * O melhor para isso.
  * MAE.
  * RMSE.
* Da pra ver a tendencia fazendo a média anual, por mês, etc.
* O `rolling` é o tamanho da média móvel (`k`).