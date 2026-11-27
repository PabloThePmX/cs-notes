# Big Data: Resumo para estudo (Prova 2)

> Como usar: leia o resumo, depois faça os **flashcards** e por último o **quiz**.
> Cada aula tem uma caixa **💡 Para fixar** com um truque de memória.

> **Complementos ➕:** no fim de cada aula há uma seção **"➕ Complemento para a prova"** com conteúdo padrão da área (documentação do Flink, Kafka e Airflow) que **não apareceu em aula**. Priorize o que veio da aula e use os ➕ para reforçar. Não dá para saber o que o professor vai cobrar: confirme com ele.

**Fontes usadas:** anotações das Aulas 8, 9 e 10, o `conteudos.txt` que o professor passou (PyFlink, DataGen, atividade Open-Meteo, links de deduplicação no Kafka), o PDF *"Deduplicação de Dados em Tempo Real"* (Streamkap) e a **prova antiga** (12 questões, todas reaproveitadas no quiz).

---

## Mapa geral (a visão de cima)

```
Aula 8   PyFlink: DataStream, Table API e FlinkSQL em Python; DataGen; source/sink; rodar job pela CLI
Aula 9   Deduplicação em streaming: de onde vêm as duplicatas, estratégias, ROW_NUMBER, Kafka idempotente
Aula 10  Apache Airflow: orquestração, DAG, operadores, agendamento, sensors
```

**Sobre o estilo da prova:** a prova antiga tem **12 questões de múltipla escolha com 5 alternativas (a–e)**, incluindo uma de **V/F** (sequência tipo "V-V-F-V"). Cobra **definição** ("o que representa um DAG", "o que é um sink") e **função de componente** ("função do banco de metadados do Airflow"). O quiz daqui usa **4 alternativas** (formato do site), mas as perguntas antigas foram mantidas com o mesmo enunciado.

⚠️ A prova antiga também perguntou sobre **ELT com DBT** (conteúdo da Prova 1, Aula 6). Vale revisar **ETL x ELT** no material da Prova 1.

---

# Aula 8: PyFlink (DataStream, Table API e FlinkSQL)

## O que é o PyFlink
- **PyFlink** = a API **Python** do Apache Flink.
- O Flink foi escrito em **Java**. O Python é **só uma interface** para ele: por baixo, quem executa é a JVM.
- Por isso, **dentro do Python é preciso declarar as bibliotecas (JARs) do Java** que o job usa, como os connectors.
  - Ex.: o connector **RMQ** (RabbitMQ) chama o connector do Java, então **o JAR dele precisa existir**.

> 💡 **Para fixar:** PyFlink é um **controle remoto** em Python para uma máquina Java. Se a peça (JAR) não estiver na máquina, o controle não adianta.

## As camadas de API: DataStream → Table API → SQL

| | **DataStream API** | **Table API** | **Flink SQL** |
|---|---|---|---|
| Estilo | **Imperativo** (você diz *como*, passo a passo) | **Declarativo**, relacional (métodos tipo `select`, `filter`) | **Declarativo**, SQL puro |
| Nível | Mais **baixo**, mais controle (estado, tempo) | Intermediário | Mais **alto**, mais abstrato |
| Dados | Fluxo de objetos/eventos | Tabelas com **schema** | Tabelas com **schema** |
| Connectors | Os do DataStream | Os de **SQL & Table API** (são **diferentes** dos do DataStream) | Os mesmos da Table API |

- **Fluxo mais comum na aula:** pegar um **DataStream**, **converter para Table API** e aí sim trabalhar (com SQL).
- A Table API **abstrai detalhes internos** e usa uma interface **parecida com SQL** para transformações **estruturadas**.

> 💡 **Para fixar:** **DataStream = câmbio manual**; **Table/SQL = câmbio automático**. Os dois andam em stream e em batch.

⚠️ **Pegadinha (prova antiga):** a **Table API é declarativa** e a **DataStream é imperativa** (não o contrário). Ambas suportam **event-time** e ambas existem em **Java e Python**.

## Montando o pipeline (job) em Python
O job é um pipeline: **source → transformação → sink** (o que dá para fazer depende do connector).

