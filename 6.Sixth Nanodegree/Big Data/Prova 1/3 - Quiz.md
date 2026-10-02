# Big Data: Quiz de múltipla escolha

> 50 questões, 4 alternativas cada, no estilo das provas antigas do professor ("qual descreve melhor...", "qual NÃO é...", "qual a diferença..."). Responda no papel e só depois abra o **gabarito**. Questões com ➕ vêm dos links complementares, não das aulas.
> As alternativas erradas foram feitas para parecerem tão boas quanto a certa: use o raciocínio, não o tamanho do texto.

**Placar:** ___ / 50

---

## Aula 1: Introdução ao Big Data

**1. Qual das opções descreve melhor o que é Big Data?**

- A) Um banco relacional de grande porte, mantido em um único servidor com enorme capacidade de armazenamento.
- B) Dados multivariados e de elevada dimensão, geralmente criados em tempo real e com crescimento exponencial.
- C) Um conjunto de ferramentas de BI para montar relatórios e dashboards sobre os dados históricos da empresa.
- D) Dados estruturados e padronizados, coletados em intervalos fixos e guardados apenas em tabelas relacionais.

<details><summary>Gabarito</summary>

**B.** É a definição da aula: dados multivariados, de elevada dimensão, em tempo real e com crescimento exponencial. A alternativa A descreve um banco tradicional, e a C descreve BI.
</details>

**2. Qual dos itens abaixo NÃO é um dos 5 V's do Big Data?**

- A) Veracidade
- B) Velocidade
- C) Variedade
- D) Validação

<details><summary>Gabarito</summary>

**D.** Os 5 V's são Volume, Velocidade, Variedade, Veracidade e Valor. "Versatilidade" não faz parte.
</details>

**3. Quais V's foram acrescentados aos 3 V's de Doug Laney (2001) para formar os 5 V's?**

- A) Veracidade e Valor
- B) Velocidade e Variedade
- C) Volume e Veracidade
- D) Valor e Velocidade

<details><summary>Gabarito</summary>

**A.** Laney propôs Volume, Velocidade e Variedade. Depois vieram Veracidade e Valor. As alternativas B, C e D misturam V's que já eram dele.
</details>

**4. Segundo a aula, o que a Veracidade exige dos dados?**

- A) Que sejam gerados em fluxo contínuo, 24 horas por dia, sem interrupção e sem atraso na chegada ao destino final.
- B) Que venham de muitas fontes e tipos diferentes, entre dados estruturados e não estruturados.
- C) Que passem por verificação antes de serem armazenados, evitando dados falsos, incompletos ou duvidosos.
- D) Que gerem vantagem competitiva e melhor serviço ao cliente por meio das informações extraídas.

<details><summary>Gabarito</summary>

**C.** Veracidade é confiar no dado antes de guardar. A descreve **Velocidade**, B descreve **Variedade** e D descreve **Valor**.
</details>

**5. Qual V tem como problema a dificuldade de armazenar, minerar e analisar muitas fontes e tipos de dados, e como solução bancos não relacionais, como o MongoDB?**

- A) Volume
- B) Variedade
- C) Velocidade
- D) Veracidade

<details><summary>Gabarito</summary>

**B.** Variedade lida com muitas fontes e tipos, e os bancos não relacionais armazenam bem tipos diferentes. O Volume é resolvido com armazenamento mais barato.
</details>

**6. Segundo os slides, o que é o Hadoop?**

- A) Uma implementação open-source do conceito de MapReduce, usada para armazenar e processar Big Data.
- B) Um banco não relacional criado pelo Google, com operações PUT, GET, DELETE e SCAN sobre tabelas.
- C) Um sistema de arquivos distribuído proprietário do Google, usado apenas dentro da própria empresa.
- D) Um serviço de nuvem do Google para consultas SQL analíticas sobre grandes volumes de dados.

<details><summary>Gabarito</summary>

**A.** Hadoop é a versão open-source do MapReduce. B descreve o **BigTable**, C o **GFS** e D o **BigQuery**.
</details>

---

## Aula 2: Pipeline de dados, formatos e ferramentas

**7. Qual é a ordem correta das etapas de um data pipeline?**

