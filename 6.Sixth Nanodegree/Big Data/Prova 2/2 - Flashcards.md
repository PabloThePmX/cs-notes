# Big Data: Flashcards (Prova 2)

> Leia a pergunta, **tente responder de cabeça**, e só então clique em "Resposta".

---

## Aula 8: PyFlink (DataStream, Table API e FlinkSQL)

**1. O que é o PyFlink e por que ele precisa dos JARs do Java?**
<details><summary>Resposta</summary>

É a **API Python** do Flink. O Flink foi escrito em **Java** e o Python é **só uma interface**: os connectors rodam na JVM, então o **JAR** de cada connector precisa ser declarado/existir.
</details>

**2. Quais as 3 camadas de API do Flink vistas em aula, da mais baixa para a mais alta?**
<details><summary>Resposta</summary>

**DataStream → Table API → SQL (FlinkSQL)**.
</details>

**3. Qual a principal diferença conceitual entre Table API e DataStream API?**
<details><summary>Resposta</summary>

- **Table API:** **declarativa**, abstrai detalhes internos, interface **parecida com SQL** para dados **estruturados**.
- **DataStream API:** **imperativa**, mais baixo nível, mais controle.
</details>

**4. Qual o fluxo mais comum para trabalhar no PyFlink, segundo a aula?**
<details><summary>Resposta</summary>

Pegar um **DataStream**, **converter para Table API** e aí sim trabalhar (com SQL).
</details>

**5. Os connectors do DataStream e da SQL/Table API são os mesmos?**
<details><summary>Resposta</summary>

**Não.** SQL & Table API têm **connectors diferentes** dos do DataStream.
</details>

**6. O que é uma **source** no Flink?**
<details><summary>Resposta</summary>

O componente que **fornece os dados de entrada** ao job (ex.: Kafka, DataGen, RabbitMQ).
</details>

**7. O que é um **sink** no Flink?**
<details><summary>Resposta</summary>

O **ponto de saída** dos dados **após o processamento** (ex.: Kafka, MongoDB, `print`). Conecta com sistemas externos; não é só para debug.
</details>

**8. O que é o connector **DataGen**?**
<details><summary>Resposta</summary>

Uma source que **gera dados aleatórios** em memória, para teste. Parecido com o **Faker**, mas **ainda mais aleatório, sem filtros**.
</details>

**9. O que faz `.option("rows-per-second", "1")` no DataGen?**
<details><summary>Resposta</summary>

Gera **1 linha por segundo**.
</details>

**10. Para que serve o connector `print`?**
<details><summary>Resposta</summary>

É um **sink** que **imprime** os registros no stdout (para ver o pipeline funcionando).
</details>

**11. No exemplo do professor, o que fazem `col(...)` e `lit(...)`?**
<details><summary>Resposta</summary>

- `col("num")`: referencia a **coluna** `num`.
- `lit('hello')`: um **valor literal** (constante) em todas as linhas.
</details>

**12. Para que servem `execute_insert("print_sink")` e `.wait()`?**
<details><summary>Resposta</summary>

- `execute_insert`: **insere** o resultado no sink e **dispara o job**.
- `.wait()`: mantém o script **esperando** o job contínuo.
</details>

**13. Qual comando SQL define um processamento **contínuo** da fonte para o destino no PyFlink?**
<details><summary>Resposta</summary>

**`INSERT INTO sink_table SELECT ... FROM source_table`**.
</details>

**14. Qual o primeiro passo no código Python de um job Flink?**
<details><summary>Resposta</summary>

**Pegar o ambiente de execução** (`env` / `t_env`).
</details>

**15. Como dar nome ao pipeline (job) no Flink?**
<details><summary>Resposta</summary>

Pelo **`env`** (ex.: `env.execute("nome do job")`). Esse é o nome que aparece no Flink.
</details>

**16. Como se coloca um job PyFlink no ar?**
<details><summary>Resposta</summary>

Pela **CLI**, com o binário do Flink: `/opt/flink/bin/flink run -py rabbit.py`.
</details>

**17. Por que o job Python não é enviado pelo dashboard do Flink?**
<details><summary>Resposta</summary>

O **dashboard só aceita JARs**, não Python.
</details>

**18. Onde aparece o resultado de `res_ds.print()` rodando no Docker?**
<details><summary>Resposta</summary>

Nos **logs do TaskManager**: Docker Desktop ou `docker logs flink-taskmanager`.
</details>

**19. Quais métodos convertem entre DataStream e Table?**
<details><summary>Resposta</summary>

- DataStream → Table: `t_env.from_data_stream(ds)`.
- Table → DataStream: `t_env.to_data_stream(table)` ou `to_changelog_stream(table)` (com updates).
</details>

