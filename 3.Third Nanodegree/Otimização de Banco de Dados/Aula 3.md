# Aula 3

* `GROUP BY` vem depois do `WHERE`.
  * O `GROUP BY` é uma função.
    * Ela possui as funções de agregação que serão: `SUM`, `MIN`, `MAX`, `AVG` e `COUNT`.
      * Vão fazer essas funções a partir da coluna que esta sendo agrupada.
      * Essa funções não funcionam em colunas varchar.
    * As colunas agregadas precisam ser usadas no `SELECT` e vice versa (se tem função de agregação no `SELECT` precisa colocar a coluna que não é de agregação no `GROUP BY`).
      * A função de agregação também, pois vai ser uma nova coluna com o resultado da função.
        * Geralmente vai ser a coluna de agrupamento + as funções de agregação (que podem ser da coluna agrupada ou de outras).
      * Por ser uma função, o `GROUP BY` não pode ter funções de agregação (obviamente.)
  * É o último item do `SELECT`.
  * Usar o `HAVING` para filtrar os valores agrupados ou da função de agregação.
    * Ou seja, primeiro filtra usando um `WHERE`, depois é feito o agrupamento, e com o `HAVING` iremos filtrar esse agrupamento.
    * O `HAVING` só funciona com o valor das colunas de função.
  * O bom de agrupar, é que evita o processamento de dados desnecessários, pois vai processar com dados ordenados.  
  * O `COUNT(*)` retorna o número de linhas, já o `COUNT(coluna)` vai retornar o número de linhas NÃO NULAS da coluna.
* Ao restaurar um backup, provavelmente dará um erro, pois ele vai tentar criar a schema public, mas ela ja existe.
  * Esse erro é mais um warning, ou seja, provavelmente vai criar as tabelas normalmente.
* Sempre agrupar pela PK, pois nomes, informações, etc podem ter valores repetidos, dai acaba agrupando errado.
  * Ou agrupar por colunas com regra `UNIQUE`.
  * Da pra "ocultar" essas colunas do `SELECT` usando um CTE que faz o agrupamento, e ao fazer um `SELECT` nele, usar apenas as colunas que precisamos
    * Ou criando uma sub-query com o agrupamento, e fazer um SELECT tirando a PK.
* O agrupamento que vai executar as funções de agrupamento.
  * Porém, se temos apenas uma coluna, não precisamos agrupar por nada.