| Componente | Função |
|---|---|
| **Source** | **Fornece os dados de entrada** ao job (ex.: Kafka, DataGen, RabbitMQ, API) |
| **Transformação** | Processa: filtra, seleciona, agrega, **destrincha** os dados |
| **Sink** | **Ponto de saída** dos dados após o processamento (ex.: Kafka, MongoDB, banco, `print`) |

Passos no código:
1. **Pegar o ambiente de execução** (`env` / `t_env`).
2. Declarar os **JARs** dos connectors Java.
3. Criar a **tabela source** e a **tabela sink**.
4. Transformar e **inserir** da source no sink.
5. Pelo **`env`** dá para **dar nome ao pipeline** (o nome do job no Flink).

- **"Destrinchar" os dados:** decidir **onde separar** e **quais critérios** usar (ex.: quebrar o JSON da API em colunas).

> 💡 **Para fixar:** **S**ource **e**ntra, **S**ink **s**ai. A ordem é sempre "de onde vem → o que faço → para onde vai".

⚠️ **Pegadinha:** **sink NÃO é** "o que captura a entrada" (isso é source) e **não é só para debug**: ele **se conecta a sistemas externos**.

## Exemplo do professor: DataGen → Print

```python
from pyflink.table import (EnvironmentSettings, TableEnvironment,
                           DataTypes, TableDescriptor, Schema)
from pyflink.table.expressions import col, lit

# 1) ambiente (modo streaming)
t_env = TableEnvironment.create(EnvironmentSettings.in_streaming_mode())

# 2) source: gerador de dados em memória
t_env.create_table("generator_source",
    TableDescriptor.for_connector("datagen")
      .schema(Schema.new_builder().column("num", DataTypes.BIGINT()).build())
      .option("rows-per-second", "1")
      .build())

# 3) sink: imprime no stdout
t_env.create_table("print_sink",
    TableDescriptor.for_connector("print")
      .schema(Schema.new_builder()
              .column("num", DataTypes.BIGINT())
              .column("hello", DataTypes.STRING()).build())
      .build())

# 4) lê source -> processa -> grava sink
t_env.from_path("generator_source").select(
    col("num").abs % 10, lit('hello pyflink')
).execute_insert("print_sink").wait()
```

| Peça | O que faz |
|---|---|
| `TableEnvironment.create(... in_streaming_mode())` | Cria o ambiente da Table API em modo **streaming** |
| `for_connector("datagen")` | Connector que **gera dados aleatórios** (source de teste) |
| `option("rows-per-second", "1")` | Gera **1 linha por segundo** |
| `for_connector("print")` | Sink que **imprime** a saída (stdout) |
| `from_path(...)` | Lê uma tabela registrada |
| `col("num").abs % 10` | Valor absoluto do `num`, resto da divisão por 10 |
| `lit(...)` | Valor **literal** (constante) em todas as linhas |
| `execute_insert("print_sink")` | **Insere** o resultado no sink (dispara o job) |
| `.wait()` | Mantém o script esperando o job (que é **contínuo**) |

- **DataGen** é parecido com o **Faker** (lib de dados falsos), mas gera dados **ainda mais aleatórios, sem filtros** (sem nomes/e-mails "realistas").

> 💡 **Para fixar:** **DataGen é a torneira de teste**, **Print é o ralo de teste**. Servem para ver o pipeline funcionando sem Kafka nem banco.

## FlinkSQL dentro do Python
A mesma lógica pode ser escrita em SQL com `t_env.execute_sql(...)`:

```sql
CREATE TABLE source_table (...) WITH ('connector' = 'kafka', ...);
CREATE TABLE sink_table   (...) WITH ('connector' = 'mongodb', ...);

INSERT INTO sink_table SELECT * FROM source_table;   -- o job contínuo
```

- O comando que define o **processamento contínuo da fonte para o destino** é o **`INSERT INTO sink SELECT ... FROM source`**. Um `SELECT` sozinho só consulta; o `INSERT INTO` é o que cria o job.
- **`INSERT ... ON CONFLICT`** (UPSERT) apareceu na aula: no destino (banco), se a chave já existe, **atualiza** em vez de inserir. Ver Aula 9.

> 💡 **Para fixar:** no Flink SQL, **`INSERT INTO` = ligar a esteira**. Enquanto a source tiver dados, a esteira não para.

