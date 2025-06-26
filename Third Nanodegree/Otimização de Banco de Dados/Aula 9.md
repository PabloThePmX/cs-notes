# Aula 9

* O `DECLARE` não é necessário caso não existam variáveis.
* Seguindo a lógica de que, se fazer um where pela chave primária, SEMPRE vai ter o retorno de 0 ou 1, ou seja, já é possível saber que não serão retornados mais valores.
  * Para salvar um valor único para uma variável, no `SELECT` usar `INTO` para atribuir a uma variável.
    * Ex.: `SELECT first_name INTO name ....`.
      * Dessa forma é possível salvar até mais de um valor de uma vez, atribuindo n coluna do select para n variáveis.
        * Porém continua apenas aceitando retornos de uma linha.
  * Bem como usando uma sintaxe de subconsulta, atribuindo com o `:=`.
* Da pra declarar blocos de `EXCEPTION`
  * Com funções prontas como `WHEN NO_DATA_FOUND THEN raise 'msg erro'`
    * Ou seja, quando não encontrar valores, jogar uma mensagem de erro.   
* Os plpgsql aceita if, com `IF`, `ELSE`, `ELSEIF` e `END IF`.

## Cursor
* O cursor (um ponteiro para cada linha) guarda na memória o resultado de uma consulta.
  * Ou seja, ele salva uma matriz de dados.
* Vai extraindo linha por linha do cursor com o comando `fetch`.
* Carrega linha por linha, sempre reaproveitando o mesmo espaço (tira e coloca).
* Usa a variável do tipo `RECORD`.
  * Porém lembrar que ela só armazena UM registro.
* Agora geralmente se usa uma estrutura de condição.

## Estruturas de condição
* Até o postgres 10 usava uma lógica mais robusta, que precisava declarar vários passos manualmente.
  * Agora é basicamente so um `FOR IN` com `LOOP` normal.
    * Pode ler uma subconsulta.
* Usar o `FOR IN` para declarar a coleção e ler com o `LOOP` e `END LOOP`.
  * Para pegar cada valor durante o LOOP, usar o `<item>.<coluna>`.
  * Ex.: `FOR item in ()` e depois ler esse `item` dentro do `LOOP`.

## Functions
* Usa lógica também.
* É um bloco nomeado, como a procedure.
* Como o SQL não deriva do C, há diferenças entre procedimentos e funções.
  * Uma função recebe n parâmetros e retorna apenas um valor.
  * Já o procedimento é mais flexível, pois permite n parâmetros e retorna n valores.
* Existem funções nativas (do próprio SGBD) e definidas pelo usuário.
* Para criar, usar o `CREATE OR REPLACE FUNCTION <nome> (<tipos_dados_parametros>)`.
  * Da pra declarar direito com o nome e tipo da variável, ao invés de usar apenas os tipos.
    * Porém não da pra ser misto, ou seja, ou é declarado por tipo de dado, ou pelo tipo de dado e nome.
    * O tipo vem depois do nome da variável.
  * Tem que cuidar ao usar o `REPLACE` em desenvolvimento.
  * Existe o `DROP FUNCTION` também.
  * Verificar como está a padronização do banco para o definir o nome dos parâmetros.
    * Alguns usam com o `p_` na frente.
* Usar o `RETURNS <tipo_dado>` para dizer o que vai declarar.
* Ao usar o RETURNS, inicializar o bloco de retorno com o label, ou seja `RETURNS int AS $$` e a partir daqui iniciar o código.
  * E retornar um valor dentro do `BEGIN`, com o `RETURN <variavel>`.
* Para pegar o valor de cada parâmetro quando for apenas declarado o tipo nos parâmetros, usar `<nome> ALIAS FOR $1` para pegar do primeiro parâmetro.
* Ao final do bloco, precisa declarar a linguagem, ou seja `$$ LANGUAGE plpgsql`
* Chama a função apenas com SELECT e sem FROM.
* A função é usada apenas para retornar valores, enquanto nos procedimentos podemos usar para alterar valores do banco.
