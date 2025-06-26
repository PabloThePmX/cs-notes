# Aula 16

## Boas Práticas de Versionamento
* Software `fork` para auxiliar o versionamento do git.
* O modelo `Git Flow` usa várias branches estruturadas para organizar o desenvolvimento.
  * As versões do softwares são controladas pelas branches `<N.VERSAO>-release`
  * O desenvolvimentos fica na branch `develop`
    * Ao que ficar pronto, vai ser feito um merge para o release que depois de testado vai ser enviado para o `main`.
  * O `hotfix` é uma branch de correção urgente de bugs.
    * Uma ramificação da `main`.
      * Vai sair da `main`, e vai ser mesclada nela e no `develop`.
    * A nomenclatura fica como `hotfix/<correção>`.
  * A `main` = produção.
  * A `feature` é uma ramificação da develop, onde nela é criada uma nova funcionalidade ou uma correção (não urgente) para o projeto.
    * A nomenclatura fica como `feature/<implementação-nova>`.
* Criar branches para funcionalidades específicas, nomes claros e branches curtas (muito tempo sem mesclar).