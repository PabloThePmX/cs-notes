# Big Data: Quiz de múltipla escolha (Prova 2)

> 38 questões, 4 alternativas cada, no estilo da prova antiga do professor. As 12 questões da **prova antiga** estão aqui com o mesmo enunciado (marcadas no gabarito; a prova real tinha 5 alternativas, aqui ficaram 4). Responda no papel e só depois abra o **gabarito**. Questões com ➕ vêm de conteúdo complementar, não das aulas.
> As alternativas erradas foram feitas para parecerem tão boas quanto a certa: use o raciocínio, não o tamanho do texto.

**Placar:** ___ / 38

---

## Aula 8: PyFlink (DataStream, Table API e FlinkSQL)

**1. No PyFlink, qual é a principal diferença conceitual entre a 'Table API' e a 'DataStream API'?**

- A) A Table API abstrai detalhes internos e usa uma interface similar a SQL para transformações estruturadas.
- B) A Table API é imperativa, enquanto a DataStream API é puramente declarativa e parecida com SQL.
- C) A DataStream API não oferece suporte a processamento orientado a tempo (event-time) nem a estado do job.
- D) A Table API exige conhecimento profundo de Java, enquanto a DataStream API usa apenas Python.

<details><summary>Gabarito</summary>

**A.** *(Prova antiga, Q2.)* A Table API é **declarativa** e parecida com SQL. A alternativa B inverte os conceitos: a **DataStream** é que é imperativa. A DataStream suporta event-time, e as duas APIs existem em Python.
</details>

**2. Qual comando SQL é comumente utilizado no PyFlink para definir um processamento contínuo da fonte para o destino na Table API?**

- A) INSERT INTO sink_table SELECT * FROM source_table
- B) SELECT * FROM source_table WHERE val IS NOT NULL
- C) CREATE VIEW source_view AS SELECT * FROM source_table
- D) UPDATE sink_table SET val = 1 WHERE id IS NOT NULL

<details><summary>Gabarito</summary>

**A.** *(Prova antiga, Q4.)* O **`INSERT INTO ... SELECT ... FROM`** liga a source ao sink e cria o job contínuo. Um `SELECT` só consulta, e a `VIEW` só dá nome a uma consulta, sem gravar em lugar nenhum.
</details>

**3. Assinale a alternativa verdadeira sobre tabelas temporárias no Flink SQL:**

- A) São usadas para persistência de longo prazo dos dados do pipeline.
- B) São criadas diretamente no Data Lake, em formato aberto como Parquet.
- C) Podem ser compartilhadas entre diferentes aplicações pelo catálogo.
- D) São descartadas quando a sessão ou o job que as criou é encerrado.

<details><summary>Gabarito</summary>

**D.** *(Prova antiga, Q8.)* ➕ Tabela temporária vive **só na sessão**. Persistência e compartilhamento entre aplicações são características de tabelas **permanentes** registradas em um catálogo.
</details>

**4. Sobre a definição de source no Apache Flink, é correto afirmar que:**

- A) É o componente responsável por enviar dados para fora do pipeline.
- B) Uma source representa um destino final dos dados já processados.
- C) Uma source fornece os dados iniciais ao job de processamento.
- D) A source no Flink deve ser configurada usando apenas a linguagem Java.

<details><summary>Gabarito</summary>

**C.** *(Prova antiga, Q9.)* Source = **entrada**. As alternativas A e B descrevem o **sink**. E dá para configurar sources em Python (PyFlink) e SQL.
</details>

**5. Em relação ao componente sink no Apache Flink, marque a correta:**

- A) Os sinks são os responsáveis por capturar os dados de entrada do job.
- B) Um sink representa o ponto de saída dos dados após o processamento.
- C) Um sink é usado apenas para debug, imprimindo os dados na tela.
- D) Os sinks não podem se conectar com sistemas externos ao Flink.

<details><summary>Gabarito</summary>

**B.** *(Prova antiga, Q10.)* Sink = **saída**. Capturar a entrada é papel da **source**. O `print` é um sink de teste, mas existem sinks para Kafka, MongoDB, bancos etc.
</details>

**6. Sobre Flink e Kafka, avalie: (I) O Flink possui conector nativo para consumir tópicos Kafka. (II) O Flink pode atuar como produtor e consumidor de dados no Kafka. (III) Ao integrar com Kafka, o Flink perde a capacidade de escalabilidade. (IV) É possível fazer transformações em tempo real nos dados do Kafka usando Flink. A sequência correta é:**

