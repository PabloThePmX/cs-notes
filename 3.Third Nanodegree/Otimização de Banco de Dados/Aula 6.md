# Aula 6

## CTE
* Uma CTE é definida usando o `WITH`.
  * Seria como criar uma tabela temporária que é possível fazer um `SELECT` depois.
  * So precisa usar o WITH na primeira CTE declarada.
* `WITH <nome> AS (DEFINIÇÃO DO CTE)`
  * Dai quando for fazer um `SELECT`, faz no nome definido aqui.
* O CTE permite recursividade.
  * Da pra fazer até menus dessa forma.
  * Usar o `WITH RECURSIVE`.

## Window Functions
* Ele meio que faz um "ZOOM" (separa em partições) dos valores retornados.
  * Pega valores que já foram retornados.
  * Diferente do `GROUP BY` que agrupa em uma linha, a window function vai retornar todas as linhas + a função de agregação.
* É definida usando a claúsula `OVER()`.
* Tem funções de agregação, ranking e value.
* Mostra a função de agreação SOBRE a partição de uma coluna.