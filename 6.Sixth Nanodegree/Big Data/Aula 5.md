# Aula 5

* `PyFlink`.
* `ISO 8601` é de timestamp.
  * Com UTC ou sem.
* Epoch UNIX Timestamp.
  * É integer.
* O PostgreSQL é objeto relacional.
* `Watermarks` do Flink é um tipo de registro inserido nos dados para marcar a passagem do tempo.
* Dados sintéticos
  * `Faker`, originalmente é uma lib feita em java.
    * Baseado em repositórios de dados.
    * `flink-faker`.
    * Diversos providers com informações de vários tipos. 
  * `Datagen`.
* Tudo de externo usado no Flink, se chama connectors.
* Pipeline com source faker e sink kafka.
* A parte do `WITH` do sql pode ser diferente dependendo do source.
  * É criada uma tabela temporária para isso.
    * E depois a tabela de source é adicionada na sink.
* Caso não tenha sido definido um sink, da pra usar o `blackhole`.
  * Para gerar os dados mas não salvar em lugar algum.
* O `sql-client.sh` é um terminal de sql para o Flink.
* O modelo de streaming roda sem parar.