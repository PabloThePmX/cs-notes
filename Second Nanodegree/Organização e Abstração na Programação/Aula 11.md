# Aula 11

* O tipo de dado de uma classe, é a classe em si.
* O construtor herdado vai sempre executar antes do construtor filho.
* Podemos usar o `super()` para herdadar retornos das implementações dos métodos da classe pai, e assim, podemos editar o valor. 
  * Ou seja, se estamos mexendo no método `__str__()`, podemos buscar o valor de `super().__str__()` da classe pai, e altera-lo (override).
  * Isso é polimorfismo.
* Podemos instanciar a classe dentro de uma lista.
  * Ter uma lista com vários objetos diferentes.