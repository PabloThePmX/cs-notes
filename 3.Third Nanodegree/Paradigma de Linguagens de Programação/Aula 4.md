# Aula 4

## Programação Orientada a Aspectos (AOP)
* Separar as operações de forma transversal.
* Da pra dizer que, todas as vezes antes ou depois de executar um pacote (projeto) especifico, chamar um método.
  * No java, usar as anotações `@Before` e `@After`.

## Princípios
* KISS (Keep it simple, stupid)
  * Deixe as coisas simples.
* DRY (Don't repeat yourself)
  * Não repita, reutilize o código.
* YAGNI (You Ain't Gonna Need It)
  * Não adicione funcionalidades que não são necessárias.
* Alta Coesão
  * Tudo precisa estar bem relacionado, ou seja, os métodos devem estar claros e devem ter uma tarefa única.
* Baixo acoplamento
  * Quanto menos dependências um modulo possuir, melhor.
  * Independência de módulos.
* SOLID
  * S -> Uma classe deve possuir uma única responsabilidade. (se a classe tem mais de um motivo para mudar, significa que ela tem mais de uma responsabilidade)
  * O -> Classes devem estar abertas para extensões, mas sem alterar o que já existe (herdar algo existente e adicionar novas funções).
  * L -> Se uma classe é subclasse de outra, então ela pode substituir a classe pai sem problema (pais podem ser substituídos por filhos sem quebrar o sistema).
  * I -> Uma classe deve ter um objetivo único (Várias interfaces, e a classe implementa apenas aquelas que ela vai usar).
  * D -> Não depender de algo concreto, mas sim de abstrações, como interfaces (Relacionado com injeção de dependência).
* O SOLID vai impactar na alta coesão e o baixo acoplamento.
* Tem que saber equilibrar, pois nem sempre vale a pena aplicar todos os princípios e deixar algo simples em algo complexo.