# Aula 14
* Dados -> Modelo -> Resultado.

## Regressão Logística
* Função sigmoide.
* Apenas 0 ou 1, sim ou não.
* É o resultado de uma regressão linear com função sigmoide.
* É uma rede neural com apenas um neurônio.
* Matriz de confusão.
  * Ponto de corte (limiar) costuma ser 0,5.
  * A soma de tudo é a acurácia.
  * Precisão (valor preditivo positivo) e recall.
    * Recall o quão sensível é para "mandar" uma informação para ser avaliada (detecta).
    * Precisão é o que aquilo que o recall mandou, está correto (acerta).
      * Ex.: De 100 pessoas que podiam cancelar o serviço, 85 cancelaram.
* F1 Score.
  * A média harmônica entre a precisão e o recall.
* Gráfico ROC-AUC.
  * Area Under the Curve.