## Conversão DataStream ↔ Table (documentação indicada)
- Usa-se um **`StreamTableEnvironment`** criado a partir do ambiente de stream.
- **DataStream → Table:** `t_env.from_data_stream(ds)`.
- **Table → DataStream:** `t_env.to_data_stream(table)` (tabela só com inserções) ou `t_env.to_changelog_stream(table)` (quando há atualizações/remoções).
- **Onde ver o `print()`?** No Docker, a saída vai para os **logs do TaskManager** (quem executa as tarefas): Docker Desktop ou `docker logs flink-taskmanager`.

## Executando o job
- Usa-se o **binário do Flink pela CLI** para colocar o job no ar:
  `/opt/flink/bin/flink run -py rabbit.py`
- O **dashboard (Web UI) do Flink não deixa enviar Python**, **só JARs**. Por isso, job em Python vai **pela CLI**.

> 💡 **Para fixar:** **Dashboard aceita JAR; Python vai pela porta dos fundos (CLI, `-py`)**.

## Atividade em aula (Open-Meteo → Kafka → MongoDB)
1. **Obter dados via API** (lib `requests`) da Open-Meteo (temperatura por hora na coordenada da Atitus).
2. **Gravar no Kafka** (tópico).
3. **Consumir do Kafka com FlinkSQL** (PyFlink) e **gravar no MongoDB** (sink).

> 💡 **Para fixar:** API (origem) → Kafka (fila/buffer) → Flink (processa) → MongoDB (destino). É o pipeline da Prova 1 na prática.

## ➕ Complemento para a prova

### Tabelas temporárias x permanentes no Flink SQL
| | **Temporária** | **Permanente** |
|---|---|---|
| Onde fica | Só na **memória da sessão** | Em um **catálogo** externo (ex.: Hive Metastore) |
| Duração | **Descartada ao fim da sessão/job** | Persiste entre sessões |
| Compartilhamento | Só aquela sessão enxerga | Visível para outras sessões/aplicações |
| Criação | `CREATE TEMPORARY TABLE ...` | `CREATE TABLE ...` num catálogo persistente |

> 💡 **Para fixar:** **temporária = rascunho**: fechou a sessão, foi pro lixo.

### Flink e Kafka
- O Flink tem **connector nativo para Kafka** e pode atuar **como consumidor (source) e como produtor (sink)**.
- Integrar com Kafka **não tira a escalabilidade**: o paralelismo do Flink pode acompanhar as **partições** do tópico.
- Dá para fazer **transformações em tempo real** sobre os dados do Kafka usando Flink.

### Kafka: consumidores (revisão)
- Consumidores **leem de tópicos**; a **ordem é garantida dentro de cada partição** (não no tópico inteiro).
- **Vários consumidores** podem ler o mesmo tópico (grupos diferentes recebem tudo; dentro de um **consumer group**, cada partição vai para um consumidor só).
- O consumidor controla **onde parou** pelo **offset**, e pode reler mensagens (Kafka guarda por tempo de retenção, não apaga ao ler).
- Comunicação via **protocolo binário próprio sobre TCP** (não HTTP).

### Arquitetura do Flink (para entender o "logs do TaskManager")
- **JobManager:** coordena o job (agenda tarefas, checkpoints, recuperação).
- **TaskManager:** **executa** as tarefas de fato (por isso o `print` aparece nos logs dele).

---

# Aula 9: Deduplicação de dados em streaming

## A ideia central
- **Duplicatas não são bug do pipeline**: são **consequência do projeto** (da natureza da operação).
- Em **computação distribuída**, quase todo sistema **prioriza confiabilidade em vez de precisão**: melhor entregar duas vezes do que perder.
- **Descartar é ruim**, mas **ficar fazendo retry também é ruim**, pois **a fila da mensageria não anda**.
- **Custo de ignorar duplicatas:** de **métricas infladas** e receita contada em dobro até **agregações corrompidas que envenenam os modelos** a jusante.
- Primeiro passo: **verificar a fonte das duplicatas**.

> 💡 **Para fixar:** sistema distribuído é como **carteiro inseguro**: na dúvida, ele entrega de novo. Seu trabalho é não contar a carta duas vezes.