- A) V - F - V - F
- B) V - V - F - V
- C) F - V - F - V
- D) V - V - F - F

<details><summary>Gabarito</summary>

**B.** *(Prova antiga, Q12.)* Só a III é falsa: o Flink escala junto com as **partições** do tópico. A alternativa D erra a IV, que é justamente o uso principal (transformar em tempo real).
</details>

**7. Por que, no PyFlink, é preciso declarar as bibliotecas (JARs) do Java dentro do script Python?**

- A) Porque o Flink é escrito em Java e o Python é só uma interface para a execução na JVM.
- B) Porque o Python precisa compilar o script em JAR antes de enviá-lo ao dashboard do Flink.
- C) Porque os connectors em Python são mais lentos e o JAR serve apenas como cache de dados.
- D) Porque o Kafka exige que todo consumidor seja escrito em Java para ler os seus tópicos.

<details><summary>Gabarito</summary>

**A.** O PyFlink **chama o Flink em Java**. Connectors como o **RMQ** chamam o código Java, então o **JAR precisa existir**. O script não é compilado em JAR: ele vai pela CLI com `-py`.
</details>

**8. Como um job escrito em Python é colocado no ar no Flink, segundo a aula?**

- A) Pela CLI, com o binário do Flink: /opt/flink/bin/flink run -py script.py
- B) Pelo dashboard web do Flink, enviando o arquivo .py na tela de submit.
- C) Pelo Kafka Connect, registrando o script como um connector de sink.
- D) Pelo Airflow, que é o único jeito de agendar um job PyFlink no cluster.

<details><summary>Gabarito</summary>

**A.** O **dashboard só aceita JARs**, então o Python vai pela **CLI** com `-py`. A alternativa B é a armadilha: o dashboard existe, mas não aceita Python.
</details>

**9. O que caracteriza o connector DataGen usado em aula?**

- A) É um sink que grava os dados gerados pelo job em um arquivo no disco local.
- B) É uma source que lê dados reais de uma API externa, como a Open-Meteo.
- C) É uma biblioteca Python que gera nomes e e-mails realistas para teste.
- D) É uma source que gera dados aleatórios em memória, sem os filtros do Faker.

<details><summary>Gabarito</summary>

**D.** O **DataGen** é uma **source de teste** que gera dados aleatórios (ex.: `rows-per-second`). Gerar nomes e e-mails realistas é o que o **Faker** faz.
</details>

**10. No exemplo do professor, rodando o Flink no Docker, onde se vê a saída do sink print?**

- A) No terminal onde o script Python foi executado com o comando flink run.
- B) Na aba de SQL do dashboard, que exibe as linhas inseridas no sink.
- C) Nos logs do container do JobManager, que coordena o job no cluster.
- D) Nos logs do container do TaskManager, por exemplo com docker logs.

<details><summary>Gabarito</summary>

**D.** Quem **executa** as tarefas é o **TaskManager**, então o `print` sai nos logs dele (`docker logs flink-taskmanager`). O **JobManager** só coordena.
</details>

**11. Qual o fluxo mais comum no PyFlink, segundo a aula?**

- A) Escrever o job inteiro em DataStream, pois a Table API não roda em Python.
- B) Pegar um DataStream, converter para Table API e então trabalhar com SQL.
- C) Pegar uma Table, converter para DataStream e então trabalhar com Java.
- D) Usar só FlinkSQL, pois as tabelas não podem ser convertidas em streams.

<details><summary>Gabarito</summary>

**B.** A aula destacou **DataStream → Table API**. A conversão existe nos dois sentidos (`from_data_stream` / `to_data_stream`), e a Table API funciona em Python.
</details>

**12. No exemplo com DataGen, o que faz a chamada execute_insert("print_sink")?**

- A) Cria a tabela print_sink no catálogo, sem iniciar nenhum processamento.
- B) Lê os dados do sink print_sink e os devolve como um DataStream novo.
- C) Insere o resultado da consulta no sink e dispara a execução do job.
- D) Valida o schema da source e para o job se alguma coluna estiver nula.

<details><summary>Gabarito</summary>

**C.** `execute_insert` é o equivalente ao `INSERT INTO` do SQL: **grava no sink e dispara o job**. Criar a tabela foi feito antes, com `create_table`.
</details>

**13. Na atividade em aula com a Open-Meteo, qual era a ordem do pipeline?**