**20. O que significa "destrinchar" os dados no pipeline?**
<details><summary>Resposta</summary>

Decidir **onde separar** os dados e **quais critérios** usar (ex.: quebrar o JSON da API em colunas).
</details>

**21. Quais as etapas da atividade em aula com a Open-Meteo?**
<details><summary>Resposta</summary>

**API (requests) → gravar no Kafka → consumir do Kafka com FlinkSQL → gravar no MongoDB.**
</details>

**22. ➕ Tabelas temporárias no Flink SQL: onde ficam e quanto duram?**
<details><summary>Resposta</summary>

Ficam **só na sessão** (memória) e são **descartadas quando a sessão/job encerra**. Não são compartilhadas com outras aplicações.
</details>

**23. ➕ O Flink pode ser produtor e consumidor do Kafka?**
<details><summary>Resposta</summary>

**Sim.** Tem **connector nativo**: lê tópicos (source) e grava tópicos (sink), com transformação em tempo real e sem perder escalabilidade.
</details>

**24. ➕ Como funciona a ordem de leitura dos consumidores no Kafka?**
<details><summary>Resposta</summary>

Consumidores leem de **tópicos**, e a **ordem é garantida por partição** (não no tópico inteiro).
</details>

**25. ➕ Num consumer group, quantos consumidores leem cada partição?**
<details><summary>Resposta</summary>

**Um só** por partição dentro do grupo. Grupos diferentes podem ler o mesmo tópico inteiro.
</details>

**26. ➕ JobManager x TaskManager?**
<details><summary>Resposta</summary>

- **JobManager:** coordena (agenda, checkpoints, recuperação).
- **TaskManager:** **executa** as tarefas.
</details>

---

## Aula 9: Deduplicação de dados em streaming

**27. Duplicatas em streaming são um bug do pipeline?**
<details><summary>Resposta</summary>

**Não.** São **consequência do projeto** (da natureza da operação). Sistemas distribuídos priorizam **confiabilidade em vez de precisão**.
</details>

**28. Por que nem descartar nem ficar em retry é bom?**
<details><summary>Resposta</summary>

**Descartar** perde dados; **retry infinito** trava a fila: **a mensageria não anda**.
</details>

**29. Qual o custo de ignorar duplicatas?**
<details><summary>Resposta</summary>

De **métricas infladas** (receita em dobro) até **agregações corrompidas que envenenam os modelos** a jusante.
</details>

**30. Quais as 4 fontes de duplicatas?**
<details><summary>Resposta</summary>

1. Entrega **at-least-once** (ACK perdido)
2. **Retentativas de produtores** (ex.: webhook)
3. **Sobreposição snapshot x stream no CDC**
4. **Reinícios de pipeline e checkpointing**
</details>

**31. Como a entrega at-least-once gera duplicata?**
<details><summary>Resposta</summary>

O produtor espera o **ACK**. Se ele se perde (timeout/failover), o produtor **reenvia**, mas o broker já tinha gravado → **2 cópias**.
</details>

**32. Dê o exemplo de duplicata por retentativa de produtor (webhook).**
<details><summary>Resposta</summary>

O webhook é processado, mas o receptor devolve **503** por problema **transitório no balanceador de carga**. O emissor tenta de novo e o evento fica **registrado 2 vezes**.
</details>

**33. Por que o CDC gera duplicata na sobreposição snapshot x stream?**
<details><summary>Resposta</summary>

Linhas alteradas **durante o snapshot** aparecem **no snapshot e no stream de mudanças** (WAL/binlog).
</details>

**34. Por que reinícios com checkpoint geram duplicatas?**
<details><summary>Resposta</summary>

Se o job falha entre dois checkpoints, volta ao **último checkpoint** e **reprocessa** o que veio depois. É intencional para **não perder** dados.
</details>

**35. At-most-once, at-least-once e exactly-once: quantas vezes chega?**
<details><summary>Resposta</summary>

- **At-most-once:** 0 ou 1 (pode **perder**).
- **At-least-once:** 1 ou mais (pode **duplicar**).
- **Exactly-once:** exatamente 1.
</details>

**36. Quando o at-most-once é aceitável?**
<details><summary>Resposta</summary>

Em aplicações onde perder uma mensagem não é grave, como **telemetria** (IoT).
</details>

**37. Quais as 4 estratégias de deduplicação?**
<details><summary>Resposta</summary>

1. **Semântica exactly-once**
2. **Deduplicação com estado** (stateful)
3. **Sinks idempotentes** (UPSERT)
4. **Deduplicação com janela de tempo**
</details>

**38. Qual o limite da semântica exactly-once?**
<details><summary>Resposta</summary>

Só cobre **a fronteira que controla**. **Não impede duplicatas vindas da origem** nem da sobreposição do CDC.
</details>

