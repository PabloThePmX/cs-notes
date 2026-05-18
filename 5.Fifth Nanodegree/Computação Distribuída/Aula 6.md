# Aula 6

## Filas de Mensagens (Mensageria)
* Sistemas de redes interconectadas que se conectam via troca de mensagens.
* Dessa forma, teremos desacoplamento, escalabilidade horizontal, resiliência (mensagens persistem no broker caso ocorrer uma falha) e balanceamento de carga.
* Sem fila, o acoplamento fica direto.
  * A fila fica entre o produtor e o consumidor.
* Começou nos anos 80 pela IBM.
* Terminologia essencial:
  * Producer: Componente que envia a mensagem.
  * Consumer: Solicita as mensagens.
  * Broker: O middleware que gerencia o armazenamento, roteamento e entrega de segura das mensagem.
  * Queue: Estrutura de dados (geralmente FIFO) que armazena temporariamente as mensagens até ser consumidas.
  * Topic: Canal lógico.
  * Message: O payload.
* Modelos de Comunicação IPC
  * Memória Compartilhada
  * Sockets TCP/UDP
  * RPC (Remote Procedure Call)
  * Message Passing (Assíncrono): Brokers.

### Protocolo AMQP
* Padronização para que clientes em qualquer linguagens possam se comunicar via brokers.
* Protocolo de amada de aplicação focada em mensageria assíncrona orientada a rede.
* Suporte a SASL e TLS.

#### Componentes
* Producer -> Exchange -> Binding -> Queue -> Consumer.
* O exchange é o roteador, responsável por receber mensagens dos produtores e encaminha-los para as filas corretas.
* Regras de Roteamento

#### Tipos de Exchange AMQP
* Direct: Via chave, sendo que a `routing_key` deve ser exatamente igual a `binding_key`.
* Fanout: Encaminha a mensagem para todas as filas vinculadas, ignorando a `routing_key`.
* Topic: Filtro de roteamento, como se fosse uma URL.
  * Usando `*` para uma palavra e `#` para zero ou mais (wildcards).
  * Ex.: `pagamento.*/*.error/#`.
  * Dessa forma da pra fazer logs por serviço e nível.
  * O mais versátil para o dia a dia.
* Headers: Roteia baseando nos headers da mensagem, ignorando a `routing_key`.

#### Garantia de Entrega
* At-most-once: Enviada sem confirmação.
* At-least-once: Ao menos uma vez, e reenvio automático até o ACK.
* Exactly-once: Exatamente uma vez, tem garantia mais forte e complexa.
* Acknowledgments (Confirmations): O `basic_ack` é a sinalização para o broker que a mensagem foi processada com sucesso.

#### Persistência e Durabilidade
* Fila durável (Durable Queue).
* Mensagem Persistente.

#### Prefatch e Fair Dispatch
* Por padrão os brokers distribuem mensagens sequencialmente, o que pode ser ruim.
* Prefatch Count: Define o limite de mensagens não confirmadas
* Fair Dispatch: Garante um despache justo, onde consumidores mais rápidos processam mais mensagens, enquanto os sobrecarregados não recebem tanto.

### Padrões
* Enterprise Integration Patterns
  * 65 padrões documentados para a integração de sistemas.
  * Point-to-Point.
    * Padrão um para um, onde cada mensagem é entregue exatamente para um consumidor.
    * A fila atua como um buffer persistente de trabalho pendente.
    * Promove o balanceamento de carga.
    * Garante que o trabalho não seja duplicado.
  * Publish-Subscribe (Message Topic).
    * Difunde uma mensagem para múltiplos consumidores simultaneamente.
    * One to many.
    * Desacoplamento total, sendo que o publisher não tem conhecimento dos consumers.
    * Usado por notificações globais, invalidar caches, logs de auditoria, etc.
  * Request-Reply.
    * Emula comunicação síncrona enviando uma resposta para uma fila de retorno.
    * O cliente cria uma fila temporária para receber a resposta.
    * A mensagem da request é enviada com metadados específicos de roteamento.
* Competing Consumers.
* Router & Filters.
* Saga Pattern.

### RabbitMQ
* Smart Broker (Fila), pois apaga após o uso.
* Escrito em Erlang.
* Clustering nativo.
* Quorum Queues.
  * Algoritmo Raft.
* Roteamento inteligente com flexilidade total via exchanges: Direct, Fanout, Topic e Headers.
* Extensível via sistema de plugins.
* Foca na garantia de entrega.
* Melhor para tarefas em background e microsserviços.

### Apache Kafka
* Dumb Broker (Log imutável), pois não apaga depois de receber.
  * Estrutura append-only.
  * Cada mensagem recebe um offset único e sequencial.
* Focado em performance.
  * Utiliza zero-copy para transferir dados de cache do SO diretamente para a rede.
* Ecossistema de componentes.
  * Topics e Partitions
  * Brokers
  * Consumer Groups.
* Retenção e Reply.
  * As mensagens não são deletadas após o consumo.
    * Por padrão.
    * Para que possa "voltar no tempo" e ver as mensagens novamente.
    * Diferente do RabbitMQ, que sempre apaga por padrão.
* Melhor para big data, event streaming.
  * Ou seja, melhor para uma quantidade massiva de dados.

### Apache ActiveMQ e Cloud-Native.
* O ActiveMQ é utilizado em ambientes corporativos de Java.
* Na AWS, Cloud, Azure e afins, cada um tem os seus serviços de mensageria.

### Teorema de CAP
* Consistência (C), Disponibilidade (A) e Tolerância a Partições (P).
* Em um sistema distribuído, é impossível garantir simultaneamente os três pilares.
* O RabbitMQ é CP, Kafka é AP/CP e o SQS é AP.

PAREI NO SLIDE 26