- A) API (requests) → Kafka → FlinkSQL consome do Kafka → MongoDB
- B) API (requests) → MongoDB → FlinkSQL consome do Mongo → Kafka
- C) Kafka → API (requests) → FlinkSQL grava na API → MongoDB
- D) API (requests) → FlinkSQL → MongoDB → Kafka consome do Mongo

<details><summary>Gabarito</summary>

**A.** Obter da API, **gravar no Kafka**, **consumir do Kafka com FlinkSQL** e **gravar no MongoDB**. O Kafka fica no meio como buffer.
</details>

---

## Aula 9: Deduplicação de dados em streaming

**14. No contexto do Apache Kafka, qual estratégia é a mais simples para evitar duplicatas causadas exclusivamente por tentativas de reenvio (retries) do produtor?**

- A) Implementar um cache Redis no lado do consumidor da mensagem.
- B) Habilitar o 'Idempotent Producer' nas configurações do Kafka.
- C) Desativar completamente as tentativas de reenvio do produtor.
- D) Aumentar o tempo de retenção das mensagens dentro do broker.

<details><summary>Gabarito</summary>

**B.** *(Prova antiga, Q6.)* `enable.idempotence=true` dá **número de sequência** a cada mensagem e o broker descarta a repetida. Desativar retries evita a duplicata, mas **troca duplicata por perda**.
</details>

**15. Assinale a alternativa verdadeira sobre o funcionamento dos consumidores (consumers) no Apache Kafka:**

- A) Um consumidor só pode ler cada mensagem uma única vez por tópico, sem reler.
- B) Consumidores leem mensagens de tópicos, respeitando a ordem por partição.
- C) O Kafka não permite múltiplos consumidores lendo o mesmo tópico.
- D) Consumidores precisam estar no mesmo servidor físico do produtor.

<details><summary>Gabarito</summary>

**B.** *(Prova antiga, Q11.)* ➕ A ordem é garantida **por partição**. O consumidor pode reler (controla o **offset**), e vários consumidores/grupos podem ler o mesmo tópico.
</details>

**16. Segundo o material, por que duplicatas aparecem em pipelines de streaming?**

- A) Porque os pipelines priorizam precisão em vez de confiabilidade na entrega.
- B) Porque o Kafka grava cada mensagem duas vezes para garantir a replicação.
- C) Porque sistemas distribuídos priorizam confiabilidade em vez de precisão.
- D) Porque são um bug do pipeline, causado por erro de código no consumidor.

<details><summary>Gabarito</summary>

**C.** Duplicata **não é bug**, é **consequência do projeto**: na dúvida, o sistema reenvia para não perder. A alternativa A é o inverso.
</details>

**17. Qual das opções NÃO é uma fonte de duplicatas citada no material?**

- A) Entrega at-least-once com confirmação (ACK) perdida.
- B) Uso de State TTL para expirar o estado de deduplicação.
- C) Sobreposição entre snapshot e stream de mudanças no CDC.
- D) Reinício do pipeline a partir do último checkpoint salvo.

<details><summary>Gabarito</summary>

**B.** As 4 fontes são at-least-once, retentativas de produtor, sobreposição do CDC e reinícios com checkpoint. O **State TTL** é uma **alavanca de gerenciamento de estado** (pode deixar passar duplicata tardia, mas não a cria).
</details>

**18. Como a entrega at-least-once do Kafka pode gerar uma mensagem duplicada?**

- A) O broker não envia o ACK ao produtor e por isso descarta a mensagem antes de gravá-la.
- B) O consumidor confirma o offset antes de processar e a mensagem se perde.
- C) O produtor envia sem esperar ACK e o broker grava em duas partições.
- D) O ACK do broker se perde, o produtor reenvia e a mensagem já estava gravada.

<details><summary>Gabarito</summary>

**D.** Sem ACK, o produtor **tenta de novo**, mas o broker já tinha persistido. A alternativa B descreve **perda** (at-most-once), não duplicata.
</details>

**19. Qual o principal limite da semântica exactly-once (Kafka/Flink) para deduplicação?**

- A) Só funciona em batch e não pode ser usada em pipelines de streaming.
- B) Elimina todas as duplicatas, mas aumenta o estado sem nenhum limite.
- C) Exige desativar os checkpoints do Flink para não reprocessar dados.
- D) Só cobre a fronteira que controla e não impede duplicatas da origem.

