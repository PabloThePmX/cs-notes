# Big Data: Flashcards

> Leia a pergunta, **tente responder de cabeça**, e só então clique em "Resposta".

---

## Aula 1: Introdução ao Big Data

**1. O que é Big Data?**
<details><summary>Resposta</summary>

Dados **multivariados** e de **elevada dimensão**, geralmente **criados em tempo real**, com **crescimento exponencial**.
</details>

**2. Big Data é sobre o quê, segundo a aula?**
<details><summary>Resposta</summary>

Sobre o **valor e o significado** que podem ser extraídos dos dados. Não é só "um monte de dados".
</details>

**3. Quais são os 5 V's?**
<details><summary>Resposta</summary>

**Volume, Velocidade, Variedade, Veracidade e Valor.**
</details>

**4. Quais são os 3 V's de Doug Laney (2001) e quais V's vieram depois?**
<details><summary>Resposta</summary>

- Laney: **Volume, Velocidade, Variedade**.
- Acrescentados: **Veracidade** e **Valor**.
</details>

**5. Volume: qual o problema e qual a solução?**
<details><summary>Resposta</summary>

- Problema: exige cada vez mais poder de computação para armazenar e processar.
- Solução: armazenamento mais **barato**, confiável e acessível (**nuvem**). O **Hadoop** é o principal sistema.
</details>

**6. Variedade: qual o problema e qual a solução?**
<details><summary>Resposta</summary>

- Problema: muitas fontes e tipos (estruturados e não estruturados) dificultam armazenar, minerar e analisar.
- Solução: bancos **não relacionais** (ex.: **MongoDB**). ML e Deep Learning ajudam a dar sentido aos formatos.
</details>

**7. Velocidade: o que é e como se resolve?**
<details><summary>Resposta</summary>

Fluxo **maciço e contínuo** de dados. Resolve-se com **sistemas automáticos 24h por dia**. Os pipelines podem ser **streaming** (tempo real) e/ou **batch** (lote).
</details>

**8. O que a Veracidade exige?**
<details><summary>Resposta</summary>

Que os dados passem por **verificação antes de serem armazenados**, evitando dados **falsos, incompletos ou duvidosos**.
</details>

**9. O que é Valor?**
<details><summary>Resposta</summary>

Os dados precisam **gerar valor**: vantagem competitiva, melhor serviço ao cliente e destaque no mercado.
</details>

**10. O que é o Hadoop e de que conceito ele vem?**
<details><summary>Resposta</summary>

Uma implementação **open-source** do conceito de **MapReduce**.
</details>

**11. Quais são os três pilares do "legado Google" nos slides?**
<details><summary>Resposta</summary>

**GFS** (Google File System), **MapReduce** e **BigTable**. O BigTable evoluiu para o **BigQuery**. (Os slides datam 2006, 2007 e 2008.)
</details>

**12. ➕ O que é "linhagem de dados" e o que é "governança de dados"?**
<details><summary>Resposta</summary>

- **Linhagem:** origem e etapas de processamento do dado.
- **Governança:** execução de autoridade e controle sobre os dados (DMBOK).
</details>

---

## Aula 2: Pipeline de dados, formatos e ferramentas

**13. Quais as etapas de um data pipeline, em ordem?**
<details><summary>Resposta</summary>

**Coleta, ingestão, armazenamento, processamento e consumo.**
</details>

**14. Qual a decisão central depois da coleta?**
<details><summary>Resposta</summary>

O dado vai para um **data lake** (uso em **lote/batch**) ou segue como **fluxo (stream)**?
</details>

**15. Qual o papel do Spark, do Flink e do Kafka?**
<details><summary>Resposta</summary>

- **Spark:** processamento para data lake (**batch**).
- **Flink:** processamento de **stream**.
- **Kafka:** **transporta** os dados até um deles.
</details>

**16. Por que cada ferramenta geralmente fica em um servidor separado?**
<details><summary>Resposta</summary>

Porque podem demandar **muito processo e memória**.
</details>

**17. O que são Source e Sink?**
<details><summary>Resposta</summary>

