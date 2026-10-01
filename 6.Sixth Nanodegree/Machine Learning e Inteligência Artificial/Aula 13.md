# Aula 13

* Interpolar = encontrar um dado que está no meio dos dados.
  * Os modelos são melhores para buscar isso.
* Extrapolar = encontrar um dado fora do escopo existente.
* Os dados de treino são usados para encontrar padrões, e os de teste são usados para comparar com os dados reais.
  * O modelo pode decorar os dados de treino, mas esse não é ideal, por isso precisa de dados de teste.
    * Por isso que tem que separar os dados em treino e teste.
* Previsão e Preditor.

## Regressão Mútua
* Cada informação entra multiplicada pelo seu próprio peso.
  * É tudo somado.
* O peso é encontrado pelo modelo.
* Com duas variáveis, a reta vira um plano (3D).
  * Com três variáveis pra cima, já não é possível demonstrar.
    * Vira um hiper plano.
* No treino quase não muda nada.
* Coeficiente, peso, parâmetro, é tudo igual, apenas termos diferentes.
* Para colocar uma variável com nome (tipo bairro), e não quantidade no modelo:
  * Da pra numerar.
    * Porém o modelo passa a usar isso como quantidade.
  * O melhor é ter uma coluna nova para cada bairro, com 0 e 1.
    * Dummy variables.
    * Colinearidade perfeita: dummy variables com 0 significam um valor também.
      * Os valores vão ser em relação a isso.
    * One hot encoding.
    * Essas colunas entram na formula como qualquer outra variável.
      * São usadas como peso.
* Antes de treinar, precisa transformar em 0 e 1, e padronizar as variáveis numéricas numa escala comum.
* Regularização = escolher automaticamente as melhores variáveis e deixar na mesma escala.
  * Adiciona a penalidade em relação aos pesos.
  * Ridge, Lasso e ElasticNet.
* Resíduos sem padrão significam que o modelo está bem posto.
* Hiper parâmetro é algo que vamos setar.
  * Uma configuração de como o treino vai acontecer.
    * É o que nos vamos fazer experimentos para descobrir.
  * Parâmetro é o que vai ser encontrado pelo algoritmo.
* Treinamento usando o dataset `California Housing Prices`.
  * Tipo o `Hello World` do ML.