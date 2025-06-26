# Aula 6

* Princípios 
  * DRY
  * KISS
  * YAGNI

## SOLID
* Princípios.
* S -> Responsabilidade Única
  * Cada classe precisa ter uma única responsabilidade e um objetivo claro (modulariza).
* O -> Open/Closed
  * O software deve estar aberto para receber extensões, mas fechado para alterações.
    * Podemos colocar algo novo, mas sem modificar rotinas existentes.
    * Extensões do chrome (é aberto para receber extensões, mas o navegador em si continua o mesmo).
* L -> Substituição de Liskov
  * Objetos de uma classe devem funcionar ao serem substituídos por objetos de suas subclasses sem que quebre a aplicação.
    * Ex.: Uma classe Carro pode ser substituída por uma classe CarroEletrico sem problema (CarroEletrico herda de Carro)
  * Não pode perder as características da classe principal.
  * Classes filhas devem agir como a pai.
* I -> Segregação de Interfaces
  * É melhor ter várias interfaces específicas do que uma única interface geral.
  * Só vai ter as interfaces que o usuário precisa.
* D -> Inversão de Dependência
  * Um modulo de alto nível não deve depender de um modulo de baixo nível, mas ambos devem depender de abstrações.
  * Injeção de dependência, que deve ser feita pela interface, e não pela implementação dela.
