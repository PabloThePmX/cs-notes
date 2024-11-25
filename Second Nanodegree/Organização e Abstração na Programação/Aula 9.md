# Aula 9

### Paradigmas de Programação
* **Imperativos**
  * Procedural
    * Estruturado
  * Orientação a Objetos
* **Declarativos** (Diz o que vai fazer, e não como vai fazer)
  * Funcional
  * Lógico

### Procedural
* Procedimentos (funções).
* Controle de fluxo.
* Variáveis e dados globais.
* Pode ter desempenho melhor.

### POO
* Reutilização de código.
* Abstração de dados.
* Desacoplamento.
* Novos tipos de dados (abstração).
* "Chamar" = "Invocar"
* A classe é o modelo, e ao chamar a classe, vai ser criado o objeto dessa classe, ou seja, uma instância desse objeto.
  * O objeto obviamente vai so existir em runtime.
* ### Abstração
  * É o processo de identificar e definir as características essenciais de um objeto do mundo real. 
* ### Encapsulamento
  * "Proteger" as variáveis.

### POO em Python
* Para declarar uma classe colocando `class`
* O construtor se chama `__init__`
  * Chamar como `def __init__(self)` sendo o `self`, o equivalente ao `this`
* Precisa chamar o `self` nos parâmetros dos métodos, pois não é implícito como em outras linguagens.