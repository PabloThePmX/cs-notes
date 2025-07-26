# Aula 3

* Variáveis do tipo primitivo não tem métodos.
* Métodos `static` pertencem a classe, enquanto não estáticos pertencem a instância.
* Encadeamento de métodos.
  * Cada invocamento retorna um objeto (instância), e é nesse objeto que é chamado o outro método.
    * Dessa forma, ele vai mostrar os métodos que o objeto pode invocar.
* `Stream` é um pipeline, ou seja, uma pilha de instruções que deverão ser executadas somente ao ser transformado em uma lista ou algo do tipo (operações terminais).
  * Lazy, pois so é executado quando uma operação terminal é chamada.
  * A stream funciona de forma paralela.

## Paradigma Logico
* Faz verificações lógicas a partir de fatos (linguagem puramente lógica: `prolog`).
* Pode ser usado com IA, PLN, Banco de Dados, etc. 


Quando invocar um método que retorne um objeto diferente dele, ele vai retornar uma nova instancia ou a nova classe?