<details><summary>Gabarito</summary>

**D.** Exactly-once não resolve **webhook repetido** nem **sobreposição do CDC**: essas duplicatas já nascem antes. Por isso se usa defesa em camadas.
</details>

**20. Na deduplicação com Flink SQL, qual consulta mantém apenas o registro MAIS RECENTE por id?**

- A) ROW_NUMBER() OVER (PARTITION BY id ORDER BY updated_at DESC) e WHERE row_num = 1
- B) ROW_NUMBER() OVER (PARTITION BY id ORDER BY updated_at ASC) e WHERE row_num = 1
- C) ROW_NUMBER() OVER (PARTITION BY updated_at ORDER BY id DESC) e WHERE row_num = 1
- D) ROW_NUMBER() OVER (PARTITION BY id ORDER BY updated_at DESC) e WHERE row_num > 1

<details><summary>Gabarito</summary>

**A.** Particiona pela **chave** (id), ordena por tempo **DESC** e fica com o **1º**. Com **ASC** (alternativa B) fica o **primeiro** registro (first-write-wins).
</details>

**21. O que faz a função PROCTIME() no Flink SQL?**

- A) Retorna o tempo do evento, ou seja, o horário em que o dado foi gerado na origem.
- B) Retorna o watermark atual da source, ou seja, o limite de atraso aceito no job.
- C) Retorna o tempo de processamento, ou seja, o horário do cluster que executou.
- D) Retorna o tempo de vida do estado, ou seja, o TTL configurado para cada chave.

<details><summary>Gabarito</summary>

**C.** `PROCTIME()` = **processing time** (relógio da máquina). Tempo do evento é **event-time**, e o TTL é configurado em `table.exec.state.ttl`.
</details>

**22. Por que os sinks idempotentes (UPSERT) são chamados de "última linha de defesa"?**

- A) Porque impedem que a duplicata seja produzida pelo produtor no início do pipeline.
- B) Porque substituem o checkpoint do Flink, evitando o reprocessamento após falhas.
- C) Porque descartam toda mensagem repetida antes de chegar ao processador de stream.
- D) Porque, se uma duplicata escapar das camadas anteriores, ela só atualiza a linha.

<details><summary>Gabarito</summary>

**D.** O UPSERT fica **no destino**: se a chave existe, faz **UPDATE** em vez de INSERT. Impedir na origem é papel do **produtor idempotente**.
</details>

**23. Qual a desvantagem da deduplicação com janela de tempo (ex.: últimos 10 minutos)?**

- A) Duplicatas que chegam depois da janela passam como se fossem registros únicos.
- B) O estado cresce sem nenhum limite, pois todas as chaves já vistas ficam guardadas.
- C) Ela só funciona com tempo de evento e não aceita o tempo de processamento.
- D) Ela exige que o sink faça UPSERT, senão nenhuma duplicata é removida.

<details><summary>Gabarito</summary>

**A.** A janela **limita o estado**, mas perde **duplicatas tardias**. Estado que cresce sem limite é a dedup **ilimitada** (com estado sem TTL).
</details>

**24. Para que serve isolation.level=read_committed em um consumidor Kafka?**

- A) Para que o produtor descarte mensagens com número de sequência repetido.
- B) Para que o consumidor confirme o offset antes de processar cada mensagem.
- C) Para que o consumidor só leia mensagens de transações já confirmadas.
- D) Para que o broker grave cada mensagem só depois de todas as réplicas.

<details><summary>Gabarito</summary>

**C.** Com **escritas transacionais**, fecha o **exactly-once** dentro do Kafka (o "I" do ACID). A alternativa A é o **produtor idempotente** e a D é `acks=all`.
</details>

**25. Em qual cenário a entrega at-most-once costuma ser aceitável?**

- A) Em pagamentos, onde cada transação precisa ser contada uma única vez.
- B) Em CDC de bancos, onde cada alteração precisa chegar ao data lake.
- C) Em telemetria de sensores, onde perder uma leitura isolada não é grave.
- D) Em pedidos de e-commerce, onde nenhum pedido pode ser descartado.

<details><summary>Gabarito</summary>

**C.** At-most-once = **0 ou 1 vez**: não duplica, mas **pode perder**. Serve para **telemetria/IoT**. Nos outros casos, perder é inaceitável.
</details>

**26. O que significa dizer que uma operação é idempotente?**

