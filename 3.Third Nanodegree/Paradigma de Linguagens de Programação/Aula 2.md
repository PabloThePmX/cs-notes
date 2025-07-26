# Aula 2

* Da pra assimilar que o repositório = contexto.
* Paradigma procedural, usa funções, métodos, procedimentos, etc
* O paradigma estrutural fala de condições, como `if`, `while`, `for`, etc.
  * Por tanto ele está dentro do procedural.
  * Foi criado para ter um maior controle, e evitar a utilização de `goto`.
* A ordem dos paradigmas estruturais seria `Estruturado -> Procedural -> Imperativo`
* O paradigma funcional se concentra na maneira que serão juntadas funções para poder resolver um problema.
  * Ex.: Lambda

## Funcional
* Uma função lambda não "fica na memória" como uma função normal.
  * Em python, a função lambda precisa ser declarada com `lambda`.
  * Em Java é parecido com C# e JS.
    * O java possui interfaces funcionais para serem usadas com funções lambda.
* Função de ordem superior, é uma função que aceita outras funções como parâmetros (funções ou lambdas), ou retorna uma função.
* Função como cidadãos de primeira classe, é como é chamada uma função passada como argumento para outras funções.
* Imutabilidade representa a não alteração de algum valor, ou seja, uma vez que o dado for criado, não poderá ser alterado.
  * Ao invés de modificar esse dado existente, será criado uma nova versão dele.
    * Permitindo que as funções sejam puras.
* Método puro e impuro
  * Puro não altera valores globais, apenas o o valor que recebe, já o impuro sim, altera valores globais.
  * Dados globais e funções impuras podem impactar quando se trabalhar com mais threads.
* Funções podem ser combinadas.
* Na recursividade, o método chama ela mesma.
  * Quanto mais recursividade = mais devagar.