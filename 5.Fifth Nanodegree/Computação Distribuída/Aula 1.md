# Aula 1

## Fundamentos 

* Um sistema distribuído é uma coleção de computadores independentes que se apresenta aos seus usuários como um sistema único.
* Cada computador funciona de forma independente e autônoma.
* Ligados por uma rede.
* Para o usuário final, a complexidade é oculta, pois o sistema parece uma entidade única.
  * Ponto único de acesso.
  * A complexidade é mascarada para garantir usabilidade e escalabilidade.
  * O conceito de transparência permite que a complexidade de múltiplos nós seja oculta.

### Motivação para a Distribuição
* Mudança de paradigma
  * Sistemas centralizados atingiram limites físicos de processamento e armazenamento
  * A necessidade de lidar com Zettabytes exigiu uma nova abordagem.
* Processamento de Big Data
* Alta disponibilidade e resiliência.
* Desempenho e latência.
  * Distribuição geográfica para reduzir latência.

### Evolução Histórica
* Origens militares, e em 1962 foi desenvolvida a Cadeia de Comunicação Distribuída (CCD).
* Criação da ARPANET.
* A necessidade de uma rede robusta levou à divisão de dados em pacotes, despachados por diferentes caminhos, garantindo a entrega mesmo sob falha de nós específicos.
  * Ou seja, múltiplas rotas físicas entre computadores.
* A comutação de pacotes permitiu que redes sobrevivessem mesmo sendo danificadas.
  * Cada pacote também busca o melhor caminho disponível.
* Em 1982 foi adotado o protocolo TCP/IP, permitindo a comunicação de forma transparente entre diferentes redes.
* Arquitetura de camadas (Pilha TCP/IP)
  * Aplicação: HTTP, FTP
  * Transporte: TCP, UDP
  * Rede: IP
  * Enlace: Ethernet, WiFi
* A independência de hardware permitiu que qualquer dispositivo, independente do fabricante, pudesse fazer parto do sistema distribuído.
* A década de 90 marcou a transição dos supercomputadores para sistemas construídos com componentes de prateleira (commodity hardware).
  * Cluster

### Nuvem
* A computação em nuvem representa a personificação dos sistemas distribuídos, democratizando o acesso a recursos de alto desempenho sob demanda.
  * IaaS, PaaS, SaaS.

### Vantagens (da computação distribuída)
* Escalabilidade Horizontal (Scale-Out).
  * Permite expandir o sistema adicionando mais servidores (nós), na infraestrutura existente.
  * Expansão sob demanda.
  * Adiciona mais maquinas no cluster, e não apenas na memória atual.
* Disponibilidade Continua
  * Possui replicação para vários servidores, para que não haja perda caso ocorra algum problema.
  * Redução de downtime e manutenção sem interrupção do sistema.
* Desempenho e Paralelismo
  * Processo simultâneo.
  * Divisão de tarefas.
    * Sub tarefas menores distribuídas entre os nós disponíveis.
  * Otimização de recursos.
    * Balanceia a carga de trabalho de forma inteligente por toda a rede.

### Desafios
* A complexidade da Distribuição.
  * Concorrência
    * Sincronização de processos simultâneos e prevenção de race condition.
  * Tolerância a Falhas
    * Capacidade de operar sob falhas parciais.
  * Consistência
    * Garantir quer todos os nós vejam a mesma versão dos dados replicados.
  * Latência e Rede
    * Lidar com atrasos de comunicação.
* Concorrência e Sincronização
  * Concorrência Intrínseca
    * Múltiplos processos executam de forma independente e simultânea, sem um relógio global, a ordem das operações se tornam imprevisíveis.
  * Garantir a integridade de recursos compartilhados.
* Race Conditions
  * Ocorre quando a saída de um programa depende da sequência ou tempo de execução de operações incontroláveis.
  * Em sistemas distribuídos, a falta de um relógio global agrava isso.
  * Dois processos acessam o mesmo valor e "se perdem" por causa disso.
* Deadlocks
  * Bloqueio mútuo, sendo a situação em qu dois ou mais processos ficam bloqueados esperando uns pelos outros para liberar recursos.
  * Dependência circular.
  * Falta um gerenciador central, que conheça o estado de todos os nós instantaneamente.

### Tipos de Falhas