**Source** = origem (várias fontes). **Sink** = destino (um só), como um **funil**.
</details>

**18. Classifique: tabelas, CSV/JSON, e-mails/vídeos/áudios.**
<details><summary>Resposta</summary>

- Tabelas: **estruturados** (com padrão).
- CSV, JSON: **semiestruturados** (um pouco de padrão).
- E-mails, vídeos, áudios: **não estruturados** (sem padrão).
</details>

**19. O que precisa acontecer com dados não estruturados?**
<details><summary>Resposta</summary>

Passar por um processo para **gerar metadados**.
</details>

**20. O que é um Data Lake (ideia da Aula 2)?**
<details><summary>Resposta</summary>

Armazena dados para serem disponibilizados **para diferentes fins em outros momentos**.
</details>

**21. Que formatos de arquivo a aula cita?**
<details><summary>Resposta</summary>

**Parquet** (evoluiu para **Delta**) e **Avro** (binário). CSV e JSON **não têm padrão** rígido. Há ainda formatos **proprietários** (Excel, SQL Server).
</details>

**22. O que é o minIO?**
<details><summary>Resposta</summary>

Armazenamento compatível com **S3**.
</details>

**23. ➕ Quais os 4 componentes principais de um pipeline (AWS)?**
<details><summary>Resposta</summary>

**Fontes, transformações, dependências e destinos.**
</details>

**24. ➕ Parquet x Avro: orientação e uso?**
<details><summary>Resposta</summary>

- **Parquet:** **colunar**, ótimo para análise e data lakes.
- **Avro:** orientado a **linha**, rápido na escrita, forte em **schema evolution**, bom para **Kafka**.
</details>

**25. ➕ O que é o ORC?**
<details><summary>Resposta</summary>

Formato **colunar** do ecossistema **Hive/Hadoop**, com excelente compressão. Bom para batch.
</details>

---

## Aula 3: ETL, streaming e latência

**26. O que significa ETL e o que cada letra faz?**
<details><summary>Resposta</summary>

**Extract** (coleta das fontes), **Transform** (limpa, junta, modela), **Load** (carrega o dado pronto no destino).
</details>

**27. O que fazer quando os dados são muito pesados?**
<details><summary>Resposta</summary>

**Pré-prepará-los** em um banco específico, já com **joins e filtros**.
</details>

**28. O Apache Flink possui persistência?**
<details><summary>Resposta</summary>

**Não.** Ele é só uma **passagem** dos dados.
</details>

**29. Que latência o streaming exige e o que a piora?**
<details><summary>Resposta</summary>

Exige latência **baixa**. **Trafegar dados na rede** gera latência alta.
</details>

**30. ➕ Batch x Stream: latência, custo e quando roda?**
<details><summary>Resposta</summary>

- **Batch:** latência **alta**, custo menor, roda em **intervalos agendados**.
- **Stream:** latência **baixa**, custo e complexidade maiores, roda **continuamente**.
</details>

**31. ➕ Cite ferramentas típicas de batch e de stream.**
<details><summary>Resposta</summary>

- Batch: Airflow, BigQuery, Redshift, Snowflake.
- Stream: Kafka, Flink, Kinesis, Dataflow.
</details>

**32. ➕ O que é o Flink segundo a AWS e que recursos ele tem?**
<details><summary>Resposta</summary>

Mecanismo **distribuído, open source**, para processamento **com estado** de dados ilimitados (fluxos) e limitados (lotes). Tem **tempo de evento**, **checkpoints/savepoints** e APIs em vários níveis (SQL, Table, DataStream).
</details>

**33. ➕ RabbitMQ x Kafka: modelo de entrega e retenção?**
<details><summary>Resposta</summary>

- **RabbitMQ:** **push**, **exclui** a mensagem após o consumo, filas prioritárias.
- **Kafka:** **pull**, **retém** as mensagens e permite **reprocessar**. Milhões de mensagens por segundo.
</details>

**34. ➕ Quando usar RabbitMQ e quando usar Kafka?**
<details><summary>Resposta</summary>

- **RabbitMQ:** roteamento complexo, protocolos legados (MQTT, STOMP), entrega garantida.
- **Kafka:** tempo real, replay de eventos, big data contínuo, alto volume.
</details>

