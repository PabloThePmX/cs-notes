# Aula 26

* Comando `CREATE` 
    ```SQL
    CREATE TABLE nome_tabela (
        nome_coluna tipo_dado [CONSTRAINTS],
        nome_coluna2 tipo_dado [CONSTRAINTS],
    );
    ```
* Comando `INSERT`
  ```SQL
  INSERT INTO nome_tabela(nome_coluna, nome_coluna2)
  VALUES ('Nome da Pessoa', 'Sobrenome da Pessoa');
  ```
  * Não há inserção no ID, pois ele é atribuído automaticamente.
  * Para adicionar mais valores de uma vez, apenas adicionar eles sem declarar novamente o `VALUES`, separando-os por vírgula.
* Comando `ALTER`
  ```SQL
  ALTER TABLE nome_tabela ADD COLUMN nome_coluna3 VARCHAR(20);
  ```
* Comando `SELECT`
  ```SQL
  SELECT * FROM nome_tabela;
  SELECT nome_coluna FROM nome_tabela;
  --Mostra apenas os registros que tem valores diferentes
  SELECT DISTINCT nome_coluna FROM nome_tabela;
  ```

* Usando `alias` com `as` para renomear as colunas ou tabelas temporariamente.
  * Ou seja, o SELECT usa o nome do alias no nome da coluna de retorno.
    * `SELECT nome_coluna AS nome_novo FROM nome_tabela;`
      * O keyword pode ser omitido, e funcionará da mesma forma.
      * Para respeitar os espaços e ser case sensitive: `SELECT nome_coluna as "Nome Coluna" FROM nome_tabela;`
* Constraints (restrições) mais comuns:
  * `NOT NULL`
  * `UNIQUE`
  * `PRIMARY KEY`
  * `FOREIGN KEY`
    * Possível usar assim ou com `REFERENCES`
      * Fazem a mesma coisa, mas são aplicadas de maneiras diferentes
        * O `FOREIGN KEY` é declardo no final do CREATE, depois de criar as colunas.
          * Mais organizado.
          * É atribuído a uma das colunas criadas.
        * O `REFERENCES` é declarado durante a criação, ou seja, durante a delcaração da coluna já é atribuído o comando dizendo que há a referência.
  * `CHECK`
* Ordenar usando o `ORDER BY nome_coluna`
  * Deve-se ordenar por uma coluna, e se quiser ordenar decrescente usar `DESC`.
    * Por padrão é a ordem crescente.
* Comando `WHERE` para filtrar.
  * Usar o `LIKE` para filtrar usando wildcards (%, _) no `WHERE`: `WHERE LIKE`.
* Da pra usar os operadores lógicos `NOT`, `AND` ou `OR`.
* `INNER JOIN`:
  * Compara os valores de uma coluna em comum em cada tabela, e mostra o resultado.
    ```SQL
    SELECT tabela1.coluna, tabela2.coluna
    FROM tabela1
    INNER JOIN tabela2 ON tabela1.coluna_comum = 
    tabela2.coluna_comum;
    ```
      * Seleciona uma coluna de cada tabela e junta ambas onde a coluna em comum de ambas possuir o mesmo valor.
* `SELF JOIN`
  * É um JOIN na mesma tabela, ou seja, compara o valor de colunas da mesma tabela.
  * Usado bastante para coisas hierarquicas, como hierarquia de corporações.
  ```SQL
  SELECT f1.nome AS funcionario1, f2.nome AS funcionario2, 
  f1.departamento
  FROM funcionarios f1
  INNER JOIN funcionarios f2 ON f1.departamento = 
  f2.departamento
  WHERE f1.id != f2.id;
  ```
  * O `f1` ao lado do from, é o alias.
    * Ele pode ser omitido. 