**39. Como funciona a deduplicação com estado e qual o custo?**
<details><summary>Resposta</summary>

Guarda em estado as **chaves já vistas** (histórico): viu → descarta; nova → emite. Custo: o estado **cresce** com as chaves e pode **esgotar a memória**.
</details>

**40. O que é um sink idempotente?**
<details><summary>Resposta</summary>

Gravar o mesmo registro várias vezes dá **o mesmo resultado** que gravar uma. Ex.: **UPSERT** (`INSERT ... ON CONFLICT DO UPDATE`). É a **última linha de defesa**.
</details>

**41. Qual o problema do UPSERT com muitas duplicatas (ex.: IoT)?**
<details><summary>Resposta</summary>

**Performance**: o banco precisa checar conflito a cada escrita; UPSERT é mais lento que INSERT.
</details>

**42. Como funciona a deduplicação com janela de tempo?**
<details><summary>Resposta</summary>

Só verifica as chaves de uma **janela recente** (ex.: últimos **10 minutos**). Estado limitado, mas **perde duplicatas tardias**.
</details>

**43. O que é idempotência?**
<details><summary>Resposta</summary>

Executar/entregar **mais vezes não muda o resultado**.
</details>

**44. O que é o Lamport clock?**
<details><summary>Resposta</summary>

Um **relógio lógico** que **ordena eventos sem precisar de um relógio físico** sincronizado.
</details>

**45. Qual o padrão de deduplicação do Flink SQL?**
<details><summary>Resposta</summary>

A window function **`ROW_NUMBER()`**: **PARTITION BY** a chave, **ORDER BY** o timestamp, e **WHERE row_num = 1**.
</details>

**46. No ROW_NUMBER, como manter o mais recente x o primeiro?**
<details><summary>Resposta</summary>

- Mais recente: `ORDER BY ... DESC`.
- Primeiro (first-write-wins): `ORDER BY ... ASC`.
</details>

**47. O que é State TTL no Flink?**
<details><summary>Resposta</summary>

**Time To Live**: o estado **expira automaticamente** depois de um tempo (`table.exec.state.ttl`). TTL de 24h = deduplica só dentro de 24h.
</details>

**48. O que é `PROCTIME()`?**
<details><summary>Resposta</summary>

Função do Flink que dá o **tempo de processamento**: o **horário do cluster que executou**, em vez do tempo do evento.
</details>

**49. Deduplicação ilimitada x limitada no tempo: qual o trade-off?**
<details><summary>Resposta</summary>

**Ilimitada:** pega tudo, mas o estado **cresce sem parar**. **Limitada:** estado previsível, mas **deixa passar duplicatas tardias**. Correção x recursos.
</details>

**50. Como ativar o produtor idempotente no Kafka e como ele funciona?**
<details><summary>Resposta</summary>

`enable.idempotence=true`. Cada mensagem ganha um **número de sequência**; o broker **descarta** a que já confirmou. Resolve duplicata de **retry do produtor**.
</details>

**51. O que são escritas transacionais no Kafka?**
<details><summary>Resposta</summary>

Transação como num **banco relacional**: **ou tudo, ou nada** (commit/rollback). Torna **atômico** ler de um tópico e escrever em outro.
</details>

**52. O que é o isolamento do consumidor no Kafka?**
<details><summary>Resposta</summary>

`isolation.level=read_committed`: o consumidor só lê mensagens de **transações confirmadas**. Equivale ao **I** do **ACID**.
</details>

**53. Quais as 3 camadas da defesa em profundidade?**
<details><summary>Resposta</summary>

1. **Origem/Kafka:** produtor idempotente, exactly-once.
2. **Processador (Flink):** ROW_NUMBER, dedup com estado.
3. **Sink:** UPSERT/MERGE na chave primária.
</details>

**54. ➕ O que significam `acks=0`, `acks=1` e `acks=all`?**
<details><summary>Resposta</summary>

- `0`: não espera confirmação.
- `1`: espera o **líder**.
- `all`: espera **todas as réplicas em sincronia** (mais seguro).
</details>

**55. ➕ Commit do offset antes x depois de processar: o que acontece numa falha?**
<details><summary>Resposta</summary>

- **Antes:** perde a mensagem (at-most-once).
- **Depois:** reprocessa (at-least-once).
</details>

**56. ➕ HashMapStateBackend x RocksDBStateBackend?**
<details><summary>Resposta</summary>

- **HashMap:** estado em **memória**, baixa cardinalidade.
- **RocksDB:** transborda para **disco**, alta cardinalidade.
</details>

**57. ➕ Como o ClickHouse deduplica?**
<details><summary>Resposta</summary>