## As 4 fontes de duplicatas
| Fonte | O que acontece |
|---|---|
| **Entrega at-least-once** | O produtor espera o **ACK** do broker. Se o ACK se perde (timeout, failover), ele **reenvia**, mas o broker já tinha gravado. Do lado do consumidor: processou mas **falhou antes de commitar o offset** → recebe de novo |
| **Retentativas de produtores** | Fora do Kafka também. Ex.: **webhook** processado, mas o receptor devolve **503** por um problema **transitório no balanceador de carga**; o emissor tenta de novo → evento registrado **duas vezes** |
| **Sobreposição snapshot x stream no CDC** | O CDC tira um **snapshot** da tabela e depois lê o **stream** de mudanças (WAL, binlog, oplog). Linhas alteradas **durante** o snapshot aparecem **nos dois** |
| **Reinícios de pipeline e checkpointing** | O Flink faz **checkpoint** periódico. Se falha entre dois checkpoints, **volta ao último** e **reprocessa** o que veio depois. É intencional (evita perda), mas gera duplicatas |

> 💡 **Para fixar:** **A-R-S-C** → **A**CK perdido, **R**etry do produtor, **S**napshot do CDC, **C**heckpoint do Flink.

## Garantias de entrega (semânticas)
| Semântica | Quantas vezes chega | Risco | Quando serve |
|---|---|---|---|
| **At-most-once** | **0 ou 1** vez | **Perde** mensagens (remove duplicatas, mas pode remover outras junto) | Aceitável em **telemetria** / IoT, onde perder uma leitura não é grave |
| **At-least-once** | **1 ou mais** vezes | **Duplica** | **Padrão do Kafka**. Espera ACK (tipo handshake) |
| **Exactly-once** | **Exatamente 1** vez | Mais caro / complexo | Financeiro, contagens exatas |

> 💡 **Para fixar:** **most** = no **máximo** um (pode ser zero → perde). **least** = no **mínimo** um (pode ser dois → duplica).

## As estratégias de deduplicação
**Não existe bala de prata.** Usa-se **várias camadas**, cada uma reduzindo o que a próxima precisa tratar.

| Estratégia | Como funciona | Limite / custo |
|---|---|---|
| **Semântica exactly-once** | Kafka: **produtor idempotente + escritas transacionais**. Flink: **checkpoint barriers + sinks transacionais** | Só cobre **a fronteira que controla**. **Não impede duplicatas vindas da origem** nem da sobreposição do CDC |
| **Deduplicação com estado (stateful)** | Guarda em **estado** as chaves já vistas (o **histórico**). Chave vista → descarta. Nova → emite | Estado **cresce** com as chaves únicas; precisa limitar senão **estoura a memória** |
| **Sinks idempotentes** | Escrever o mesmo registro N vezes = escrever 1 vez. **UPSERT** (`INSERT ... ON CONFLICT DO UPDATE`): se existe, **atualiza** | **Última linha de defesa**. UPSERT é mais **lento** que INSERT (checa conflito); com **muitas duplicatas** (ex.: IoT) pode virar problema de **performance** |
| **Deduplicação com janela de tempo** | Só rastreia chaves de uma **janela recente** (ex.: últimos **10 minutos**). Fora da janela = considerado único | Estado **limitado**, mas **perde duplicatas muito tardias** |

- **Idempotência:** fazer/entregar **mais vezes não muda o resultado** (não altera o valor). Ex.: `x = 5` é idempotente; `x = x + 1` não é.
- **Lamport clock:** relógio **lógico** que **ordena eventos sem precisar de um relógio físico** sincronizado (cada processo mantém um contador).

> 💡 **Para fixar:** UPSERT é o **"se já existe, só atualiza a ficha"**. Por isso é a **rede de segurança** no fim do pipeline.

⚠️ **Pegadinha:** **exactly-once NÃO resolve tudo**. Duplicata que já nasce na origem (webhook repetido, snapshot do CDC) passa por ele.

## Deduplicação com Flink SQL: o padrão ROW_NUMBER
É a **abordagem padrão recomendada pela documentação do Flink**, limpa e **declarativa**, usando a **window function `ROW_NUMBER()`**.

**Receita:** **particionar** pela chave → **ordenar** pelo timestamp → manter só o **primeiro ou o último**.

```sql
-- Mantém o registro MAIS RECENTE por chave
SELECT id, name, email, updated_at FROM (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY id ORDER BY updated_at DESC) AS row_num
  FROM user_events
) WHERE row_num = 1;
```

| Quero manter | ORDER BY | Nome |
|---|---|---|
| O **mais recente** | `DESC` | last-write-wins |
| O **primeiro** (mais antigo) | `ASC` | **first-write-wins** |

