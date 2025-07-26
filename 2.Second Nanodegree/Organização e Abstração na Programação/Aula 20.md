# Aula 20

### Super
  * Para chamar os membros de uma classe pai, usa-se o `super`.
    * Pode-se chamar o construtor da classe pai também.
      * Dentro do construtor filho. 
  * O `super` é usado para chamar métodos e atributos, enquanto o `super()` é usado para chamar o construtor.

### Classe abstrata
  * É uma classe que não pode ser instanciada, mas ela pode ser herdada por outras.
  * Para declara-la `public abstract class NovaClasse {}`.
  * É diferente da interface, pois aqui podemos ter implementações dentro dos métodos.
    * E interfaces não podem ter atributos (campos) também.
    * Mas dentro da classe abstrata, podemos ter métodos abstratos também.
      * Que não terão implementação, apenas a assinatura.
        * Será obrigatório a implementação desse método nas classes filhas.
          * Usar o `@Override` para implementar na classe filha.
### `Final`
  * Para bloquear heranças de uma classe (ela ser a classe final), colocar `final`, `public final class NovaClasse {}`.
  * Podemos usar isso em um método também, `public final int novoMetodo(){}`, não deixando que o mesmo seja sobrescrito por alguma outra classe filha.
  * Pode ser útil para "chumbar" a implementação de um método de uma classe abstrata.
  * É possível declarar uma `const` usando o `final`, para que seja alimentada uma única vez.
    * A convenção do nome de uma constante é `SNAKE_CASE`.