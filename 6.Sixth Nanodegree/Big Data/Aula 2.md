# Aula 2O

* Os 5 V's.
  * Volume
  * Velocidade
  * Variedade
  * Veracidade
  * Valor
* Doug Laney tem 3 V's.
  * Velocidade
  * Variedade
  * Volume
* `minIO` para armazenamento no S3.
* Formato `Parquet` (evoluiu para `Delta`) e `Avro` (binário).
  * `CSV` e `JSON` não tem padrão.
  * Formatos proprietários como do Excel, SQL Server, etc.
* Data Pipeline.
  * Coleta, ingestão, armazenamento, processamento, consumo.
    * A coleta é feita a partir de fontes, que precisam ser ditas se são estruturadas ou não.
      * Isso vai para um data lake? (para ser usado em lote), ou vai ser um fluxo (stream)?
        * `Apache Spark` para data lake (em batch), `Apache Flink` para stream e `Apache Kafkla` para transportar para algum deles.
          * Geralmente cada um fica em um servidor, visto que pode demandar muito processo/memória.
  * Data Lake armazena dados para serem disponibilizados para diferentes fins em outros momentos.
* Dados estruturados (tabelas), semi (CSV, JSON, etc) e não estruturados (e-mails, vídeos e áudios).
  * Com padrão, com um pouco de padrão, sem padrão qualquer.
  * Os não estruturados precisam passar por um processo para gerar metadados.
* É recomendável analisar os dados para coletar apenas dados relevantes e "limpos".
* O `Apache Flink` é um motor de processamento.
  * Assim como o `Spark`.
* Em Big Data tem vários componentes conversando entre si.
* O `Flink` usa java para os jobs (task).
* Existe o `FlinkSQL`.
* Várias fontes e um destino (que vai funcionar como um funil).
  * Source e Sink.