- As **window functions** fazem um **recorte** da tabela (a partição) sem agrupar as linhas.
- Dá para usar junto com **watermark** do Flink (definido na source).

> 💡 **Para fixar:** **P-O-W** → **P**ARTITION BY chave, **O**RDER BY tempo, **W**HERE row_num = 1.

## Gerenciamento de estado no Flink
O Flink mantém estado **para cada chave única** do `PARTITION BY`. Com chaves de **alta cardinalidade** (milhões de usuários), cresce muito. Duas alavancas:

| Alavanca | Como |
|---|---|
| **State TTL** (Time To Live) | `table.exec.state.ttl`: o estado **expira automaticamente** depois de um tempo (TTL de 24h = deduplica só dentro de 24h) |
| **Tempo de processamento** | Usar **`PROCTIME()`** (horário **do cluster que executou**) em vez do **tempo de evento**. Mais simples de raciocinar |

- **Ilimitada x limitada no tempo:** ilimitada **garante** pegar tudo, mas o estado **cresce sem parar**; limitada tem estado **previsível**, mas deixa passar duplicatas tardias. **Trade-off: correção x recursos.**
- **Chave composta** (user_id + event_type + session_id) gera **muito mais estado** que chave simples: use a **chave mais estreita** que identifique a duplicata.
- **State backend:** `HashMapStateBackend` (em memória, baixa cardinalidade) x `RocksDBStateBackend` (transborda para **disco**, alta cardinalidade).

⚠️ **Pegadinha:** `PROCTIME()` = **tempo de processamento** (relógio da máquina), **não** o tempo em que o evento aconteceu (event-time).

## Deduplicação no nível do Kafka
| Mecanismo | Como | O que resolve |
|---|---|---|
| **Produtor idempotente** | `enable.idempotence=true`. Cada mensagem ganha um **número de sequência**; o broker **descarta** a que já confirmou | Duplicatas por **retentativa do produtor** (retries). **Sem custo para os consumidores** |
| **Escritas transacionais** | Transação **como num banco relacional**: **ou tudo, ou nada** (commit/rollback). Ler de um tópico e escrever em outro vira **atômico** | Padrão **consumir-transformar-produzir** que falha antes de commitar o offset |
| **Isolamento do consumidor** | `isolation.level=read_committed`: o consumidor só vê mensagens de **transações confirmadas** | Fecha o **exactly-once de ponta a ponta** dentro do Kafka (como o **I** do **ACID** nos bancos) |

Configuração típica do produtor: `enable.idempotence=true`, `acks=all`, `retries` alto.

> 💡 **Para fixar:** retry do produtor duplicou? **Liga o produtor idempotente.** É a solução **mais simples** (resposta da prova antiga).

⚠️ **Pegadinha (prova antiga):** "desativar os retries" também evita duplicata, mas **troca duplicata por perda** (vira at-most-once). Não é a resposta.

## Deduplicação no destino (sink)
| Banco | Mecanismo |
|---|---|
| **PostgreSQL** | `INSERT ... ON CONFLICT (id) DO UPDATE SET ... = EXCLUDED....` |
| **Snowflake** | `MERGE INTO ... WHEN MATCHED THEN UPDATE WHEN NOT MATCHED THEN INSERT` |
| **ClickHouse** | `ReplacingMergeTree`: guarda todas as versões e **colapsa em merges em segundo plano** (deduplicação **eventual**; usar `FINAL` para garantir) |

- Alto volume: agrupar upserts em **lotes** e usar **tabela de staging + MERGE** periódico.

## Defesa em profundidade (as 3 camadas)
| Camada | Mecanismo | O que captura |
|---|---|---|
| **Origem / Kafka** | Produtor idempotente, exactly-once | Retentativas de produtor, duplicatas de rede |
| **Processador (Flink)** | `ROW_NUMBER`, dedup com estado | Sobreposição do CDC, reprocessamento por rebalanceamento |
| **Sink** | UPSERT / MERGE na chave primária | Duplicatas tardias, lacunas do TTL, reinícios de pipeline |

**Exemplo do PDF:** CDC do PostgreSQL → Kafka → Flink → Snowflake. 10 milhões de linhas no snapshot, 50 mil alteradas durante ele (aparecem 2×). Produtor idempotente tira as de rede; `ROW_NUMBER` reduz as 50 mil a 1 versão cada; `MERGE` pega o que escapar do TTL.

