# Aula 11

## Comandos
* `.rename`: para renomear algo, e vai ser passado por parâmetro o item com os valores que queremos renomear.
  * A renomeção pode ser um dicionário, com o index sendo o nome atual, e o valor o nome novo.
* `.merge`: podemos dizer qual o tipo de join nos parâmetros, para juntar os df baseado nisso
  * Ex.: `.merge(right=df_1, left="df_2", how="inner", on=["nome", "sobrenome"])`, ou seja, vai criar um df com os valores que os dois df possuem em comum, usando o nome e sobrenome como chaves.
  * Podemos usar o parâmetro `suffixes` para alterar e colocar um sufixo dizendo de qual df cada coluna veio.

## Anotações
* INNER JOIN: o que os dois df possuem em comum
* LEFT JOIN: o que tem na esquerda, e o que tem em comum com o da direita
* RIGHT JOIN: mesma coisa
* OUTER JOIN: junta tudo

## Perguntas Trabalho
### Pesquisa Mercado Imobiliario

* Qual a sua idade?
* Qual a sua cidade? (unique + replace)
* Quantas pessoas moram na sua casa atualmente?
* Essa casa é sua ou alugada?
* Se for alugada, qual o valor aproximado do aluguel?
* É vc que paga?
----------------
* Você esta atualmente empregado?
* Quantos anos no trabalho atual?
* Em media, qual a sua renda? (utilizar as respostas que tem no excel do prof)
-----------------
> Da pra definir a idade média das pessoas que não moram mais com pais, e quantos deles já possuem casa própria.

> Definir uma média de valor de aluguel por cidade (cidades com > 5 respostas)

> Definir quanto a pessoa tem que estar ganhando em média para morar sozinho ou ter casa própria
                   
