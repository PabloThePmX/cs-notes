# Aula 5

* O `seaborn` precisa do `matplotlib`.
* Encoding de dados categóricos.
  * Transforme texto em dados numéricos.
  * One hot encoding.
    * Transforma cada categoria em uma nova coluna booleana ou inteira.
      * Ex.: A pessoa é branca: Sim ou Nao, é parda: Sim ou Não, etc.
    * Usar o `get_dummies()`.
      * Dizer a coluna e o tipo que vai ser o resultado (que na maioria dos casos vai ser `int`, para ser 0 ou 1).
      * Dizer o prefixo para ser o prefixo do nome da coluna.
    * Depois fazer um `join` para colocar o resultado dessa função, dentro do data frame.
      * Não tem `inplace`, precisa fazer a atribuição.
  * Ordinal encoding.
    * Cria uma nova coluna que associa a categoria original a um número de 0 a n.
    * Fazer com dicionário chave-valor.
    * Aplicar o `.map(dicionario chave valor)` na coluna.
* Média (mean), mediana (median) e moda (mode).
  * Mediana: valor do meio após a ordenação.
  * Cuidar com outliers.
* O `.describe()` na coluna, vai mostrar várias informações (descrições dos dados), como média, mediana, etc.
  * Mostra o quartil também, que é cada parte do valor total dividido por 4.
    * Ou seja, 25% de cada parte.
    * Vai ser 3 quadrantes, Q1, Q2 e Q3.
* `std` = desvio padrão.
  * A média de distância para a média total.

## K-NN
* K-nearest neighbors.
* Classificação e regressão.
  * Classificação: Dados categóricos e qualitativos.
    * Qual grupo ou categoria determinado valor pertence?
  * Regressão: Dados numéricos e quantitativos.
    * Qual o valor estimado?
* Distância Euclidiana.
* Utiliza apenas números.
* Desempenho ruim em grandes datasets, principalmente devido ao sort.
* Usado principalmente para preencher dados vazios, ao invés de usar a moda/mediana.
* Da pra classificar vários valores "juntos".