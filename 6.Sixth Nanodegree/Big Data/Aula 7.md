# Aula 7

* Data Lakes: Arquitetura Medallion
  * Bronze (raw data), prata e ouro.
    * Bronze pode salvar no S3 o Alarik (open source).
* Parquet (snappy).

## CDC (Change Data Capture)
* Interceptar dados na fonte.
* Replicação.
* É um tipo de arquitetura (design pattern)
  * Conceitual.
* Captura alterações em banco de dados em tempo real.
* Parecido com triggers.
  * Porém ela sobrecarrega as operações do banco de dados.
    * Pois monitora os dados também.
* No banco, muita coisa está sendo gravada em memória, mas só é persistida no commit.
* Busca os dados na fonte, e fazer algo com eles.
* É mais eficiente ir nos logs para gerar replicação, do que fazer isso com consultas SQL.
  * É o que o CDC faz, para replicar para outros lugares, tipo kafka.
* Baixa latência.
* Obtém os dados sem sobrecarregar a origem.
* Em vez de reprocessar conjunto de dados, o CDC vai se concentrar em mudanças incrementais.
  * Sempre monitorando o BD.
* Não olha o passado, dados existentes antes da implementação do CDC.
* Três Formas:

### Log (Mais popular e melhor principalmente para Big Data)
* Inspeciona os logs de transação que o bando de dados utiliza.
* Analisa os logs e repassa as alterações para frente.
* Logs de DML.

#### Debezium.
* É tipo um plugin do banco de dados (SQL e NoSQL), que traz informações mais estruturadas do log.
  * Conversa com o CDC de cada banco.
* Geralmente é usado com o Kafka Connect.
  * Geralmente para um tópico no Kafka, que possui uma tabela com o mesmo nome.
  * O Connect faz a ligação do Kafka para o Banco de Dados.
* Manda em JSON.
  * O `op` contém o tipo da ação, como `insert`, `update`, `delete`, etc.
* Cria um tópico com o esquema e o nome da tabela no nome.
* Usa o `WAL` do Postgres
  * Write Ahead Logging.
  * É um padrão de projeto que exige que as alterações sejam gravadas no disco apenas apos o registro dessas mudanças no log de transações.
  * Grava o que vai acontecer, antes de efetivar de fato.
  * Grava apenas registros incrementais de log.
  * Precisa habilitar no banco.
    * Usa-se a replicação lógica (que é tipo o "filtro" de log).
* Baixo nível, pois está na camada do banco de dados, e não do usuário.

### Trigger
* Igual uma função de banco.
* Ao ocorrer a alteração, grava em um lugar.
* Mas tem um custo maior, sobrecarregando o sistema.

### Timestamp
* De auditoria.
* Fica disparando consultas comparando com a última consulta, para ver se mudou a data.
* Sobrecarrega também, pois precisa ficar consultando o banco.