- A) Ingestão, coleta, processamento, armazenamento e consumo
- B) Coleta, armazenamento, ingestão, consumo e processamento
- C) Coleta, processamento, ingestão, consumo e armazenamento
- D) Coleta, ingestão, armazenamento, processamento e consumo

<details><summary>Gabarito</summary>

**D.** A ordem é coleta, ingestão, armazenamento, processamento e consumo. As demais trocam etapas de lugar.
</details>

**8. Como a aula classifica e-mails, vídeos e áudios, e o que é preciso fazer com eles?**

- A) Semiestruturados, pois têm um pouco de padrão e podem ser lidos direto por consultas SQL comuns.
- B) Estruturados, pois ficam em tabelas com esquema fixo e podem ser analisados sem nenhum preparo.
- C) Não estruturados, pois não têm padrão, e precisam passar por um processo que gere metadados.
- D) Semiestruturados, pois seguem o formato CSV ou JSON, e só precisam ser convertidos em tabelas.

<details><summary>Gabarito</summary>

**C.** E-mails, vídeos e áudios são não estruturados. Os semiestruturados são CSV e JSON (alternativas A e D), e os estruturados são as tabelas (B).
</details>

**9. Qual alternativa descreve corretamente o papel de Spark, Flink e Kafka em um pipeline?**

- A) Spark processa em lote para o data lake, Flink processa fluxos (stream) e Kafka transporta os dados até eles.
- B) Spark processa fluxos em tempo real, Flink processa em lote para o data lake e Kafka armazena os dados finais.
- C) Kafka processa em lote para o data lake, Spark transporta os dados e Flink armazena os resultados finais.
- D) Flink processa em lote para o data lake, Spark processa fluxos e Kafka executa as consultas dos usuários.

<details><summary>Gabarito</summary>

**A.** Spark é batch/data lake, Flink é stream e Kafka transporta. As demais trocam os papéis.
</details>

**10. No contexto de um pipeline com Flink, o que são Source e Sink?**

- A) Source é o destino que recebe o resultado final e Sink é a origem dos dados enviados ao pipeline.
- B) Source é a origem que fornece os dados e Sink é o destino que os recebe, como um funil de fontes.
- C) Source e Sink são ambos origens de dados, e diferem apenas pelo formato, estruturado ou não.
- D) Source é o motor que processa os dados e Sink é a camada que guarda os metadados do pipeline.

<details><summary>Gabarito</summary>

**B.** Várias fontes (source) alimentam um destino (sink), como um funil. A alternativa A inverte os papéis.
</details>

**11. ➕ Qual alternativa compara corretamente os formatos Parquet e Avro?**

- A) Ambos são colunares e ideais para escrita rápida de registros individuais em tempo real.
- B) Parquet é orientado a linhas e usado em streaming; Avro é colunar e usado em análises.
- C) Ambos são formatos de texto legíveis por humanos, sem esquema definido, no mesmo estilo de CSV e JSON.
- D) Parquet é colunar, para análise em data lakes; Avro é de linha, binário e evolui bem o esquema.

<details><summary>Gabarito</summary>

**D.** Parquet é colunar (análise em data lakes). Avro é binário, orientado a linha e forte em evolução de esquema (bom para Kafka). B inverte as orientações.
</details>

**12. Qual afirmação sobre o Apache Flink é correta segundo a aula?**

- A) É um banco de dados que persiste os dados de forma definitiva, assim como o Spark.
- B) Funciona apenas em lote, com jobs escritos exclusivamente em SQL e sem suporte a Java.
- C) É um motor de processamento, como o Spark, com jobs em Java e também o FlinkSQL.
- D) É um sistema de transporte de mensagens entre origem e destino, como o Kafka.

<details><summary>Gabarito</summary>

**C.** O Flink é um motor de processamento (como o Spark), com jobs em Java e o FlinkSQL. A alternativa D descreve o **Kafka**.
</details>

**13. ➕ Quais são os quatro componentes principais de um pipeline de dados segundo a AWS?**

- A) Coleta, ingestão, processamento e consumo
- B) Fontes, transformações, dependências e destinos
- C) Extração, limpeza, carga e visualização
- D) Produtores, consumidores, tópicos e partições

<details><summary>Gabarito</summary>

