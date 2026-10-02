# Big Data: Resumo para estudo

> Como usar: leia o resumo, depois faça os **flashcards** e por último o **quiz**.
> Cada aula tem uma caixa **💡 Para fixar** com um truque de memória.

> **Complementos ➕:** no fim de cada aula há uma seção **"➕ Complemento para a prova"** com conteúdo dos links indicados (AWS, Databricks, Confluent, Google Cloud, DataCamp etc.) que **não apareceu em aula**. Priorize o que veio da aula e use os ➕ para reforçar. Não dá para saber o que o professor vai cobrar: confirme com ele.

---

## Mapa geral (a visão de cima)

```
Aula 1  O que é Big Data, os V's, histórico (Google, Hadoop)
Aula 2  Pipeline: coleta > ingestão > armazenamento > processamento > consumo
Aula 3  ETL, Flink como "passagem", latência no streaming
Aula 4  Data Warehouse > Data Lake > Data Lakehouse, Star Schema
Aula 5  Flink na prática: timestamps, watermarks, connectors, source/sink
Aula 6  ETL x ELT: onde e quando transformar
Aula 7  Medallion (bronze/prata/ouro) e CDC (Change Data Capture)
```

**Sobre o estilo da prova:** as provas antigas do professor (G1/G2 de IA & ML) são de **múltipla escolha com 4 alternativas**: "qual descreve melhor...", "o que é...", "qual NÃO é...", "qual a diferença entre... e...". Cobram **definição** e **diferença entre conceitos**, não conta.

---

# Aula 1: Introdução ao Big Data

## O que é Big Data
- Termo **recente**. São dados **multivariados** e de **elevada dimensão**, geralmente **criados em tempo real**, com **crescimento exponencial**.
- Quanto mais dados são gerados, **maior o esforço** para extrair informação.
- Exige ferramentas **além dos bancos relacionais** e dos sistemas paralelos de bancos de dados (desafio dos data centers).
- Big Data é **muito mais que "um monte de dados"**: é sobre o **valor e o significado** que podem ser extraídos deles.
- *Data Never Sleeps* (Domo): a cada minuto, uma quantidade enorme de dados é gerada. Países maiores costumam ter boa infraestrutura para suportar tantos usuários.

> 💡 **Para fixar:** Big Data = não é o tamanho, é o **valor** que se tira dele.

## Os V's
Doug Laney (2001) propôs **3 V's**. A aula usa **5 V's**.

| V | Ideia | Problema | Solução |
|---|---|---|---|
| **Volume** | Quantidade enorme de dados | Exige muito poder de computação para armazenar e processar | Armazenamento cada vez mais barato e acessível (nuvem). Hadoop é o principal sistema para armazenar/processar |
| **Variedade** | Muitas fontes e tipos (estruturados e não estruturados) | Dificulta armazenar, minerar e analisar | Bancos **não relacionais** (ex.: MongoDB). ML e Deep Learning ajudam a dar sentido aos formatos |
| **Velocidade** | Fluxo maciço e contínuo | Chega mais rápido do que se consegue interpretar | Sistemas automáticos 24h por dia. Pipelines **streaming** (tempo real) e/ou **batch** (lote) |
| **Veracidade** | Dados confiáveis | Dados falsos, incompletos ou duvidosos prejudicam análises | **Verificar antes de armazenar** e cuidar das fontes |
| **Valor** | Dados que geram vantagem | Dado sem uso não vale nada | Gerar vantagem competitiva, melhor serviço ao cliente e destaque no mercado |

- **Os 3 de Doug Laney:** Volume, Velocidade, Variedade. **Os 2 acrescentados:** **Veracidade** e **Valor**.

> 💡 **Para fixar:** Laney = **V**olume, **V**elocidade, **V**ariedade. Depois vieram a **verdade** (Veracidade) e o **valor** (Valor).

## Histórico (milestones dos slides)
- **Legado Google:** GFS, MapReduce, BigTable (os slides listam 2006, 2007 e 2008).
  - **GFS** (Google File System): sistema de arquivos distribuído.
  - **BigTable**: operações PUT/GET/DELETE/SCAN. Evoluiu para o **BigQuery**.
  - **MapReduce**: modelo de processamento distribuído.
