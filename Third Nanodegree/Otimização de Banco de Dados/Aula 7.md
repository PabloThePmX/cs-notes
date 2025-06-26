# Aula 7

* Muitos joins e ordenação de dados faz o uso computacional elevar.

## View
* Para declarar uma nova view, rodar `CREATE VIEW <nome_view> AS SELECT ...`
* São consultas "salvas" na db.
* A view é gerada em tempo de execução, ou seja, sempre está atualizada.
* Pode ser útil para encapsular um `JOIN` muito grande.
* Podem ser usadas para segurança, dando acesso apenas para alguns usuários.
* Podemos estrutura uma view de acordo com o que vai ser mostrado para o usuário no front.

## Views Materializadas
* Existem as views materializadas, que salvam os resultados na própria view, e não precisa ser buscada a todo momento. (porém não é tão comum utiliza-la)
* Para declara-la, usar `CREATE MATERIALIZED VIEW <nome_vw> AS ....`
* Se precisar atualizar o valor, fazer um `REFRESH MATERIALIZED VIEW`.
  * Ou seja, toda vez que queremos atualizar o valor, precisa atualizar manualmente.
* Pode ser usada para buscar valores que costumam continuar fixos, como valores com filtro de anos passados.
* É possível criar ela sem dados, com um `WITH NO DATA` no final da consulta de criação.