**B.** AWS: fontes, transformações, dependências e destinos. A alternativa A mistura com as etapas vistas em aula, e D é vocabulário do Kafka.
</details>

---

## Aula 3: ETL, streaming e latência

**14. Qual alternativa descreve corretamente o fluxo de um ETL?**

- A) Extract coleta das fontes, Transform limpa e modela, Load carrega o dado pronto no destino final.
- B) Extract carrega o dado bruto no destino, Transform ocorre lá dentro e Load libera os dados ao consumo final.
- C) Extract limpa o dado na origem, Transform grava no destino e Load extrai o dado para análise.
- D) Extract copia para o data lake, Load transforma o dado e Transform entrega aos relatórios.

<details><summary>Gabarito</summary>

**A.** ETL transforma antes de carregar. A alternativa B descreve o fluxo do **ELT**.
</details>

**15. Segundo a aula, qual é a relação do Apache Flink com a persistência dos dados?**

- A) Ele armazena os dados por tempo indeterminado, funcionando como um data lake para consultas.
- B) Ele grava os dados em um banco relacional interno antes de entregá-los ao destino do pipeline.
- C) Ele é só uma passagem dos dados e não possui persistência, que fica a cargo de source e sink.
- D) Ele persiste apenas os dados brutos e descarta os resultados transformados depois do envio.

<details><summary>Gabarito</summary>

**C.** O Flink é uma passagem: o dado vem do source e vai para o sink, sem persistência própria.
</details>

**16. Por que trafegar dados na rede é um problema no processamento de streaming?**

- A) Porque a rede reduz o volume dos dados, e o stream acaba perdendo informações relevantes.
- B) Porque a rede obriga que os dados sejam gravados em disco antes de qualquer processamento posterior.
- C) Porque a rede impede o uso de formatos binários, como o Avro, nos jobs de processamento.
- D) Porque a rede gera latência alta, e o streaming precisa de latência baixa para responder rápido.

<details><summary>Gabarito</summary>

**D.** Streaming exige latência baixa, e trafegar dados na rede aumenta a latência.
</details>

**17. O que a aula sugere quando os dados são muito pesados para serem processados diretamente?**

- A) Descartar parte dos dados antes da coleta, para reduzir o volume enviado ao pipeline.
- B) Pré-prepará-los em um banco específico, já com os joins e filtros aplicados.
- C) Enviar tudo para o Kafka e deixar o processamento a cargo do consumidor final.
- D) Trocar o processamento por consultas manuais feitas por analistas sobre a origem.

<details><summary>Gabarito</summary>

**B.** Pré-preparar em um banco específico, com joins e filtros, deixa o dado pronto para a etapa seguinte.
</details>

**18. ➕ Qual alternativa compara corretamente processamento batch e stream?**

- A) Batch tem latência alta e custo menor, em intervalos agendados; stream tem latência baixa e infraestrutura complexa.
- B) Batch tem latência baixa e custo maior; stream roda em intervalos agendados com infraestrutura mais simples e barata.
- C) Ambos têm a mesma latência, e a diferença é só o formato: tabelas no batch e arquivos no stream.
- D) Batch processa dado a dado em tempo real; stream junta grandes blocos e os processa em horários fixos.

<details><summary>Gabarito</summary>

**A.** Batch é agendado, de latência alta e mais barato. Stream é contínuo, de baixa latência e mais complexo. A alternativa D inverte as definições.
</details>

**19. ➕ Qual alternativa compara corretamente RabbitMQ e Kafka?**

- A) RabbitMQ usa pull, retém as mensagens para reprocessar e chega a milhões por segundo; Kafka usa push e exclui após o consumo.
- B) Ambos excluem a mensagem logo depois do consumo e diferem apenas pela linguagem do cliente.
- C) RabbitMQ entrega por push e exclui a mensagem após o consumo; Kafka usa pull, retém e permite reprocessar eventos.
- D) RabbitMQ é plataforma distribuída de eventos para big data; Kafka é agente de mensagens com filas prioritárias.

<details><summary>Gabarito</summary>

**C.** RabbitMQ: push, exclui após consumo, filas prioritárias. Kafka: pull, retém e permite replay. A e D invertem as características.
</details>