#### Falhas de Parada
* Ocorre quando um componente do sistema para de funcionar abruptamente e cessa qualquer tipo de processamento ou resposta.
* Mais simples de detectar, pois fica com interrupção total do sistema.

#### Falhas de Omissão
* Componente continua em execução, mas falha em enviar ou receber mensagens através da rede.
* Desafio de rede e sincronização.
  * Perda de pacotes na transmissão.
  * Buffers de entrada ou saída cheios.

#### Falhas Bizantinas (Crítico)
* Ocorre quando um componente do sistema age de forma arbitrária ou maliciosa, enviando mensagens incorretas ou contraditórias.
* A falha mais difícil de detectar.
* Algoritmos de consenso complexos (BFT).
* Um dos nós é "traidor" mandando mensagens falsas.

#### Estratégias de Tolerância a Falhas
* Não sobre evitar erros, mas garantir a continuidade do serviço através de redundância estratégica.
* Redundância
  * Duplicação de componentes críticos de hardware e software para eliminar pontos únicos de falha (SPOF).
* Replicação e Load Balancer
  * Distribuição de carga entre múltiplos servidores que sincronizam dados.
* Praticas SRE
  * Implementação de metodologias do Google (Site Reliability Engineering) para monitoramento.
* Em Sistemas Distribuídos, as falhas são normas, e não exceção.
  * A estratégia reside na mitigação através de redundância.

## Arquiteturas

### Cliente-Servidor
* A arquitetura fundamental.
* Um cliente (navegador, pc, mobile) que faz requisições e recebe respostas de um servidor central.
* Arquitetura simples, com uma gestão centralizada e separação clara de responsabilidades.
* Porém tem um ponto único de falha (servidor), pode sofrer gargalo ao ter sobrecarga com muitos clientes e é mais difícil de escalar, pois precisa ser feito mais verticalmente.

### Peer-to-Peer (P2P)
* No p2p não existe uma hierarquia rígida, sendo que cada nó (peer) atua simultaneamente como cliente e servidor.
  * Solicitando e fornecendo recursos.
* Pode ser escalado organicamente, e é descentralizado.
* O sistema sobrevive mesmo com saídas massivas de nós.
* Alguns aplicações práticas:
  * Torrent
    * Os usuários (peers) compartilham pedaços de arquivos entre si simultaneamente.
    * Quanto mais usuários, maior a disponibilidade do arquivo.
  * Bitcoins
    * Rede p2p para validar transações sem intermediários (bancos).
    * Utiliza um registro distribuído (blockchain) mantido por milhares de nós.
* Ambos os sistemas demonstram como a decentralização resolve problemas de escalabilidade e confiança.

### Microsserviços
* Serviços pequenos, autônomos que trabalham juntos.
* Encapsulamento forte, onde cada serviço esconde sua complexidade e dados.
* Escalabilidade independence e implantação isolada.
* O contrário disso, seria uma abordagem monolítica.

#### Domain-Driven Design (DDD)
* Modelagem estratégica para sistemas distribuídos.
* Fundamental para identificar domínios, definir responsabilidades e delimitar escopos, o que é crucial para o particionamento de microsserviços.
* Basicamente definir bem o que cada módulo deve ser e fazer, delimitando contextos.

## Teorema CAP (Eric Brewer)
* É impossível para um sistema distribuído garantir simultaneamente as três propriedades

### Consistência (C)
* Todos os clientes veem os mesmos dados ao mesmo tempo, independentemente do nó.
* A leitura sempre retorna a escrita recente.

### Disponibilidade (A)
* Cada requisição recebe uma resposta (sucesso ou falha), garantindo que o sistema esteja sempre operacional.

### Tolerância (P)
* O sistema continua operando mesmo que haja falhas de comunicação entre os nós.

* Com isso, se faz necessário ter um trade-off para melhorar algum desses aspectos.

### Sistemas CP
* Prioriza a consistência.
* Em caso de partição de rede, o sistema sacrifica a disponibilidade para garantir que os dados permaneçam idênticos em todos os nós.
* Um exemplo seria os bancos, onde é preferível que não sejam feitas transações, para garantir que não hajam saldos inconsistentes.

### Sistemas AP
* Prioriza a disponibilidade.
* O sistema continua operando durante falhas, aceitando escritas e leituras, mas permite inconsistências temporárias.
* Um exemplo são as redes sociais, que não há problema em ter um feed ligeiramente desatualizado.

