# Aula 1

* Enterprise DB tem as versões do PostgreSQL.
* Diferença entre 0 e null
  * O `null` pode existir para qualquer tipo de dado.
  * O `0` pertence a algum tipo numérico.
* `SET search_path to x` para falar que é pra buscar na schema `x`, e não na `public` que é a padrão.
  * Ele vai setar na sessão atual.
* Da pra ver as `constraints` pelas propriedades da tabela.
* Ao editar um registro, ele vai colocar esse registro no topo do select (sem `order by`).
* Para fazer `COUNT()`, melhor usar uma coluna que não sera nula, dessa forma otimiza melhor a consulta.
* O comando `distinct` (`select distinct`) pega apenas valores únicos.
* Usar `WHERE` com `IN` para filtrar por uma lista.

## Ferramentas PostgreSQL
* Ficam na pasta `bin`.
* `pg-restore`: Restaura uma base de dados.