---

## Aula 4: Data Warehouse, Data Lake e Lakehouse

**20. Qual alternativa descreve o Star Schema?**

- A) Modelo não relacional que evita joins ao guardar documentos aninhados dentro de coleções.
- B) Modelo do data lake que guarda arquivos brutos, sem hierarquia de pastas, em um object storage na nuvem.
- C) Modelo de streaming que distribui eventos em tópicos do Kafka com o nome da tabela de origem.
- D) Modelo de data warehouse que agrega os dados e evita vários joins, pois já ficam prontos para busca.

<details><summary>Gabarito</summary>

**D.** O Star Schema é usado em data warehouse, tudo relacional, para evitar vários joins. A alternativa A lembra o MongoDB, e B descreve o data lake.
</details>

**21. Qual é a linha do tempo correta das arquiteturas de dados vistas em aula?**

- A) Data Lake, Data Warehouse e Data Lakehouse
- B) Data Lakehouse, Data Lake e Data Warehouse
- C) Data Warehouse, Data Lake e Data Lakehouse
- D) Data Warehouse, Data Lakehouse e Data Lake

<details><summary>Gabarito</summary>

**C.** Data Warehouse, depois Data Lake e, por fim, Data Lakehouse.
</details>

**22. Por que o Data Lake passou a ser viável?**

- A) Porque os formatos de dados foram padronizados, eliminando a necessidade de metadados.
- B) Porque o armazenamento ficou mais barato, o que permite guardar todos os tipos de dados.
- C) Porque os bancos relacionais deixaram de funcionar com grandes volumes, forçando a troca.
- D) Porque o processamento em batch foi substituído pelo streaming, que dispensa armazenamento.

<details><summary>Gabarito</summary>

**B.** O armazenamento ficou mais barato, e isso tornou possível guardar dados de todos os formatos e origens.
</details>

**23. Como o Data Lake é descrito em aula e por que ele não tem hierarquia de pastas?**

- A) É um object storage, como o S3, sem hierarquia de pastas, para evitar recursividade nas buscas.
- B) É um sistema de arquivos tradicional, com pastas aninhadas, para facilitar a navegação dos usuários.
- C) É um banco relacional com tabelas ligadas por chaves, para garantir a integridade das consultas.
- D) É um servidor de mensagens com filas ordenadas, para garantir a entrega na ordem de envio.

<details><summary>Gabarito</summary>

**A.** Object storage sem pastas evita recursividade ao buscar. B descreve o oposto.
</details>

**24. O que o Data Lakehouse adiciona ao Data Lake?**

- A) Uma camada de star schema, que obriga todos os dados a seguirem um único modelo relacional.
- B) Uma camada de transporte, que replica os dados do banco para tópicos de streaming em tempo real.
- C) Uma camada de armazenamento mais barata, que substitui os arquivos do lake por tabelas fixas.
- D) Uma camada de metadados e governança, com origem, qualidade e quem atualizou cada dado.

<details><summary>Gabarito</summary>

**D.** O Lakehouse acrescenta metadados e governança. A alternativa A descreve o data warehouse, e B descreve o CDC.
</details>

**25. ➕ Qual recurso o Data Lakehouse traz do data warehouse para o data lake (Databricks)?**

- A) Armazenamento exclusivo de dados estruturados, em tabelas relacionais com esquema fixo.
- B) Transações ACID e aplicação de esquema sobre arquivos em formatos abertos, como Parquet.
- C) Eliminação de qualquer camada de metadados, para reduzir o custo de consulta dos dados.
- D) Duplicação dos dados em dois sistemas, um para análise e outro para machine learning.

<details><summary>Gabarito</summary>

**B.** O Lakehouse traz ACID e aplicação de esquema sobre formatos abertos (Delta Lake sobre Parquet). A alternativa D descreve a arquitetura de duas camadas que ele substitui.
</details>

**26. ➕ Qual combinação descreve corretamente o esquema de data lake e data warehouse?**

- A) Lake usa schema-on-write, definindo a estrutura ao gravar; warehouse usa schema-on-read.
- B) Ambos usam schema-on-read, definindo a estrutura somente no momento em que o dado é lido por uma consulta.
- C) Lake usa schema-on-read, definindo ao ler; warehouse usa schema-on-write, definindo ao gravar.
- D) Ambos usam schema-on-write, definindo a estrutura antes de gravar qualquer dado novo.