- A) Executá-la mais de uma vez produz o mesmo resultado que executá-la uma vez.
- B) Executá-la exige uma transação, para que ocorra tudo ou nada no banco de destino.
- C) Executá-la garante que os eventos fiquem ordenados sem relógio físico.
- D) Executá-la só é permitido uma vez, e a segunda chamada gera um erro.

<details><summary>Gabarito</summary>

**A.** Idempotência = repetir **não muda o resultado** (ex.: UPSERT). "Tudo ou nada" é **transação/atomicidade**, e ordenar sem relógio físico é o **Lamport clock**.
</details>

---

## Aula 10: Apache Airflow e orquestração

**27. Na arquitetura do Apache Airflow, qual é a função primordial do banco de dados de metadados (Metadata Database)?**

- A) Armazenar exclusivamente os logs de execução de todas as tarefas.
- B) Persistir o estado de tarefas, DAGs, variáveis e conexões do ambiente.
- C) Executar o código Python contido nos arquivos DAG de forma isolada.
- D) Sincronizar os arquivos de código-fonte entre Workers e o Scheduler.

<details><summary>Gabarito</summary>

**B.** *(Prova antiga, Q1.)* ➕ O metadata DB é a **memória** do Airflow (estado, variáveis, conexões, histórico). Executar código é papel dos **workers**.
</details>

**28. No Apache Airflow, o que representa um DAG (Directed Acyclic Graph)?**

- A) Uma unidade individual de trabalho, como rodar um único script Python agendado.
- B) O banco de dados que armazena o histórico de execuções das tarefas do ambiente.
- C) Um componente opcional que executa tarefas em loops de eventos assíncronos.
- D) A representação de um fluxo de trabalho, contendo tarefas e suas dependências.

<details><summary>Gabarito</summary>

**D.** *(Prova antiga, Q3.)* DAG = **workflow inteiro**. Uma unidade de trabalho é uma **task**, e o histórico fica no **metadata DB**. E DAG não tem loop (é acíclico).
</details>

**29. Qual é a principal vantagem de utilizar o conceito de ELT (Extract, Load, Transform) com ferramentas como o DBT?**

- A) Realizar a limpeza dos dados antes que eles cheguem ao Data Warehouse.
- B) Reduzir o custo de armazenamento, pois apenas dados transformados são salvos.
- C) Aproveitar o poder de processamento do próprio Data Warehouse para transformar.
- D) Eliminar a necessidade de usar SQL, substituindo-o por linguagens como o Java.

<details><summary>Gabarito</summary>

**C.** *(Prova antiga, Q5; revisão da Aula 6.)* No ELT os dados chegam crus e são transformados **dentro do DW**. Limpar antes de carregar é o **ETL** (alternativa A). O dbt transforma **com SQL**.
</details>

**30. No Apache Airflow, o que define a ordem de execução das tarefas em um fluxo de trabalho?**

- A) A ordem em que as tarefas foram escritas de cima para baixo no script Python.
- B) A ordem alfabética dos nomes (task_id) das tarefas definidas no arquivo Python do DAG.
- C) As dependências declaradas explicitamente com operadores como >> ou set_downstream.
- D) A prioridade definida pelo administrador no portal do Webserver do Airflow.

<details><summary>Gabarito</summary>

**C.** *(Prova antiga, Q7.)* A ordem vem das **dependências explícitas** (`t1 >> t2`). A ordem de escrita no arquivo (alternativa A) **não** define nada.
</details>

**31. Em um DAG do Airflow, o que significa a linha [task1, task2] >> task3?**

- A) task1 e task2 rodam em paralelo e task3 só roda depois que as duas terminam.
- B) task1 roda, depois task2, e por último task3, sempre em sequência estrita.
- C) task3 roda primeiro e, ao terminar, dispara task1 e task2 em paralelo.
- D) task1 e task2 rodam em paralelo e task3 roda junto, sem esperar ninguém.

<details><summary>Gabarito</summary>

**A.** A **lista** à esquerda indica tarefas **paralelas**; a seta `>>` aponta para quem vem **depois**. A alternativa C inverteu o sentido da seta.
</details>

**32. Para que serve a propriedade python_callable em um operator do Airflow?**

- A) Define a expressão cron que agenda quando o DAG vai ser executado.
- B) Recebe a função Python que será executada quando a task rodar.
- C) Indica o caminho da pasta onde ficam os arquivos de definição do DAG.
- D) Recebe a lista de tasks que precisam terminar antes desta começar.