---

## Aula 4: Data Warehouse, Data Lake e Lakehouse

**35. Qual a linha do tempo dessas arquiteturas?**
<details><summary>Resposta</summary>

**Data Warehouse, Data Lake, Data Lakehouse.**
</details>

**36. O que é o Star Schema e por que usar?**
<details><summary>Resposta</summary>

Modelo de **data warehouse** que **agrega os dados** (tudo relacional). **Evita vários joins**, pois os dados já estão prontos para busca.
</details>

**37. O que o Data Lake guarda e o que ele é?**
<details><summary>Resposta</summary>

**Todos os formatos**, de **várias origens**. É um **object storage** (como o S3).
</details>

**38. Por que o Data Lake não tem hierarquia de pastas?**
<details><summary>Resposta</summary>

Para **não precisar de recursividade** nas buscas.
</details>

**39. Por que o Data Lake passou a ser possível?**
<details><summary>Resposta</summary>

Porque o **armazenamento ficou mais barato**.
</details>

**40. O que o Data Lakehouse adiciona ao lake?**
<details><summary>Resposta</summary>

Uma **camada de metadados e governança**: de onde veio, qualidade, quem atualizou etc.
</details>

**41. O MongoDB tem join?**
<details><summary>Resposta</summary>

**Não.**
</details>

**42. ➕ O que o Lakehouse traz do data warehouse (Databricks)?**
<details><summary>Resposta</summary>

**Transações ACID**, **aplicação de esquema** e governança, sobre **formatos abertos** (Parquet). O **Delta Lake** implementa a camada de metadados.
</details>

**43. ➕ Schema-on-read x schema-on-write: quem usa qual?**
<details><summary>Resposta</summary>

- **Data Lake:** schema-on-**read** (define ao ler).
- **Data Warehouse:** schema-on-**write** (define ao gravar).
- **Lakehouse:** os dois.
</details>

**44. ➕ O que é o Apache Airflow?**
<details><summary>Resposta</summary>

Um **orquestrador de workflows**: agenda e encadeia tarefas, típico de **batch**.
</details>

---

## Aula 5: Flink na prática (tempo, watermarks e connectors)

**45. O que é o ISO 8601 e o que é o Epoch UNIX?**
<details><summary>Resposta</summary>

- **ISO 8601:** padrão de timestamp em **texto**, com UTC ou sem.
- **Epoch UNIX:** timestamp como **inteiro**.
</details>

**46. O que são watermarks no Flink?**
<details><summary>Resposta</summary>

**Registros inseridos nos dados** para **marcar a passagem do tempo**.
</details>

**47. O que são Faker e Datagen?**
<details><summary>Resposta</summary>

Geradores de **dados sintéticos**. O Faker nasceu em **Java**, usa **providers**, e no Flink é o **flink-faker**.
</details>

**48. Como se chama tudo que é externo ao Flink?**
<details><summary>Resposta</summary>

**Connectors.**
</details>

**49. Para que serve a cláusula `WITH` no SQL do Flink?**
<details><summary>Resposta</summary>

Define o **connector e suas opções**, que **variam conforme o source**. Cria uma **tabela temporária**, depois inserida no sink.
</details>

**50. O que é o `blackhole`?**
<details><summary>Resposta</summary>

Sink para quando **não há destino**: **gera os dados mas não salva em lugar algum**.
</details>

**51. O que é o `sql-client.sh` e como o streaming se comporta?**
<details><summary>Resposta</summary>

É o **terminal SQL do Flink**. O modelo de streaming **roda sem parar**.
</details>

**52. Qual o pipeline do exemplo da aula?**
<details><summary>Resposta</summary>

**Source faker** e **sink Kafka**. (O PyFlink é o Flink com Python.)
</details>

**53. ➕ TIMESTAMP x TIMESTAMP_LTZ no Flink SQL?**
<details><summary>Resposta</summary>

- **TIMESTAMP:** sem fuso (como `LocalDateTime`).
- **TIMESTAMP_LTZ:** guarda em **UTC** e exibe no **fuso local** (como `Instant`).
</details>