<details><summary>Gabarito</summary>

**C.** O lake guarda bruto e define a estrutura ao ler. O warehouse define ao gravar. O lakehouse combina os dois.
</details>

---

## Aula 5: Flink na prática (tempo, watermarks e connectors)

**27. O que são watermarks no Flink?**

- A) Registros especiais inseridos nos dados do stream para marcar a passagem do tempo.
- B) Marcas de segurança gravadas nos arquivos do data lake para impedir cópias não autorizadas.
- C) Colunas de auditoria que guardam a data da última alteração de cada linha do banco.
- D) Mensagens de confirmação que o Kafka envia ao consumidor depois de ler cada tópico.

<details><summary>Gabarito</summary>

**A.** Watermarks marcam a passagem do tempo no stream. A alternativa C lembra o CDC por timestamp.
</details>

**28. Qual alternativa descreve corretamente ISO 8601 e Epoch UNIX?**

- A) ISO 8601 é um inteiro de segundos, e o Epoch UNIX é um texto com data, hora e fuso.
- B) Ambos são textos no formato data-hora e sempre trazem o fuso UTC dentro da representação.
- C) Ambos são números inteiros, e a diferença é apenas se contam segundos ou milissegundos.
- D) ISO 8601 é um padrão de timestamp em texto, com ou sem UTC; o Epoch UNIX é um inteiro.

<details><summary>Gabarito</summary>

**D.** ISO 8601 é texto, com UTC ou sem. Epoch UNIX é um inteiro. A alternativa A inverte os dois.
</details>

**29. Para que servem o Faker e o Datagen no Flink?**

- A) São connectors que leem logs de transação de bancos relacionais e os enviam ao Kafka.
- B) São ferramentas para gerar dados sintéticos, úteis para testar pipelines sem dados reais.
- C) São formatos binários de serialização que substituem o Avro em pipelines de streaming.
- D) São motores de armazenamento compatíveis com S3 para guardar os dados brutos da bronze.

<details><summary>Gabarito</summary>

**B.** Geram dados sintéticos para testes. A alternativa A descreve o Debezium, e D lembra o minIO.
</details>

**30. No Flink, quando não há sink definido, o que o `blackhole` faz?**

- A) Descarta apenas os dados inválidos e salva os demais em uma tabela temporária.
- B) Gera dados sintéticos de forma contínua, a partir de repositórios de dados falsos.
- C) Serve de destino que gera os dados, mas não os salva em lugar algum.
- D) Envia as mensagens do Flink para uma fila do RabbitMQ chamada blackhole.

<details><summary>Gabarito</summary>

**C.** O `blackhole` é um sink "buraco negro": gera os dados e não salva. B descreve o Faker.
</details>

**31. Para que serve a cláusula `WITH` ao criar uma tabela no Flink SQL?**

- A) Define o connector e suas opções, criando uma tabela temporária que depois é inserida no sink.
- B) Define o esquema relacional final e grava os dados de forma permanente no PostgreSQL usado como destino do pipeline.
- C) Define a janela de tempo do watermark e descarta os registros atrasados do stream.
- D) Define o tipo do job, batch ou stream, e é sempre igual, qualquer que seja o source.

<details><summary>Gabarito</summary>

**A.** O `WITH` configura o connector e muda conforme o source. D erra ao dizer que é sempre igual.
</details>

**32. O que é o `sql-client.sh` e como o modelo de streaming se comporta nele?**

- A) Interface web que mostra o dashboard do Flink e acompanha a memória usada pelos jobs em execução.
- B) Script que compila jobs em Java e os envia ao JobManager para rodarem uma única vez.
- C) Cliente do Kafka que lista os tópicos e as mensagens gravadas pelos produtores.
- D) Terminal SQL do Flink, em que a consulta de streaming roda sem parar até ser interrompida.

<details><summary>Gabarito</summary>

**D.** É o terminal SQL do Flink, e o streaming roda sem parar. A alternativa A descreve o dashboard (porta 8081).
</details>