<details><summary>Gabarito</summary>

**B.** `python_callable=minha_funcao` liga a **função** ao `PythonOperator`. Agendamento é o `schedule`, e dependências são definidas com `>>`.
</details>

**33. O que são os sensors no Airflow, segundo a aula?**

- A) Tasks que medem o uso de CPU e memória dos workers durante a execução do DAG.
- B) Tasks que validam o schema dos dados antes de liberar o carregamento no DW.
- C) Tasks que ficam escutando até uma condição ocorrer, como um evento num tópico.
- D) Tasks que repetem a execução em loop até o DAG inteiro terminar com sucesso.

<details><summary>Gabarito</summary>

**C.** Sensors (lib `sensors`) **esperam** algo acontecer (arquivo, mensagem no Kafka) e são **async**. Loop não existe em DAG, que é acíclico.
</details>

**34. Por que o Airflow tem foco principal em processamento batch?**

- A) Porque fluxos agendados podem ser refeitos e reprocessados, o que é típico do batch.
- B) Porque ele processa todos os dados em memória, o que não cabe em fluxos de streaming.
- C) Porque ele não consegue se integrar a sistemas externos como Kafka ou APIs.
- D) Porque ele só aceita pipelines escritos em SQL, que não funcionam em streaming.

<details><summary>Gabarito</summary>

**A.** O Airflow **agenda e reprocessa** execuções, o que combina com batch. Ele **não processa** os dados (só orquestra), integra com APIs/Kafka e usa **Python**.
</details>

**35. Qual analogia da aula descreve melhor o papel do Airflow?**

- A) Um broker de mensagens, que guarda eventos em tópicos para vários consumidores.
- B) Um cronjob do Linux com mais recursos, que agenda e controla o fluxo de scripts.
- C) Um motor de streaming, que processa eventos com watermarks e janelas de tempo.
- D) Um data warehouse, que guarda os dados tratados para consultas analíticas.

<details><summary>Gabarito</summary>

**B.** Airflow é **orquestrador/agendador**: garante ordem, logs e alertas. Broker é o **Kafka**, motor de streaming é o **Flink**.
</details>

**36. O que significa o "Acyclic" (acíclico) em DAG?**

- A) Que as arestas têm direção: cada dependência aponta para a próxima.
- B) Que as tarefas não dependem umas das outras e rodam em paralelo.
- C) Que o DAG roda uma vez só e não pode ser agendado periodicamente.
- D) Que não há ciclos: o fluxo nunca volta para uma tarefa anterior.

<details><summary>Gabarito</summary>

**D.** Acíclico = **sem loops**. A alternativa A descreve o **Directed** (direcionado), a outra metade da sigla.
</details>

**37. ➕ Na arquitetura do Airflow, qual a diferença entre Scheduler e Worker?**

- A) O Worker decide o que e quando rodar; o Scheduler executa a task de fato.
- B) O Scheduler decide o que e quando rodar; o Worker executa a task de fato.
- C) O Scheduler exibe os DAGs na interface; o Worker guarda o estado das tasks.
- D) O Scheduler guarda variáveis e conexões; o Worker exibe os logs na interface.

<details><summary>Gabarito</summary>

**B.** Scheduler **agenda**, Worker **executa**. A interface é o **Webserver**, e estado/variáveis ficam no **metadata DB**.
</details>

**38. ➕ Qual o significado da expressão cron 0 3 * * * no agendamento de um DAG?**

- A) Executar a cada 3 minutos, sempre.
- B) Executar a cada 3 horas, todo dia.
- C) Executar no dia 3 de cada mês.
- D) Executar todos os dias às 3h00.

<details><summary>Gabarito</summary>

**D.** Campos: **minuto hora dia mês dia-da-semana**. Minuto 0, hora 3, resto qualquer → **todo dia às 3h**. A cada 3 horas seria `0 */3 * * *`.
</details>

---

## Como saber como foi?

| Acertos | Leitura |
|---|---|
| 32 a 38 | Muito bem. Revise só as pegadinhas (source x sink, Table x DataStream, at-least x at-most once, DAG x task). |
| 25 a 31 | Bom. Releia as tabelas de contraste e refaça os flashcards das aulas em que errou. |
| 15 a 24 | Atenção. Refaça o resumo com calma e depois os flashcards. |
| 0 a 14 | Comece de novo pelo **Mapa geral** e pelas caixas 💡 de cada aula. |
