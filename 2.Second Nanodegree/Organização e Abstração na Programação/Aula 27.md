# Aula 27

* Comando `UPDATE`
  ```SQL
  UPDATE nome_tabela
  SET nome_coluna = novo_Valor
  WHERE condicao --alterar o registro que bate com a condição (valor da coluna)
  ```
* Comando `DELETE`
  ```SQL
  DELETE FROM nome_tabela
  WHERE condicao
  ```

### Outros comandos
* O `GROUP BY` agrupa dados em comum.
  * Usar em valores que se repetem.
  * Ex.: Agrupa os preços de uma categoria
    * `SELECT categoria, SUM(preco) FROM produtos GROUP BY categoria`.
* Podemos também realizar `Subqueries`.
  * Ex.: Fazer um `SELECT` por média (`AVG`) dentro de um `WHERE`.
* Views é uma consulta que fica armazenada no banco de dados (uma consulta pronta), sendo uma tabela virtual, é quase como se fosse um método pois é possível chama-lo para buscar essa tabela customizada.
  ```SQL
  CREATE VIEW nome_view AS
  SELECT coluna_nome
  FROM tabela_nome
  WHERE condicao
  ```
  * Ex.: Criar uma tabela contendo apenas os clientes ativos de um sistema.