**54. ➕ Como converter epoch em timestamp no Flink SQL?**
<details><summary>Resposta</summary>

`TO_TIMESTAMP_LTZ(epoch, precisão)`. Precisão **0** para segundos, **3** para milissegundos.
</details>

**55. ➕ Event time x processing time?**
<details><summary>Resposta</summary>

- **Event time:** timestamp **dentro do dado**, recomendado, resultado reproduzível.
- **Processing time:** relógio da máquina, gera **não determinismo**.
</details>

**56. ➕ Quando watermarks são necessárias?**
<details><summary>Resposta</summary>

Em operações com estado e tempo: **janelas**, **joins temporais**, **top-N**, **MATCH_RECOGNIZE**. **Não** em `SELECT/WHERE` simples.
</details>

**57. ➕ Como um tipo nullable vira Avro? E o que é BYTES?**
<details><summary>Resposta</summary>

- Nullable vira **`union(tipo, null)`**.
- `BYTES` = `VARBINARY(2147483647)`, sequência de bytes de tamanho variável.
</details>

**58. ➕ No exemplo RabbitMQ + PyFlink, quais as filas e portas?**
<details><summary>Resposta</summary>

Filas **`fila01_source`** (entrada) e **`fila01_sink`** (saída). Painel do RabbitMQ na porta **15672** e dashboard do Flink na **8081**.
</details>

---

## Aula 6: ETL x ELT

**59. Qual a diferença de ordem entre ETL e ELT?**
<details><summary>Resposta</summary>

- **ETL:** Extract, **Transform**, Load. Transforma **antes** da carga.
- **ELT:** Extract, **Load**, Transform. Transforma **depois**, no destino.
</details>

**60. Onde o ETL transforma e onde o ELT transforma?**
<details><summary>Resposta</summary>

- ETL: em um **servidor intermediário dedicado**.
- ELT: **no próprio destino** (data lake ou warehouse cloud).
</details>

**61. Para que volume e tipo de dado cada um é melhor?**
<details><summary>Resposta</summary>

- ETL: **volumes menores**, dados **estruturados**.
- ELT: **grandes volumes**, dados **semi/não estruturados**.
</details>

**62. Compare latência e custo de ETL e ELT.**
<details><summary>Resposta</summary>

- ETL: **maior latência**; custo concentrado em **servidores dedicados**.
- ELT: **menor latência**; custo **elástico**, sob demanda.
</details>

**63. Qual o trade-off de governança?**
<details><summary>Resposta</summary>

- ETL valida e limpa **antes**: menos risco de expor dado sensível bruto.
- ELT guarda o bruto: exige **controle de acesso robusto** no destino.
</details>

**64. Qual o trade-off de custo de storage x processamento?**
<details><summary>Resposta</summary>

- ELT gasta mais em **armazenamento** (dado bruto).
- ETL gasta mais em **poder de transformação dedicado**.
</details>

**65. Qual a vantagem de analítica do ELT?**
<details><summary>Resposta</summary>

Preserva o dado **bruto (raw)**: permite **várias transformações** e reprocessar **sem re-extrair** da origem.
</details>

**66. Quando usar ETL?**
<details><summary>Resposta</summary>

**Sistemas legados** (ERP, CRM on-premise), **exigência regulatória** de dado mascarado/validado antes de armazenar, **batch tradicional** com volume previsível.
</details>

**67. Quando usar ELT?**
<details><summary>Resposta</summary>

**Streaming e alto volume** (logs, IoT, cliques), **data lakes e lakehouses** (ex.: Delta Lake), ambientes **cloud-native** com warehouses elásticos.
</details>

**68. Descreva a arquitetura de um pipeline ELT moderno.**
<details><summary>Resposta</summary>

Fontes, **Extract**, **zona RAW** do data lake (**Load**), **Transform** no próprio warehouse, **zona CURATED**/warehouse, depois dashboards, ML e relatórios.
</details>

**69. Quais ferramentas comuns de um pipeline ELT?**
<details><summary>Resposta</summary>

