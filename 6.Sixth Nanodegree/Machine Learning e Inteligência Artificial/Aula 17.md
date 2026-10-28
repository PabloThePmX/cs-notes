# Aula 17

## Fundamentos de Redes Neurais
* É um modelo, e não um algoritmo.
  * Representação de algo.
* Descoberta de padrões.
* Um neurônio artificial:
  * Regressão logística com ponto de ativação.
    * A função introduz não linearidade.
  * Os pesos são a soma de pesos e parâmetros, depois vai ser passado para função de ativação, gerando a saída.
    * É uma soma.
* A dobra: ReLU.
  * Unidade linear retificada.
  * Recebe uma entrada, e se a entrada for positiva ela vai propagar a entrada, se for negativa vai mandar 0.
  * O máximo valor entre 0 e z.
* Quanto mais neurônios, mais sutil o padrão que a rede vai conseguir detectar.
  * Mas muitos podem levar a overfitting.
* Todo dado é padrão verdadeiro e ruído.
  * A regressão está ai para descobrir o padrão.
    * Mas se a rede for muito complexa, ela pode pegar o ruído.
* `Keras` pode ser uma API para backends (tipo `TensorFlow`) de redes neurais.
  * Framework para treinamento de rede neural.
* Para combater o overfitting, da pra usar regularização.
* Camada inicial com muitos neurônios para captar toda a informação bruta, e depois vai diminuindo.
* De forma básica: Soma as entradas, passa elas para uma função de ativação que gera a saída prevista.
* As épocas são as atualizações nos pesos, e é feito várias vezes.
* O treino é o gradiente descendente com mais pesos.
* Função de perda.
  * Entropia cruzada binária.
* A rede neural funciona melhor quando existem padrões, como imagens, dados e textos.
  * Já não em dados tabulares, para isso árvore é melhor.
* Uma rede grande decora, a validação sobe.
* Três jeitos de segurar a rede:
  * Pesos pequenos.
  * Neurônios sorteados (dropout).
    * Não fica dependente de um neurônio.
  * Parar o tempo (early stopping).
    * É um callback, pois fica monitorando o treinamento da rede e faz certas mudanças.
* A regularização deixa o treino propositalmente mais difícil.
  * Para aprender melhor os padrões.
* 