**33. ➕ Qual alternativa diferencia TIMESTAMP e TIMESTAMP_LTZ no Flink SQL?**

- A) TIMESTAMP guarda em UTC e converte ao ler; TIMESTAMP_LTZ não tem fuso e é só texto.
- B) Ambos guardam o fuso dentro do valor, e a diferença é apenas a precisão dos segundos fracionários.
- C) TIMESTAMP não tem fuso e é só data-hora; TIMESTAMP_LTZ guarda em UTC e exibe no fuso local.
- D) TIMESTAMP é um inteiro desde 1970; TIMESTAMP_LTZ é um texto no padrão ISO 8601.

<details><summary>Gabarito</summary>

**C.** TIMESTAMP é como `LocalDateTime` (sem fuso), e TIMESTAMP_LTZ é como `Instant` (UTC, exibido no fuso local). D mistura com Epoch e ISO 8601.
</details>

**34. ➕ No exemplo de PyFlink com RabbitMQ do professor, qual o papel das filas fila01_source e fila01_sink?**

- A) A source recebe os resultados processados e a sink fornece as mensagens de entrada do job.
- B) A source é a fila de entrada lida pelo job do Flink e a sink é a fila que recebe as mensagens.
- C) Ambas são filas de entrada, e o job as combina em uma tabela temporária antes de gravar no sink.
- D) Ambas são filas de erro, que guardam as mensagens rejeitadas pelo job durante a leitura.

<details><summary>Gabarito</summary>

**B.** O job lê da `fila01_source` e envia para a `fila01_sink`. A alternativa A inverte os papéis.
</details>

---

## Aula 6: ETL x ELT

**35. Qual é a diferença fundamental entre ETL e ELT?**

- A) O ETL carrega o dado bruto no destino e transforma lá dentro; o ELT transforma em servidor intermediário.
- B) Os dois diferem apenas pelas ferramentas, e a transformação ocorre sempre em um servidor intermediário.
- C) O ETL transforma em servidor intermediário antes da carga; o ELT carrega o bruto e transforma no destino.
- D) O ETL só é usado em streaming e o ELT só em batch, mas ambos transformam antes da carga.

<details><summary>Gabarito</summary>

**C.** ETL: transforma antes de carregar, em servidor dedicado. ELT: carrega o bruto e transforma no destino. A alternativa A inverte as definições.
</details>

**36. Em qual situação o ETL é a melhor escolha?**

- A) Integração com sistemas legados e exigência regulatória de dado mascarado ou validado antes de armazenar.
- B) Ingestão de streaming com alto volume, como logs, IoT e cliques, em ambientes cloud-native elásticos de grande escala.
- C) Data lakes e lakehouses que alimentam vários times de análise com o mesmo dado bruto.
- D) Cenários em que é preciso preservar o dado bruto para reprocessar sem extrair a origem de novo.

<details><summary>Gabarito</summary>

**A.** ETL serve a legados, a exigências regulatórias e a batch tradicional. As alternativas B, C e D são casos de uso do **ELT**.
</details>

**37. Qual vantagem do ELT permite reprocessar os dados sem extraí-los novamente da origem?**

- A) A transformação centralizada em um servidor dedicado, que facilita a auditoria dos dados.
- B) O custo concentrado em servidores de transformação, que torna o orçamento mais previsível.
- C) A entrega do dado já modelado, que dispensa qualquer outra etapa antes do consumo final.
- D) A preservação do dado bruto (raw) no destino, que permite várias transformações a partir dele.

<details><summary>Gabarito</summary>

**D.** O ELT mantém o dado bruto no destino. As alternativas A, B e C são características do ETL.
</details>

**38. Qual alternativa descreve corretamente o trade-off de governança entre ETL e ELT?**

- A) No ETL o dado bruto fica no destino e exige controle de acesso robusto; no ELT é validado e limpo antes.
- B) Em ambos a governança é idêntica, pois o dado bruto nunca é guardado no destino final.
- C) No ELT o dado é validado e limpo antes da carga, o que reduz o risco de expor dado sensível.
- D) No ETL o dado é validado antes da carga; no ELT o bruto fica no destino e exige controle de acesso.

<details><summary>Gabarito</summary>