- **Hadoop**: implementação **open-source** do conceito de MapReduce.

> 💡 **Para fixar:** o Google inventou (GFS, MapReduce, BigTable); o **Hadoop** foi a versão aberta.

## ➕ Complemento para a prova

### Termos de governança (UFLA)
| Termo | Ideia |
|---|---|
| **Governança de dados** | Execução de autoridade e controle sobre os dados (DMBOK) |
| **Gestão de dados** | Tratar dados como recursos críticos para o sucesso operacional e administrativo |
| **Glossário de negócios** | Garante coerência semântica entre áreas |
| **Dados mestres e de referência** | Informações comuns compartilhadas entre áreas, processos e sistemas |
| **Linhagem de dados** | Origem e etapas de processamento do dado |
| **Qualidade de dados** | Não é só precisão |
| **Data Warehouse / Data Lake** | DW guarda dados de várias fontes; Data Lake guarda em formato nativo |

- O termo *Big Data* foi criado em **1997** (Michael Cox e David Ellsworth), segundo a UFLA.

---

# Aula 2: Pipeline de dados, formatos e ferramentas

## Data Pipeline
Série de etapas de processamento que **prepara os dados para análise**, levando-os de várias fontes até um destino.

```
Coleta > Ingestão > Armazenamento > Processamento > Consumo
```

- A **coleta** parte das fontes. É preciso dizer se são **estruturadas ou não**.
- Decisão central: o dado vai para um **data lake** (uso em **lote/batch**) ou segue como **fluxo (stream)**?
- É recomendável **analisar os dados** e coletar só os **relevantes e "limpos"**.
- Em Big Data há **vários componentes conversando entre si**.

> 💡 **Para fixar:** C-I-A-P-C: **C**oleta, **I**ngestão, **A**rmazenamento, **P**rocessamento, **C**onsumo.

## Quem faz o quê

| Ferramenta | Papel |
|---|---|
| **Apache Spark** | Motor de processamento para **data lake / batch** |
| **Apache Flink** | Motor de processamento para **stream** |
| **Apache Kafka** | **Transporta** os dados até Spark ou Flink |
| **minIO** | Armazenamento compatível com **S3** |

- Geralmente cada um roda em **um servidor separado**, porque pode exigir muito processo e memória.
- **Flink:** motor de processamento, "assim como o Spark". Jobs em **Java** (também existe o **FlinkSQL**, e o **PyFlink** na Aula 5).
- **Source e Sink:** várias **fontes** e um **destino**, como um **funil**.

> 💡 **Para fixar:** Kafka é o **caminhão**, Spark processa o **estoque** (lote), Flink processa a **esteira** (fluxo).

## Tipos de dado

| Tipo | Padrão | Exemplos |
|---|---|---|
| **Estruturado** | Com padrão | Tabelas |
| **Semiestruturado** | Um pouco de padrão | CSV, JSON |
| **Não estruturado** | Sem padrão | E-mails, vídeos, áudios |

- Os **não estruturados** precisam passar por um processo para **gerar metadados**.
- **Data Lake:** armazena dados para serem usados **para diferentes fins em outros momentos**.

## Formatos de arquivo
- **Parquet** (evoluiu para **Delta**) e **Avro** (**binário**).
- **CSV e JSON** não têm padrão rígido.
- Formatos **proprietários** (Excel, SQL Server etc.) amarram você ao fornecedor.

## ➕ Complemento para a prova

### Componentes de um pipeline (AWS)
Quatro elementos: **fontes**, **transformações**, **dependências** (restrições que ordenam o processamento) e **destinos** (data warehouse ou data lake). Benefícios: qualidade (limpeza e padronização), eficiência (automação) e integração de várias fontes. ETL é **um tipo** de pipeline; existem outros, como ELT.

### Parquet x Avro x ORC
| Aspecto | Parquet | Avro | ORC |
|---|---|---|---|
| Orientação | **Colunar** | **Linha** | **Colunar** |
| Escrita | Mais lenta | **Rápida** | Eficiente |
| Compressão | Alta (snappy) | Moderada | Excelente |
| Schema evolution | Limitada | **Forte** | Limitada |
| Uso típico | Análise e data lakes (S3 + Athena) | Tempo real, **Kafka** | Hadoop/Hive, batch |

