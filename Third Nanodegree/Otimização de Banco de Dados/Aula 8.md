# Aula 8

* O `plpgSQL` possui funções adicionais para o PostgreSQL, como `trigger`.
  * No oracle se chama `PL/SQL` e no Sql Server, `T-SQL`.
  * Lógica de programação com SQL.
    * Ou seja, tem variáveis, condições, etc.
      * As variáveis precisam primeiro ser declaradas.
* Permite que dados pesados sejam processados unicamente dentro do banco, sem que haja trafego pesado via API REST.
* Chamada de procedimentos.
* Pode expor interfaces sem que haja um acesso direto ao banco.
* Permite automatizações.
  * Ex.: Usar triggers quando determinada ação acontece.
* Se há alguma rotina que está sendo reescrita para várias linguagens, pode ser adaptada para que so precise chamar algum procedimento de banco.
* Para fazer que o query entenda outra linguagem além do SQL:
  * Usar um `label` com inicio e fim.
    * Geralmente se usa um label com o nome `$$` e para declara-lo, usar o `do $$`, e para fechar, usar apenas o `$$`.
      * Assim são declarados blocos anônimos.
* `Blocos anônimos` são comandos que executam apenas uma vez, sem estarem salvos em algum lugar (funciona como se fosse lambda, sem nome).
  * Dentro dele existe o bloco `declare` para declarar as variáveis, o `begin` para inciar o código em si e o `end` para dizer que finalizou.
    * Usar `;` no fim de cada comando.
      * O label não precisa disso.
    * Esse código fica dentro do label, e precisa ser fechado.
* A declaração de variável precisa ter um tipo.
  * Vai ser os tipos do SQL, porem `VARCHAR` e afins não precisa declarar tamanho.
  * Para atribuir um valor a variável, usar o `:=`, ou até mesmo com `DEFAULT` como no SQL normal.
    * Porém o `DEFAULT` só pode ser usado no bloco `declare`.
    * Usar o `=` para comparação.
* Usar o `raise notice '%', <variavel>` para mostrar um valor de uma variável, como se fosse um `printf`, ou seja, o `%` vai ser substituído pelo valor.
  * O `raise` aceita `exception`, `warning`, etc.
* Dentro do bloco de código da pra fazer `SELECT`, `UPDATE` e afins, ou seja, SQL normal.
  * Porém cuidar pra ver se o retorno pode ser mais que um.
  * Pode-se alimentar uma variável com o retorno de um SELECT, e geralmente para separar, se coloca o SQL dentro de `()`.
* O tipo de dados `RECORD` permite que uma variável tenha vários registros, pois é o mesmo tipo do retorno do `SELECT` do sql.
  * E para ler esse valor, usar um `LOOP`.