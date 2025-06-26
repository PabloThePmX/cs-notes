# Aula 2

* O join é uma comparação, pois podemos chamar duas tabelas distintas e pegar seus valores, porem sem o join, ele não saberá por qual coluna precisa juntar.
  * Sem o join, vai pegar um registro e juntar com todos os registros da outra.
* `INNER JOIN <TABELA> ON (<COLUNA_PK> = <COLUNA_FK>)`
  * Quando ambas PK e FK tiver o mesmo nome, da pra substituir o `ON` por `USING`.
* O `JOIN` sempre vai ser de dois em dois, ou seja, quando tem mais tabelas, cada uma vai gerando um resultado que vai se afunilando até ter apenas duas.
  * Isso pode ser explorado para melhorar a performance. 
  * Ele meio que vai ir se "ligando" ate virar uma grande linha de dados.
* Existe o `EQUIJOIN` (porém é a forma antiga, não recomendado fazer).
* Os `OUTER JOINS` (`LEFT` e `RIGHT`) vão trazer os valores mesmo quando algum registro não possuir relação com algum outro.
  * Ou seja, vai deixar as colunas que não retornaram valores como nulo quando a comparação não retornar algum registro.
  * Dessa forma vai mostrar todos os registros, mesmo que algum registro não haja outro registro para ser juntado.
  * Filtrar por onde a FK for nula.
* Pode-se usar o `ILIKE` para comparar sem ser case sensitive.
* Internamente, o SGBD executa os comandos em uma ordem diferente daquela declarada.
  * Por isso que o alias funciona, pois internamente ele primeiro vai declarar antes de fazer o select.
* Para organização, é bom deixar para colocar o `SELECT` por último.
* Sobre os joins: Em resumo, vai ser uma ligação entre a tabela da esquerda com a direita, portanto precisamos de uma coluna que faça essa ligação, uma maneira de encontrar isso, seria de ir fazendo a conexão de cada tabela como se fosse uma "linha".