- **Parquet (Snowflake):** formato binário colunar. Organiza em **grupos de linhas, blocos de colunas, páginas e metadados**. Comprime por coluna (dicionário, bit-packing). Compatível com Spark, Hive e Snowflake.

> 💡 **Para fixar:** **Par**quet = **par**a **an**álise (colunar). **Avro** = **a**vança no **Kafka** (linha, evolui o esquema).

---

# Aula 3: ETL, streaming e latência

## ETL
**E**xtract, **T**ransform, **L**oad: extrai das fontes, transforma (limpa, junta, modela) e carrega o dado já pronto no destino.

## Pontos da aula
- Quando os dados são **muito pesados**, dá para **pré-prepará-los em um banco específico**, já com **joins e filtros**.
- O **Apache Flink é só uma passagem** dos dados: **não possui persistência**.
- No **streaming**, a **latência precisa ser baixa**.
- **Trafegar dados na rede gera latência alta.**

> 💡 **Para fixar:** Flink é um **cano**, não um **balde**: o dado passa, não fica.

## ➕ Complemento para a prova

### Batch x Stream (DataCamp)
| Aspecto | Batch | Stream |
|---|---|---|
| Quando processa | Em **intervalos agendados** | **Continuamente**, em tempo real |
| Latência | **Alta** | **Baixa** |
| Complexidade e custo | Menor | **Maior** |
| Infraestrutura | Mais simples | Especializada |
| Casos de uso | DW, relatórios periódicos, histórico, migrações | Fraude, monitoramento, IoT |
| Ferramentas | Airflow, BigQuery, Redshift, Snowflake | Kafka, Flink, Kinesis, Dataflow |

### Apache Flink (AWS)
- Mecanismo **distribuído**, **open source**, para processamento **com estado** de dados **ilimitados (fluxos)** e **limitados (lotes)**.
- Recursos: **estado** distribuído, semântica de **tempo de evento**, **checkpoints** e **savepoints** (tolerância a falhas), APIs em níveis (SQL, Table, DataStream, ProcessFunction).
- Usos: fraude em tempo real, clickstream, ETL contínuo, personalização.
- Atenção: "sem persistência" (aula) fala do **destino dos dados**; o Flink mantém **estado interno** para operações como janelas e agregações.

### RabbitMQ x Kafka (AWS)
| Aspecto | RabbitMQ | Kafka |
|---|---|---|
| Natureza | **Agente de mensagens** ("agência postal") | **Plataforma de eventos** ("biblioteca") |
| Entrega | **Push** (agente entrega) | **Pull** (consumidor busca) |
| Após o consumo | **Exclui** a mensagem | **Retém** (permite reprocessar) |
| Throughput | Milhares/s | **Milhões/s** |
| Prioridade | Filas **prioritárias** | Todas iguais |
| Ideal para | Roteamento complexo, MQTT/STOMP, entrega garantida | Tempo real, big data, replay |

> 💡 **Para fixar:** RabbitMQ **empurra** e **apaga**. Kafka **guarda** e você **puxa**.

---

# Aula 4: Data Warehouse, Data Lake e Lakehouse

## Linha do tempo
```
Data Warehouse  >  Data Lake  >  Data Lakehouse
```

| Conceito | Ideia |
|---|---|
| **Data Warehouse** | Dados **agregados**, relacionais, prontos para consulta. Usa **Star Schema** |
| **Data Lake** | Guarda **todos os formatos**, de várias origens. É um **object storage** (tipo S3), **sem hierarquia de pastas** |
| **Data Lakehouse** | Lake + **camada de metadados e governança** (origem, qualidade, quem atualizou etc.) |

- O Data Lake só virou possível porque o **armazenamento ficou mais barato**.
- **Sem hierarquia de pastas** para não precisar de **recursividade** nas buscas.

> 💡 **Para fixar:** Lake = **guardar tudo**. Lakehouse = guardar tudo **com etiqueta e regra**.

## Star Schema
- Usado em **data warehouse**: agrega dados e manda para outro banco ou apenas uma tabela (**tudo relacional**).
- **Evita vários joins**, pois os dados já estão prontos para busca.

## Outros pontos
- **MongoDB não tem join.**
- **ETL** na extração com Python: `numpy` e `pandas`.
- **Apache Airflow** (citado nas anotações).

