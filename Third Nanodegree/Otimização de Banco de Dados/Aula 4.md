# Aula 4

* O `DISTINCT` pode ser usado para buscar pelos valores únicos.
* Usar alias + * para fazer um select de todas as colunas em um join, ou seja `SELECT f.*, l.*`.

## Subconsultas (Subquery)
* Seria como um `SELECT` dentro de outro `SELECT`.
  * Da pra até colocar um `SELECT` dentro de um `FROM`, para que pegue do resultado de uma consulta.
* Vai ser usado para comparar dois `SELECT`s
  * Usando `IN`, `NOT IN`, `EXISTS`, `NOT EXISTS`, `ANY`, `ALL` ou os operadores lógicos tradicionais.
    * `WHERE coluna IN (SELECT coluna FROM tabela)`.
      * Ou seja, vai verificar se o valor dessa coluna existe na coluna da outra tabela.
  * O `EXISTS` precisa de um `WHERE` para que haja ligação.
    * Geralmente o `EXISTS` substitui o uso de um `INNER JOIN`.
  * Podem ser usados para valores também.