**D.** ETL valida antes de carregar. ELT guarda o bruto, então exige controles de acesso robustos. A e C trocam os papéis.
</details>

**39. Qual alternativa descreve melhor o custo de storage e de processamento em ETL e ELT?**

- A) O ELT gasta mais em poder de transformação dedicado; o ETL gasta mais em armazenar o dado bruto.
- B) Os dois gastam igual, pois o custo depende apenas da quantidade de fontes do pipeline.
- C) O ETL tem custo elástico, pago sob demanda; o ELT tem custo concentrado em servidores dedicados.
- D) O ELT tende a gastar mais em armazenamento do dado bruto; o ETL, em transformação dedicada.

<details><summary>Gabarito</summary>

**D.** ELT guarda o bruto (mais storage). ETL paga por servidores de transformação. A e C invertem as características.
</details>

**40. Qual sequência descreve a arquitetura típica de um pipeline ELT moderno?**

- A) Fontes são extraídas e carregadas na zona raw do data lake, transformadas no warehouse e vão à zona curated.
- B) Fontes são transformadas em um servidor ETL, carregadas já modeladas e entregues direto aos dashboards de negócio.
- C) Fontes são enviadas ao warehouse, transformadas na zona curated e só depois gravadas na zona raw.
- D) Fontes são replicadas por CDC em tempo real, sem zona raw, e entregues apenas aos relatórios.

<details><summary>Gabarito</summary>

**A.** Extract, Load na zona raw, Transform no próprio warehouse, zona curated e consumo. A alternativa B descreve o ETL.
</details>

**41. ➕ Segundo a AWS, qual alternativa compara corretamente ETL e ELT?**

- A) O ELT é mais lento e voltado a dados estruturados; o ETL aceita dados de qualquer tipo.
- B) O ETL é mais rápido e mais barato que o ELT, e se adapta melhor a dados não estruturados em nuvem.
- C) O ELT aceita dados de todos os tipos e é mais rápido; o ETL é voltado a dados estruturados.
- D) Ambos têm a mesma velocidade, e a diferença é que só o ELT usa segurança integrada.

<details><summary>Gabarito</summary>

**C.** ELT: todos os tipos de dado, mais rápido, mais econômico e com segurança do próprio banco. ETL: dados estruturados, mais lento.
</details>

---

## Aula 7: Arquitetura Medallion e CDC

**42. Na Arquitetura Medallion, o que fica na camada bronze?**

- A) Dados agregados e prontos para uso por áreas de negócio, BI e modelos de machine learning.
- B) Dados brutos (raw), do jeito que chegaram da fonte, geralmente salvos em formato Parquet.
- C) Dados limpos e validados, já padronizados em esquemas e prontos para serem agregados.
- D) Apenas os metadados e a governança, com a origem e a qualidade de cada tabela do lake.

<details><summary>Gabarito</summary>

**B.** Bronze é o dado bruto (raw). A alternativa A descreve a camada ouro, e C a prata.
</details>

**43. Qual alternativa descreve melhor o que é o CDC (Change Data Capture)?**

- A) Técnica que reprocessa o conjunto inteiro de dados a cada execução para manter o destino atualizado.
- B) Técnica que compara cópias completas das tabelas e envia o histórico anterior à sua implantação.
- C) Design pattern que captura as mudanças incrementais do banco e as replica, sem sobrecarregar a origem.
- D) Gatilho de banco que grava cada alteração em outra tabela, o que aumenta a carga da origem.

<details><summary>Gabarito</summary>

**C.** CDC é um design pattern de captura incremental, com baixa latência. A alternativa D descreve apenas o **CDC por trigger**.
</details>

**44. O que acontece com os dados que já existiam no banco antes de o CDC ser implementado?**

- A) Eles não são capturados, pois o CDC não olha o passado, só as mudanças após a implantação.
- B) Eles são capturados todos de uma vez, junto das novas alterações, no primeiro ciclo de leitura.
- C) Eles são capturados apenas se tiverem sido apagados do banco com o comando delete.
- D) Eles são capturados desde que a replicação lógica esteja habilitada para as tabelas.

<details><summary>Gabarito</summary>

**A.** O CDC não olha o passado, só as mudanças incrementais. A replicação lógica (D) é requisito do WAL, não traz o histórico.
</details>

