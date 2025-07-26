# Aula 5

* O `IN` e o `EXISTS` pode ser substituído por `JOINS` ou vice versa.
* O `JOIN` junta linhas de diferentes tabelas.
* Podemos criar colunas e seta-las com um valor padrão dentro do `SELECT`.
  * Coloca o valor e diz o alias desse valor (qua vai acabar sendo o nome da coluna).
* O SQL concatena usando o `||`.

## Combinação de Consultas (baseada na teoria dos conjuntos)
### UNION
* O `UNION` vai unir `SELECT`s.
* O `JOIN` une na horizontal (junta na linha) e `UNION` na vertical ("cria" linhas).
* Concatena o resultado de consultas.
* Precisam ter a mesma quantidade de colunas, e devem ser do mesmo tipo de dados.
* Precisa concatenar dados que possuem relação.
* O `UNION` vai ficar no "meio" dos `SELECT`s.
* Pode ser útil para unir tabelas iguais que estão em schemas diferentes (locais diferentes).
  * Também para comparar períodos de tempo diferentes de uma mesma tabela (preciso do valor pago por uma pessoa em três anos distintos) (momentos diferentes).
    * Dessa forma da pra fazer `SUM` em cada ano separadamente.
  * Também quando temos tabelas em redes separadas.
* Remove as duplicatas automaticamente.
* Possível juntar o resultado do `UNION` para utilizar em um `SELECT` externo.
  * Se quisermos colocar um nome diferente para a coluna, precisa ser feito dessa forma, e colocando o alias nas colunas do `SELECT` interno.

### UNION ALL
* Mesma coisa que o `UNION` mas não remove as duplicatas.
* Por não precisar remover, pode ser mais rápido.
