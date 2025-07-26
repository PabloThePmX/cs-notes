# Aula 25

* SQL (Structured Query Language) é uma linguagem de consulta estruturada, usado para gerenciar bancos de dados relacionais (SGBDs).
* É uma linguagem declarativa, ou seja, os usuário diz o que vai ser feito, e o SGBD executa.
* Patronizada pela ANSI e ISO.
* Tipos de comandos SQL:  
  * DDL (Data Definition Language): Para definir a estrutura do banco.
  * DML (Data Manipulation Language): Alterar registros do banco.
  * DCL (Data Control Language): Para controller o acesso aos dados.
  * TCL (Transaction Control Language): Gerencia as transações em si. 
* Tipos de dados do Postgre:
  * Numéricos:
    * `Smallint` (ocupa 2 bytes)
    * `Interger` (int) (ocupa 4 bytes)
    * `Bigint` (ocupa 8 bytes)
    * `Serial`, número incremental de 4 bytes.
    * `Bigserial`
    * `Numeric`, usado para valores exatos, que precisam de precisão.
    * `Real`, ponto flutuante com precisão simples.
    * `Double Precision`, ponto flutuante com precisão dupla.
  * Caracteres:
    * `Char`, cadeia de chars com número fixo.
      * Espaços em brancos são preenchidos, se necessário.
    * `Varchar`, tamanho variável, com limite máximo.
    * `Text`, tamanho variável, sem limite de comprimento definido.
  * Data e Hora
    * `Date`
    * `Time`
    * `Time With Time Zone`
    * `Timestamp`, data e hora.
    * `Timestamp With Time Zone`
    * `Interval`, diferença de um intervalo de tempo.
  * Booleanos
  * Dados Binários
    * `Bytea`, arquivos ou fluxos de bytes.
  * Monetários
    * `Money`, formatados com cifras de moedas.
* CRUD
  * `CREATE`
  * `ALTER`
    * Altera a estrutura da tabela.
  * `SELECT`
  * `DELETE`
  * `UPDATE`