`ReplacingMergeTree`: guarda as versões e **colapsa em merges em segundo plano** (dedup **eventual**; use `FINAL` para garantir).
</details>

---

## Aula 10: Apache Airflow e orquestração

**58. O que é o Apache Airflow?**
<details><summary>Resposta</summary>

Ferramenta de **orquestração** de workflows: mapeia e verifica fluxos de dados, com **agendamento de tarefas**, garantindo **ordem, sequência, logs e alertas**.
</details>

**59. O Airflow foca em batch ou stream? Por quê?**
<details><summary>Resposta</summary>

**Batch.** Pipelines agendados podem ser **refeitos/reprocessados**, o que é comum em batch.
</details>

**60. Com o que o Airflow é comparado em aula?**
<details><summary>Resposta</summary>

Com um **`cronjob` do Linux**: um **agendador** que chama outros scripts/plataformas e controla o fluxo.
</details>

**61. O que o Airflow precisa para funcionar, além do código?**
<details><summary>Resposta</summary>

Um **banco de dados** (o banco de **metadados**).
</details>

**62. O que significa DAG?**
<details><summary>Resposta</summary>

**Directed Acyclic Graph**: grafo **direcionado** (arestas têm direção) e **acíclico** (sem ciclos/loops, não volta a um passo anterior).
</details>

**63. O que um DAG representa no Airflow?**
<details><summary>Resposta</summary>

Um **fluxo de trabalho**: as **tarefas** (vértices) e suas **dependências** (arestas).
</details>

**64. Em que linguagem se definem os pipelines no Airflow? E para que serve a interface?**
<details><summary>Resposta</summary>

Em **Python**. A **interface** é mais para **ver** os fluxos, execuções e **logs**.
</details>

**65. O que é um operator no Airflow?**
<details><summary>Resposta</summary>

O **comando/tipo** de tarefa (classe de `airflow.operators`, ex.: `PythonOperator`). Dá para criar operators próprios.
</details>

**66. Para que serve o `python_callable`?**
<details><summary>Resposta</summary>

É a propriedade do operator que **recebe a função Python** a ser executada.
</details>

**67. O que define a ordem de execução das tasks?**
<details><summary>Resposta</summary>

As **dependências explícitas**, com o operador **`>>`** (sobrecarga de operador) ou `set_downstream`. Não é a ordem de escrita no arquivo.
</details>

**68. Como rodar duas tasks em paralelo antes de uma terceira?**
<details><summary>Resposta</summary>

`[task1, task2] >> task3`.
</details>

**69. Como se agenda um DAG?**
<details><summary>Resposta</summary>

Com intervalos (**diário, por hora**) ou expressão **cron** (o **crontab guru** ajuda), ou por **triggers** (manual, API, evento).
</details>

**70. O que são sensors?**
<details><summary>Resposta</summary>

Tasks (lib `sensors`) que **ficam escutando** uma condição, ex.: **tópico do Kafka** disparando o pipeline. São **async**, pois só esperam.
</details>

**71. Onde ficam os scripts dos DAGs?**
<details><summary>Resposta</summary>

Na **pasta designada** (`dags/`), de onde o Airflow os lê.
</details>

**72. Que visão da interface mostra a duração e sobreposição das tasks?**
<details><summary>Resposta</summary>

O **diagrama de Gantt**.
</details>

**73. ➕ Qual a função do Metadata Database do Airflow?**
<details><summary>Resposta</summary>

**Persistir o estado** de tasks e DAG runs, **variáveis, conexões** e histórico.
</details>

**74. ➕ Quais os componentes da arquitetura do Airflow?**
<details><summary>Resposta</summary>

**Scheduler**, **Executor**, **Workers**, **Webserver (UI)**, **Metadata Database** e a **pasta de DAGs**.
</details>

**75. ➕ Scheduler x Worker?**
<details><summary>Resposta</summary>

- **Scheduler:** decide **o que e quando** rodar.
- **Worker:** **executa** a task.
</details>

**76. ➕ O que é XCom?**
<details><summary>Resposta</summary>

**Cross-communication**: troca de **pequenos dados** entre tasks.
</details>

**77. ➕ O que faz `catchup=True`?**
<details><summary>Resposta</summary>

Roda os intervalos **passados** desde o `start_date` que ficaram para trás (**backfill**).
</details>

**78. ➕ Leia o cron `0 3 * * *`.**
<details><summary>Resposta</summary>

Campos: minuto hora dia mês dia-da-semana → **todo dia às 3h00**.
</details>

**79. ➕ Qual a principal vantagem do ELT com dbt?**
<details><summary>Resposta</summary>

**Aproveitar o poder de processamento do próprio Data Warehouse** para fazer as transformações (o T, em SQL).
</details>