**Fivetran/Airbyte** (Extract + Load) com **dbt** (Transform), sobre Snowflake, BigQuery ou Databricks.
</details>

**70. ➕ Extração, carga: o que é "staging" e full x incremental?**
<details><summary>Resposta</summary>

**Staging** é a área temporária onde o ETL guarda os dados extraídos. **Full load** carrega tudo; **incremental** carrega só o que mudou.
</details>

**71. ➕ Segundo a AWS, quando ETL ainda faz sentido?**
<details><summary>Resposta</summary>

**Bancos legados**, **experimentos de dados**, **IoT na borda** e análises complexas. ELT é a escolha padrão para análises modernas.
</details>

---

## Aula 7: Arquitetura Medallion e CDC

**72. Quais as camadas da Arquitetura Medallion?**
<details><summary>Resposta</summary>

**Bronze** (raw data), **prata** e **ouro**.
</details>

**73. Que formato aparece nas anotações para a camada bronze?**
<details><summary>Resposta</summary>

**Parquet (com compressão snappy)**.
</details>

**74. O que é CDC?**
<details><summary>Resposta</summary>

**Change Data Capture**: design pattern que **captura alterações do banco em tempo real**, intercepta dados na fonte e **replica** (ex.: para o Kafka).
</details>

**75. O CDC reprocessa tudo?**
<details><summary>Resposta</summary>

**Não.** Foca nas **mudanças incrementais**, sempre monitorando o banco.
</details>

**76. O CDC captura dados que existiam antes de ser implantado?**
<details><summary>Resposta</summary>

**Não.** Ele **não olha o passado**.
</details>

**77. Quais as 3 formas de CDC?**
<details><summary>Resposta</summary>

**Log**, **trigger** e **timestamp**.
</details>

**78. Como funciona o CDC por log e por que é o melhor para Big Data?**
<details><summary>Resposta</summary>

Inspeciona os **logs de transação (DML)** e repassa as alterações. É **a mais popular**, tem **baixa latência** e **não sobrecarrega** a origem.
</details>

**79. Como funciona o CDC por trigger?**
<details><summary>Resposta</summary>

Igual a uma função de banco: ao ocorrer a alteração, **grava em outro lugar**. **Custo maior**, sobrecarrega o sistema.
</details>

**80. Como funciona o CDC por timestamp e qual o problema?**
<details><summary>Resposta</summary>

Usa campo de **auditoria** e **dispara consultas** comparando com a última. **Sobrecarrega**, pois consulta o banco o tempo todo.
</details>

**81. O que é o Debezium?**
<details><summary>Resposta</summary>

Um **plugin do banco** (SQL e NoSQL) que traz o log de forma **mais estruturada**. Geralmente usado com o **Kafka Connect**. Envia **JSON**.
</details>

**82. Para que serve o campo `op` na mensagem do Debezium?**
<details><summary>Resposta</summary>

Indica o **tipo da ação**: `insert`, `update`, `delete` etc.
</details>

**83. Que tópico o Debezium cria no Kafka?**
<details><summary>Resposta</summary>

Um tópico com o **esquema e o nome da tabela** no nome.
</details>

**84. O que é o WAL do Postgres?**
<details><summary>Resposta</summary>

**Write Ahead Logging**: grava no log **o que vai acontecer antes de efetivar**. Grava só registros **incrementais**. Precisa ser **habilitado**, com **replicação lógica**.
</details>

**85. ➕ O que contém cada camada da Medallion?**
<details><summary>Resposta</summary>

- **Bronze:** dado bruto.
- **Prata:** dado limpo e padronizado.
- **Ouro:** dado agregado, pronto para negócio, BI e ML.
</details>

**86. ➕ O que o CDC acompanha e onde é usado?**
<details><summary>Resposta</summary>

Acompanha **INSERT, UPDATE e DELETE**. Usos: **replicação**, DW em tempo real, **microsserviços**, **auditoria e conformidade**.
</details>

**87. ➕ Cite ferramentas de CDC.**
<details><summary>Resposta</summary>

**Debezium**, **AWS DMS**, **Google Datastream**, com **Kafka** como espinha dorsal.
</details>