> 💡 **Para fixar:** **cinto, airbag e freio**: cada camada é barata e pega o que a anterior deixou passar.

## ➕ Complemento para a prova

### Configurações do produtor Kafka
- **`acks=0`**: não espera confirmação (rápido, pode perder).
- **`acks=1`**: espera só o **líder** da partição.
- **`acks=all`** (ou `-1`): espera **todas as réplicas em sincronia** (mais seguro; exigido pelo produtor idempotente).

### Offsets e commit no consumidor
- **Commit antes de processar** → se cair, **perde** a mensagem (at-most-once).
- **Commit depois de processar** → se cair, **reprocessa** (at-least-once).

> 💡 **Para fixar:** a ordem "processa e depois commita" é a que **duplica, mas não perde**.

### Checkpoint barriers (Flink)
- O JobManager injeta **barreiras** no fluxo; quando passam por todos os operadores, o estado é salvo de forma **consistente**. Junto com **sink transacional** (two-phase commit), dá o exactly-once do Flink.

---

# Aula 10: Apache Airflow e orquestração

## O que é o Airflow
- Ferramenta de **orquestração** de workflows: **mapear e verificar um fluxo** (no caso, de dados), com **agendamento de tarefas**.
- Funciona como um **agendador**: **chama outras plataformas e scripts** e **controla o fluxo** (tipo um **`cronjob` do Linux**, mas com mais recursos).
- **Garante ordem, sequência, logs e alertas** do workflow.
- **Foco principal: batch.** Pipelines agendados podem ser **refeitos/reprocessados**, o que é comum em batch, não em stream.
- **Precisa de um banco de dados para funcionar** (o banco de **metadados**).
- Pipelines definidos **em Python** (pipeline como código). A **interface web é mais para ver** os fluxos, logs e execuções.

> 💡 **Para fixar:** Airflow é o **maestro**: ele **não toca** os instrumentos (não processa os dados), só diz **quem toca e quando**.

⚠️ **Pegadinha:** Airflow **não é** ferramenta de processamento de streaming (isso é o Flink). Ele **orquestra**.

## DAG (Directed Acyclic Graph)
- **Grafo:** representação com **vértices** (as **tarefas**) e **arestas** (as **dependências**).
- **Direcionado:** as arestas **têm direção** (A → B: B depende de A).
- **Acíclico:** **não tem ciclo**, ou seja, **sem loops**: não dá para **voltar a um passo anterior**.
- No Airflow, **um DAG = um fluxo de trabalho** com **várias tarefas e suas dependências**.

| Termo | No Airflow |
|---|---|
| **DAG** | O workflow inteiro (tarefas + dependências) |
| **Task** (tarefa) | Uma unidade de trabalho (ex.: rodar um script Python) |
| **Operator** | O **tipo/comando** que a task executa (`PythonOperator`, `BashOperator`...) |

> 💡 **Para fixar:** **D**ireção, **A**cíclico, **G**rafo → **"vai sempre pra frente, nunca dá ré"**.

⚠️ **Pegadinha (prova antiga):** DAG é o **fluxo inteiro**, não **uma tarefa** (isso é task) nem **o banco do histórico** (isso é o metadata DB).

## Operadores e dependências
- Cada **variável** do fluxo é uma **task**, criada com um **operador** (classe importada de `airflow.operators`). Dá para **criar operators próprios**.
- **`python_callable`**: a propriedade que recebe a **função Python** que o `PythonOperator` vai executar.
- A **ordem** é definida por **dependências explícitas**, usando **sobrecarga do operador `>>`** (ou `set_downstream`):

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def extrair(): ...
def transformar(): ...
def carregar(): ...

with DAG("etl_clima", start_date=datetime(2025, 1, 1),
         schedule="0 * * * *", catchup=False) as dag:
    t1 = PythonOperator(task_id="extrair",     python_callable=extrair)
    t2 = PythonOperator(task_id="transformar", python_callable=transformar)
    t3 = PythonOperator(task_id="carregar",    python_callable=carregar)

    t1 >> t2 >> t3          # sequência