## ➕ Complemento para a prova

### Lakehouse (Databricks e Google Cloud)
- Arquitetura **aberta** que junta a flexibilidade e o baixo custo do **lake** com o gerenciamento e as **transações ACID** do **warehouse**.
- Recursos: **ACID**, **aplicação de esquema**, governança unificada, **SQL direto** para BI, menos duplicação.
- A **camada de metadados** fica sobre **formatos abertos (Parquet)** e acompanha as versões da tabela. **Delta Lake** implementa isso.
- Antes: arquitetura de **duas camadas** (ETL para o lake e outro ETL para o warehouse), com duplicação, custo e dados desatualizados.

| | Data Lake | Data Warehouse | Data Lakehouse |
|---|---|---|---|
| Dados | Brutos, não estruturados | Estruturados, processados | Ambos |
| Esquema | **Schema-on-read** | **Schema-on-write** | Ambos |
| Governança | Limitada | Forte | Forte |
| Custo | Baixo | Alto | Moderado |
| Uso | Exploração, ML | Analytics, BI | Tudo em um |

> 💡 **Para fixar:** *on-read* = decide o formato **quando lê** (lake). *on-write* = decide **quando grava** (warehouse).

- **Airflow:** orquestrador de workflows (agenda e encadeia tarefas, típico de batch).

---

# Aula 5: Flink na prática (tempo, watermarks e connectors)

## Tempo
- **ISO 8601**: padrão de **timestamp em texto**, **com UTC ou sem**.
- **Epoch UNIX**: timestamp como **inteiro**.
- **Watermarks** do Flink: tipo de **registro inserido nos dados para marcar a passagem do tempo**.

> 💡 **Para fixar:** ISO 8601 = **texto** ("2026-04-24T10:00:00Z"). Epoch = **número**.

## Dados sintéticos
- **Faker**: originalmente uma lib de **Java**, baseada em repositórios de dados, com diversos **providers**. No Flink: **flink-faker**.
- **Datagen**: outra opção para gerar dados.

## Connectors, source e sink
- **Tudo que é externo** usado no Flink se chama **connector**.
- Pipeline do exemplo: **source faker** e **sink Kafka**.
- A cláusula **`WITH`** do SQL **varia conforme o source**. Cria-se uma **tabela temporária** e depois a tabela de source é inserida na sink.
- **`blackhole`**: sink para quando não há destino. **Gera os dados e não salva em lugar algum.**
- **`sql-client.sh`**: terminal SQL do Flink.
- O modelo de streaming **roda sem parar**.
- **PyFlink**: Flink com Python. **PostgreSQL** é **objeto-relacional**.

```sql
CREATE TABLE origem ( ... ) WITH ( 'connector' = 'faker', ... );
CREATE TABLE destino ( ... ) WITH ( 'connector' = 'kafka', ... );
INSERT INTO destino SELECT * FROM origem;
```

> 💡 **Para fixar:** `WITH` é a **tomada**: cada connector tem um plugue diferente. `blackhole` é a **tomada falsa**.

## ➕ Complemento para a prova

### Timestamps no Flink SQL (Confluent)
| Tipo / função | O que faz |
|---|---|
| `TIMESTAMP` | Data-hora **sem fuso** (como `LocalDateTime` do Java) |
| `TIMESTAMP_LTZ` | Guarda em **UTC** e mostra no **fuso local** (como `Instant`) |
| `TO_TIMESTAMP_LTZ(epoch, precisão)` | Converte **epoch** em `TIMESTAMP_LTZ` (precisão 0 = segundos, 3 = ms) |
| `UNIX_TIMESTAMP()` / `FROM_UNIXTIME()` | String para epoch / epoch para string |

### Watermarks (Confluent)
- **Event time** (tempo dentro do dado) é o recomendado. **Processing time** (relógio da máquina) gera **não determinismo**.
- Watermarks são necessárias para operações com estado e tempo: **janelas**, **joins temporais**, **top-N**, **MATCH_RECOGNIZE**. **Não** são necessárias em `SELECT/WHERE` simples.
- **Time attribute** = coluna de timestamp com watermark. **Só uma por tabela**.

