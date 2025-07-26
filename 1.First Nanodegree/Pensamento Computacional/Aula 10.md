# Aula 10

## Comandos
* `sep=";"`: define qual vai ser o tipo do separador, nesse caso, o ponto e vírgula.
  * Usado como parâmetro na leitura do CSV `.read_csv`
* `.drop`: para excluir o df
* `inplace`; é um parâmetro que diz se vai criar um novo df com as modificações realizadas, ou se vai substituir no df atual.
  * O padrão dele é `False`, que significa que ele vai criar um novo df, que precisa ser alimentado em alguma variável.
* `.apply()`: para aplicar um código (lambda por exemplo), em uma linha ou conjunto de dados específicos.

## Anotações
* Para adicionar um valor ao dicionário, colocamos o nome do indíce novo, já atribuindo o seu valor. Ex.: `dicionario["chave2"] = "novoValor"`
* Para atualizar, podemos utilizar `dicionario.update({"chave2": "valor2"})`
* Em linguagens fortemente tipadas, quando queremos declarar um char, colocamos aspas simples no valor.
  * No python isso não importa.