## Modelos de Consistência
* O dilema:
  * Consistência alta: Dados sempre atuais, mas maior latência e menor disponibilidade.
  * Alta Performance: Resposta rápida e escalável, mas com risco de dados obsoletos temporários.

### Consistência Forte
* Todas as leituras subsequentes veem a escrita mais recente imediatamente.
* Porém isso causa alta latência (devido a espera por réplicas), e menor disponibilidade em partições.
* Exemplos como bancos ACID tradicionais.
 
### Consistência Eventual
* Se não houve novas escritas, todas as réplicas eventualmente convergirão.
* Baixíssima latência e disponibilidade (modelo AP).
* Exemplos como DNS, DynamoDB e Cache.

## Replicação Líder-Seguidor
* O líder é o responsável pelas escritas, coordenando a propagação de dados e garantindo a ordem das operações.
  * Simplicidade na garantia de consistencia forte para operações de escrita, pois existe apenas uma fonte de verdade.
* Seguidores (backups) atendem as requisições de leitura, mantém cópias sincronizadas do líder e podem ser providos em caso de falha
* Porém o líder pode se tornar um gargalo, pois em caso de falha, o processo de escolher o novo líder é complexo.

## Algoritmos de Consenso

### Paxos
* É um dos algoritmos mais influentes da computação distribuída.
* Tem o objetivo de garantir que um grupo de nós concorde sobre um único valor, mesmo que alguns nós falhem ou mensagens sejam perdidas.
* Papéis
  * Proposers: Enviam sugestões de valores para o sistema.
  * Acceptors: Atuam como um corpo eleitoral, votando e retendo o consenso.
  * Learners: Recebemos o resultado final uma vez que o consenso é alcançado.

### Raft
* Desenvolvido como uma alternativa ao Paxos, o Raft decompõem o problema do consenso em subproblemas independentes, facilitando a implementação e o ensino de sistemas consistentes.
* Estados
  * Follower: Estado passivo, respondendo a requisições de líderes e candidatos.
  * Candidate: Estado transitório usado para iniciar uma nova eleição de líder.
  * Leader: Coordena o cluster, aceita escritas e gerencia a replicação do log.
* Garante que apenas um líder exista por votação da maioria.
* O líder replica entradas para os seguidores e aguarda para confirmar.
* Salva os logs para que não fique nada perdido, e garante que uma entrada seja replicada para maiorias dos nós ao fazer o "commit" dela.

## Estudos de Caso

### Amazon S3
* Armazenamento com replicação massiva.
* Distribuição geográfica.
* Armazenamento de objetos com metadados distribuídos.
* Durabilidade extrema.
* Escalabilidade ilimitada.
* Consistência eventual
  * Otimizada para performance.

### GFS e MapReduce
* Google File System
  * Armazenamento distribuído em hardware commodity.
  * Projetado para alta tolerância a falhas e escalabilidade
* MapReduce
  * Modelo de programação para processamento paralelo massivo.
  * Divisão de tarefas em pequenos fragmentos processados por nós.
  * Capacidade de processar Petabytes.
  * Input -> Transforma -> Consolida -> Output
    * Transformação (`.map()`) e consolidação (`.reduce()`).

### Netflix
* Utiliza microsserviços independentes operando na AWS.
* Isolamento de falhas
* Alta disponibilidade e baixa latência.

### Blockchain
* Cadeia criptográfica
  * Um registro público e imutável onde cada bloco é vinculado ao anterior através de um hash único.
* Elimina a autoridade central, pois é p2p.
* Usa a cadeia mais longa como verdade coletiva, resolvendo o problema de gasto duplo.

## Tendências

### Edge Computing
* Descentralização do processamento, movendo a lógica da nuvem para a borda, próximo aos dispositivos IoT e sensores.
* Isso reduz drasticamente o tráfego de rede e aumenta a autonomia de sistemas locais.
* Menor latência, economia de banda, privacidade e resiliência (funciona localmente).

### Serverless e IA
* Serverless
  * Abstração completa dos servidores, permitindo que o desenvolvedor foque apenas no código
  * Escalabilidade sob demanda
* IA
  * Gerenciamento autônomo dos sistemas distribuídos.
  * Mitigação de falhas antes que afetem a disponibilidade do sistema.