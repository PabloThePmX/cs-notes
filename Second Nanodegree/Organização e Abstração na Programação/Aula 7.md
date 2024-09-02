# Aula 7

### Como criar o modelo ER lógico
* Começar com o modelo conceitual desenvolvido.
  * Primeiro revisar se está tudo correto.
* Definir os atributos e seus tipos de dados.
  * Não precisa adicionar o tamanho do campo, apenas no modelo físico.
* Identificar as chaves primarias para cada entidade.
* Definir as chaves estrangeiras da entidade.
* Adição de restrições de integridade (constraints).
* Mapear os relacionamentos das entidades.
  * Um para um, um para muitos e muitos para muitos (teoricamente não deveria existir, é uma anomalia).
* Pensar no desempenho.
  * Indíces, particionamento de tabelas, etc.
* Documentar as decisões tomadas para criar o modelo.
* Padronização dos nomes, colunas e restrições.
  
### Normalização
* Tem o objetivo de organizar os dados de maneira eficiente e evitando anomalias.
* As regras são chamadas de Formas Normais (FN).
  * Essas regras são aplicadas para eliminar a redundância de dados, assegurar a consistência dos dados, facilitar a manutenção e melhorar a eficiência das operações de consulta.
* Evitam tabelas com dependências complexas (ou seja, muitas FKs na mesma tabela).
* A normalização pode custar desempenho.
  * É necessário encontrar um equilíbrio.
#### Regras
* **1FN**: Todos os atributos devem ser atômicos (o campo deve ter sempre apenas um valor).
* **2FN**: Ela primeiro deve estar de acordo com a 1FN, e diz que um atributo não chave é totalmente dependente da chave primária.
* **3FN**: Além de estar na 2FN, cada atributo não chave deve depender apenas e exclusivamente da chave primária.
* **BCNF (Boyce-Codd)**: Veio para corrigir de vez problemas que poderiam ocorrer na 3FN, e nela não podemos deixar que uma chave determinante (que pode ser usada para buscar uma chave primaria) não seja considerada uma chave candidata na tanela.
    * Para deixar em BCNF, precisamos dividir a tabela e deixar que as colunas determinantes possam se tornar uma chave candidato em cada uma dessas tabelas.