```

- **Paralelo:** `[task1, task2] >> task3` → task1 e task2 rodam **em paralelo**, e task3 espera as duas.

| Sintaxe | Significado |
|---|---|
| `a >> b` | b roda **depois** de a (= `a.set_downstream(b)`) |
| `a << b` | a roda depois de b (= `a.set_upstream(b)`) |
| `[a, b] >> c` | a e b em paralelo; c depois das duas |

> 💡 **Para fixar:** a seta `>>` **aponta para quem vem depois**. A ordem **não** é a ordem em que você escreveu as tasks no arquivo.

## Agendamento e gatilhos
- Dá para executar **diariamente, por hora** etc., com expressão **cron** (o site **crontab guru** ajuda a montar).
- Ou por **triggers** (gatilhos): manual, via **API**, ou por evento.
- **Sensors** (lib `sensors`): tasks que **ficam escutando** até uma condição acontecer (ex.: arquivo chegar, mensagem em **tópico do Kafka** disparar o pipeline). São **`async`**, pois só esperam.

## Integração e uso
- Integra com sistemas externos, como **APIs** (dá para **enviar dados/disparar o Airflow via API**).
- Dá para criar **DAG para CI/CD**.
- Os scripts de DAG vão na **pasta designada** (`dags/`); o Airflow lê dali.
- A interface tem **logs** de cada task e visões como o **diagrama de Gantt** (duração e sobreposição das tasks).

> 💡 **Para fixar:** **Python escreve, UI mostra.** Você não desenha o DAG na interface.

## ➕ Complemento para a prova

### Arquitetura do Airflow
| Componente | Função |
|---|---|
| **Scheduler** | Lê os DAGs, decide **o que e quando** rodar e manda para execução |
| **Executor** | Define **como/onde** as tasks rodam (Local, Celery, Kubernetes...) |
| **Workers** | **Executam** as tasks de fato |
| **Webserver (UI)** | Interface para **visualizar** DAGs, execuções e logs |
| **Metadata Database** | **Persiste o estado** das tasks e DAG runs, **variáveis, conexões** e histórico (PostgreSQL/MySQL) |
| **Pasta de DAGs** | Onde ficam os arquivos `.py` dos DAGs |

> 💡 **Para fixar:** o banco de metadados é a **memória** do Airflow. Sem ele, o scheduler não sabe o que já rodou.

⚠️ **Pegadinha (prova antiga):** o metadata DB **não executa** o código dos DAGs (isso é o worker), **não guarda só logs** e **não sincroniza código-fonte**.

### Conceitos que costumam cair
- **DAG Run:** uma **execução** do DAG para uma data. **Task Instance:** uma execução de uma task dentro de um DAG Run.
- **`start_date` + `schedule`:** de quando e de quanto em quanto tempo rodar. **`catchup`**: se `True`, roda os intervalos passados que ficaram para trás (**backfill**).
- **XCom** ("cross-communication"): troca de **pequenos dados** entre tasks (não para datasets grandes).
- **Retries:** a task pode ser configurada para **tentar de novo** automaticamente ao falhar.
- **Estados de task:** queued, running, success, failed, up_for_retry, skipped.

### Cron em 5 campos
`minuto hora dia-do-mês mês dia-da-semana` → `0 * * * *` = de hora em hora; `0 3 * * *` = todo dia às 3h; `*/15 * * * *` = a cada 15 minutos.

### ELT com DBT (caiu na prova antiga)
- **dbt** (data build tool) faz o **T** do **ELT** com **SQL**, **dentro do Data Warehouse**.
- **Vantagem principal do ELT:** **aproveitar o poder de processamento do próprio DW** para transformar (os dados chegam crus e são transformados lá).
- O Airflow muitas vezes **orquestra** o dbt (uma task que roda `dbt run`).

---

# As ideias que sustentam tudo

1. **Flink processa, Kafka transporta, Airflow orquestra.** Stream contínuo = Flink (job com `INSERT INTO`). Batch agendado = Airflow (DAG com `>>`).
2. **Duplicata é inevitável em sistema distribuído.** A resposta é **defesa em camadas**: produtor idempotente → `ROW_NUMBER` com estado limitado (TTL) → **UPSERT** no sink.
3. **Declarativo x imperativo:** SQL/Table API dizem **o quê**; DataStream diz **como**. O mesmo vale para o Airflow: você declara as **dependências**, o scheduler decide a execução.
