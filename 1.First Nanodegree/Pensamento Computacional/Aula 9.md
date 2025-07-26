# Aula 9

## Comandos
* `lambda`: Podemos usar o lambda para funções que serão usadas apenas uma vez, `lambda valor: valor * 2`, sendo o `valor` a variável que foi recebida por parâmetro, e o resto do código, o retorno.
    * É possível receber mais que um parâmetro, como por exemplo `lambda x,y: x*y` 

* `map`: Usamos para utilizar o item de uma lista, e aplicar um código nele. `map(# funcao ou item, lista)`

* if ternário: `variavel retorno1 if condicao else retorno2`

### Perguntas que surgiram
* O que exatamente é pythonic way?
  * As "regras" para escrever um bom código em python, se escrever `import this`, temos as "regras" (*The Zen of Python*) para escrever um bom código 
* Usar o `\` para quebrar a linha de métodos?
  * Sim, pois como o Python funciona com identação, precisa disto.
* Pra que usar lambdas?
  * Para deixar as funções em uma linha só, ou para facilitar a leitura, pois não vale a pena declar um método muito específico.