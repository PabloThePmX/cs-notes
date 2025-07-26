# Aula 10

* Truncar refere-se a alteração de quantos números após a vírgula será utilizado.
* Lembrar que para alimentar um valor de uma variável com valores do banco, é possível usar `SELECT INTO`.
  * Porém precisa ser uma consulta que retorna apenas um registro.
* Podemos fazer CAST no postgresql usando a função `CAST`, ou usando `::` (que seria um shorthand), 
  * Alguns exemplos:
    * Para passar a coluna a para o tipo data: `a::date`
    * Usando CAST: `CAST(a AS DATE)`
  * Da pra fazer o cast de valores também, e não necessariamente apenas de valores em colunas.

## Procedures
* É como se fosse uma rotina em si, pois a função é para coisas mais simples.
  * A função costuma ser uma espécie de tratamento de dado, e praticamente sempre vai retornar algo.
  * Resolve algum processo.
  * Seria como se fosse uma camada de serviço, com as regras de negócio.
* Só funciona a partir do postgresql 11.
* É um bloco nomeado, como a function.
* Pode ter vários parâmetros de entrada, bem como vários de saída.
* Por vezes apenas recebe os parâmetros, e não retorna nada.
* As vezes temos uma procedure que contém vários `SELECT`, as vezes usados apenas para retornar um valor.
  * Ou trazendo vários dados de uma vez, aproveitando a mesma procedure para fazer todos esses `SELECT`.
* Cuidar para não acessar muitas vezes a mesma instância, para não saturar o banco.
  * Ou também cuidar para não acessar a mesma tabela enquanto outra consulta na mesma ainda esteja acontecendo.
* A sintaxe de uma procedure seria `CREATE OR REPLACE PROCEDURE <nome> (<parametros>) language plpgsql AS $$` e o resto fica da mesma forma que a função.
  * Ou seja, é bem parecido com a sintaxe da função, porém a language aparece mais no início.
* Geralmente se altera valores do banco, com `UPDATE` e `COMMIT`.
* Da pra dizer se os parâmetros do procedimento são `IN`, `OUT` ou `INOUT`, ex.: `(nome IN VARCHAR, sobrenome OUT VARCHAR)`.
  * Por padrão é `IN`.
  * Igual os procedimentos do GeneXus.
  * Não precisa de `RETURN`, pois vai retornar os parâmetros do tipo `OUT` e `INOUT` automaticamente.
* Não pode ser chamada em qualquer lugar como a função, pois por se tratar de uma rotina, ela pode retornar mais valores, e para chama-la, usar o `CALL`.
  * Se não possuir retorno, obviamente não haverá atribuição na chamada.
* Da pra encadear e chamar uma procedure dentro de outra.
* Quanto tiver `OUT`, deve-se declarar variáveis para serem alimentadas na procedure durante a `CALL`.
* As procedures podem ser chamados por outras linguagens.
  * Porém por aqui tem que dizer qual é o valor de entrada, e qual é o valor de saída, declarando-os com sets específicos para cada.
* O `OUT` é algo mais recente, pois anteriormente so poderiam ser usado o `IN` e `INOUT`.
  * A partir da versão 14 funciona.