**45. Quais são as três formas de CDC vistas em aula?**

- A) Log, snapshot e timestamp
- B) Trigger, replicação e snapshot
- C) Log, trigger e fila (queue)
- D) Log, trigger e timestamp

<details><summary>Gabarito</summary>

**D.** As três formas são log, trigger e timestamp.
</details>

**46. Por que o CDC por log é a forma mais popular e indicada para Big Data?**

- A) Executa consultas SQL periódicas comparando a data da última alteração, o que sobrecarrega o banco.
- B) Lê os logs de transação do banco (logs de DML) e repassa as alterações, sem sobrecarregar a origem.
- C) Usa funções do banco que gravam a alteração em outro lugar, mas têm custo maior para o sistema.
- D) Compara dois snapshots completos da tabela e envia só as diferenças, lendo grande volume de dados.

<details><summary>Gabarito</summary>

**B.** Ler os logs é mais eficiente que consultar o banco. A alternativa A descreve o CDC por **timestamp**, e C descreve o **trigger**.
</details>

**47. O que é o Debezium?**

- A) Um plugin conectado ao banco que traz o log estruturado, usado com o Kafka Connect e que envia JSON.
- B) Um motor de processamento de fluxos que executa jobs em Java, como o Flink, sobre tópicos do Kafka em tempo real.
- C) Um orquestrador de workflows em Python que agenda as cargas em batch entre origem e destino.
- D) Um formato de arquivo colunar com compressão snappy, usado na camada bronze do data lake.

<details><summary>Gabarito</summary>

**A.** O Debezium é um plugin do banco para CDC por log, normalmente com o Kafka Connect. B é o Flink, C é o Airflow e D é o Parquet.
</details>

**48. Qual alternativa descreve corretamente o WAL (Write Ahead Logging) do Postgres?**

- A) Grava a alteração no disco primeiro e só depois a registra no log de transações do banco.
- B) É um tipo de índice do Postgres que acelera as consultas executadas pelo mecanismo de CDC.
- C) Grava no log o que vai acontecer antes de efetivar a alteração, e o Debezium lê esse log.
- D) É um formato JSON enviado ao Kafka que traz o campo op com o tipo de cada ação.

<details><summary>Gabarito</summary>

**C.** O WAL registra no log antes de efetivar, e o Debezium lê esse log. A alternativa A inverte a ordem.
</details>

**49. Na mensagem JSON enviada pelo Debezium, o que indica o campo `op`?**

- A) O nome da tabela de origem, que dá nome ao tópico criado no Kafka para as alterações.
- B) O esquema da tabela e as colunas alteradas, em formato Avro, para cada mensagem enviada.
- C) O tipo da ação, como insert, update ou delete, que ocorreu no banco de dados.
- D) A posição da mensagem no log do banco, para a leitura recomeçar de onde parou.

<details><summary>Gabarito</summary>

**C.** O `op` traz o tipo da ação. A alternativa A é sobre o nome do tópico, que usa esquema e tabela.
</details>

**50. Por que o CDC por timestamp também sobrecarrega o banco de dados?**

- A) Porque grava cada alteração em memória e só a persiste quando ocorre o commit da transação.
- B) Porque dispara consultas repetidas, comparando com a última, para ver se a data mudou.
- C) Porque executa uma função dentro do banco a cada alteração, aumentando o custo das escritas.
- D) Porque lê o log de transações inteiro a cada ciclo, mesmo quando nada mudou desde a última leitura.

<details><summary>Gabarito</summary>

**B.** O timestamp consulta o banco o tempo todo para ver se algo mudou. A alternativa C descreve o **trigger**, e D, o **log**.
</details>

---

## Como saber como foi?

| Acertos | Leitura |
|---|---|
| 43 a 50 | Muito bem. Revise só as pegadinhas (ETL x ELT, as 3 formas de CDC, os V's). |
| 33 a 42 | Bom. Releia as tabelas de contraste e refaça os flashcards das aulas em que errou. |
| 20 a 32 | Atenção. Refaça o resumo com calma e depois os flashcards. |
| 0 a 19 | Comece de novo pelo **Mapa geral** e pelas caixas 💡 de cada aula. |