### Tipos e serialização
- `BYTES` = `VARBINARY(2147483647)`: sequência de bytes de tamanho variável.
- Avro: tipo **nullable** vira **`union(tipo, null)`**. `BIGINT` vira `long`, `VARCHAR/STRING` vira `string`, `ROW` vira `record`. Enum é tratado como `STRING`.

### RabbitMQ com PyFlink (repositório do professor)
- Duas filas: **`fila01_source`** (entrada) e **`fila01_sink`** (saída), criadas pelo painel do RabbitMQ (porta **15672**). Dashboard do Flink na porta **8081**.
- Job executado dentro do container `flink-jobmanager` com `flink run -py rabbit.py`.

---

# Aula 6: ETL x ELT

## Os dois fluxos
| | **ETL** | **ELT** |
|---|---|---|
| Ordem | **E**xtract, **T**ransform, **L**oad | **E**xtract, **L**oad, **T**ransform |
| Onde transforma | **Servidor intermediário** dedicado, **antes** da carga | **No próprio destino** (data lake/warehouse cloud), **depois** da carga |
| Dado no destino | Já **modelado e pronto** | **Bruto (raw)** |

> 💡 **Para fixar:** a letra **L** (Load) vem **antes** do **T** no **ELT**.

## Comparação direta
| ETL | ELT |
|---|---|
| Melhor para **volumes menores** e dados **estruturados** | Melhor para **grandes volumes** e dados **semi/não estruturados** |
| Transformação **centralizada**, mais fácil de **auditar** | **Escala horizontalmente** com o warehouse/lake cloud |
| **Maior latência** até o dado ficar disponível | **Menor latência** para disponibilizar o dado bruto |
| Custo em **servidores de transformação dedicados** | Custo **elástico**, pago sob demanda |

## Trade-offs
- **Governança:** ETL valida e limpa **antes** de carregar (menos risco de expor dado sensível). ELT exige **controle de acesso robusto** no destino, pois o dado bruto fica lá.
- **Flexibilidade:** ELT permite **várias transformações** a partir do mesmo dado bruto, **sem re-extrair**.
- **Custo:** ELT gasta mais em **armazenamento** (dado bruto); ETL gasta mais em **poder de transformação dedicado**.

> 💡 **Para fixar:** ETL = **lavou antes de guardar**. ELT = **guardou e lava quando precisar**.

## Quando usar
| ETL | ELT |
|---|---|
| **Legados** (ERP, CRM on-premise) | **Streaming** e alto volume (logs, IoT, cliques) |
| **Regulatório**: dado mascarado/validado antes de armazenar | **Data lakes e lakehouses** (ex.: Delta Lake) |
| **Batch tradicional**, volume previsível | **Cloud-native**, warehouses elásticos |

## Arquitetura de um pipeline ELT moderno
```
[Fontes: APIs, DBs, eventos]
        | Extract
        v
[Zona RAW no Data Lake]  <- Load (bruto)
        | Transform (SQL/Spark no próprio warehouse)
        v
[Zona CURATED / Data Warehouse]
        v
[Dashboards, ML, Relatórios]
```
- Ferramentas: **Fivetran/Airbyte** (Extract + Load) com **dbt** (Transform) sobre Snowflake, BigQuery ou Databricks.
- Em arquiteturas modernas (lakes/lakehouses), o **ELT tende a dominar** a ingestão em larga escala.

## ➕ Complemento para a prova

### ETL em detalhe (AWS)
- **Extract:** copia para uma **área de staging**. Pode ser por notificação, **incremental** ou **completa**.
- **Transform:** básico (limpeza, deduplicação, padronização) e avançado (derivar valores, joins, dividir campos, resumo, **criptografia**).
- **Load:** **full load** (tudo) ou **incremental** (só o que mudou).

### ETL x ELT (AWS)
| | ETL | ELT |
|---|---|---|
| Compatibilidade | Dados estruturados | Estruturados, semi e não estruturados |
| Velocidade | Mais lenta | Mais rápida |
| Custo | Configuração demorada e cara | Mais econômico |
| Segurança | Aplicações personalizadas | Recursos do próprio banco |

> A AWS indica ETL para **bancos legados**, **experimentos** e **IoT na borda**. Isso complementa os usos vistos em aula.

---

# Aula 7: Arquitetura Medallion e CDC

## Arquitetura Medallion (data lakes)
- Três camadas: **Bronze (raw data)**, **Prata** e **Ouro**.
- A bronze pode ser salva em um **S3 open source** (as notas citam "Alarik"; veja o aviso ao final).
- Formato: **Parquet (snappy)**.

> 💡 **Para fixar:** bronze = **minério** (cru). Prata = **barra** (refinada). Ouro = **joia** (pronta).

## CDC: Change Data Capture
- **Interceptar dados na fonte** e **replicar**. É um **design pattern** (arquitetura **conceitual**).
- **Captura alterações do banco em tempo real**, com **baixa latência**.
- Foca em **mudanças incrementais** em vez de reprocessar o conjunto todo, monitorando o BD sempre.
- **Não olha o passado:** dados que existiam **antes** da implantação do CDC não são capturados.
- É mais eficiente ler os **logs** do que fazer consultas SQL. É assim que o CDC replica para outros lugares, como o **Kafka**.
- No banco, muita coisa fica em memória e só é **persistida no commit**.

## As 3 formas
| Forma | Como funciona | Custo |
|---|---|---|
| **Log** (a mais popular, melhor para Big Data) | Inspeciona os **logs de transação** (logs de **DML**) e repassa as alterações | **Baixo**, sem sobrecarregar a origem |
| **Trigger** | "Igual uma função de banco": ao ocorrer a alteração, **grava em outro lugar** | **Maior**, sobrecarrega o sistema |
| **Timestamp** | Campo de **auditoria**. Dispara consultas comparando com a última, para ver se a data mudou | Sobrecarrega, pois **consulta o banco o tempo todo** |

> 💡 **Para fixar:** **L**og = **L**eve. Trigger e timestamp **pesam** no banco.

## Debezium
- Funciona como um **plugin do banco** (SQL e NoSQL) que traz o log de forma **mais estruturada**. Conversa com o CDC de cada banco.
- Normalmente usado com o **Kafka Connect**, que faz a ligação **banco ↔ Kafka**.
- Cria **um tópico no Kafka** com o esquema e o nome da tabela no nome.
- Envia em **JSON**. O campo **`op`** traz o tipo da ação (`insert`, `update`, `delete`...).
- É de **baixo nível**: atua na camada do banco, não do usuário.

## WAL (Write Ahead Logging) no Postgres
- Padrão de projeto: as alterações só vão para o disco **depois** de registradas no **log de transações**.
- **Grava o que vai acontecer antes de efetivar.** Grava só registros **incrementais**.
- **Precisa ser habilitado** no banco, usando a **replicação lógica** (o "filtro" do log).

> 💡 **Para fixar:** WAL = **anota no caderno antes de fazer**. O Debezium lê o caderno.

## Fechamento: as ideias que sustentam tudo

1. **Big Data é sobre valor**, e os 5 V's descrevem o desafio (Volume, Velocidade, Variedade, Veracidade, Valor).
2. **Pipeline:** coleta, ingestão, armazenamento, processamento e consumo. A escolha entre **batch e stream** guia as ferramentas (Spark, Flink, Kafka).
3. **Onde e quando transformar** (ETL x ELT) e **como capturar mudanças** (CDC por log) definem uma arquitetura moderna de dados (lake, lakehouse, medallion).

## ➕ Complemento para a prova

### Medallion: o que tem em cada camada
| Camada | Conteúdo típico |
|---|---|
| **Bronze** | Dado **bruto**, como veio da fonte |
| **Prata** | Dado **limpo e padronizado** (deduplicado, tipado) |
| **Ouro** | Dado **agregado**, pronto para negócio, BI e ML |

### CDC: métodos e ferramentas (Google Cloud, DataCamp)
- O CDC acompanha **INSERT, UPDATE e DELETE**.
- Métodos: **log** (binlog do MySQL, WAL do PostgreSQL), **trigger** (grava em tabela auxiliar), **timestamp/consulta** (polling, mais simples e com maior latência, depende de relógios sincronizados).
- Usos: replicação, **data warehousing em tempo real**, sincronização de **microsserviços**, **auditoria e conformidade**.
- Ferramentas: **Debezium**, **AWS DMS**, **Google Datastream**, Kafka como espinha dorsal.
