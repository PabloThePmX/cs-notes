# Prova 1

## SO e Componentes

### Conceitos
* Um SO é um software de sistema que atua como intermediário entre o hardware e os aplicativos, gerenciando recursos e fornecendo serviços.
* O kernel é o componente principal e central do SO, gerencia CPU, memória e hardware, agindo como ponte entre o software e o hardware.
  * É o componente com maior privilégio no sistema.
* O gerenciador de processos é o responsável por criar, pausar e agendar processos, distribuindo-so entre a CPU.
* O gerenciador de memória contra o uso da memória RAM e virtual, alocando espaço para cada processo.
* O sistema de arquivos organiza, armazena, recupera e protege arquivos em dispositivos de armazenamento.
* O gerenciador de E/S gerencia a comunicação com todos os periféricos.
* A interface (shell ou GUI) é a camada de comunicação com o usuário.

### Arquiitetura de Camadas
```
Usuário
↓
Aplicações (GUI/Shell)
↓
System Calls
↓
Kernel (Todos os gerenciadores ficam aqui, processos, etc)
↓
Hardware
```

## Modos de Operação e System Calls

### Modos
* Modo usuário: Tem acesso restrito ao hardware, precisando de system calls para recursos do sistema.
  * Se falhar, não compromete o SO, visto que é um processo fora do kernel.
  * Os aplicativos funcionam nesse modo.
* Modo Kernel: Acesso total sobre o hardware, e controla diretamente a CPU, RAM e dispositivos.
  * Um erro grave pode travar ou reiniciar o computador.
  * Os drivers, gerenciadores e o núcleo do SO funcionam nesse modo.
* Essa separação protege o sistema, para que não seja qualquer programa a ter acesso direto ao hardware, evitando bugs e corrupção de memória ou travamento do computador.
  * Ou seja, o modo usuário é uma camada isolada que pode dar problema sem causar preocupação ao resto do sistema.

### System Calls
* É a única forma de um programa acessar recursos do SO.
* O programa faz uma system call para "acessar" o modo kernel e receber aquilo que pediu.
* Alguns exemplos:
  * `open()`
  * `write()`
  * `read()`
  * `close()` -> remove da tabela de processos
  * `fork()` -> Cria um novo processo filho (copia do atual)
* O fluxo de chamada:
```
App (Modo Usuário)
↓
System Call
↓
Kernel verifica permissão
↓
Executa a operação
↓
Retorna (ao modo usuário)
```

## Tipos de Kernel
* Existem 3 tipos de Kernel

### Monolítico
* Todos os serviços ficam dentro do kernel.
* Possui alto desempenho pois não precisa ficar trocando o contexto.
* Um bug pode dar problema em tudo.
* O Linux e BSD funcionam dessa forma

### Microkernel
* Apenas as funções essenciais ficam no núcleo.
* Pode ter desempenho menor pois os processos precisam se comunicar.
* Falhas ficam isoladas.
* Minix é uim exemplo disso.
* Drivers rodam fora do Kernel.

### Hibrido
* Combina o monolítico e o micro.
* Melhor que o monolítico no quesito de isolamento de falhas.
* O Windows e o macOS funcionam dessa forma.




## Tipos de Sistemas Operacionais

### Tempo Real (RTOS)
Apenas 1 usuário, multi-tarefas, prioriza não falhar (Hard e Soft Real Time). (marca-passo, ABS)

### Monotarefa
Apenas 1 usuário, uma tarefa, e se o programa travar, o PC trava por inteiro. (MS-DOS)

### Mono Multitarefa
Apenas 1 usuário, N tarefas. (Windows, macOS)

### Multiusuário
N usuários, N tarefas, com isolamento de sessões. (Linux Server)

### Distribuído
N usuários, N tarefas, faz com que várias máquinas pareçam uma só. (algo tipo o Netflix)

### Redes
N usuários, N tarefas, e vários serviços de redes configurados, como DNS e DHCP. (Windows Server)

### Embarcado
Sem usuário, e apenas 1 ou poucas tarefas, usa recursos mínimos.

### Móvel
Apenas 1 usuário, N tarefas, porém possui gestão de bateria e isolamento de apps.

## Processos e Threads

### Processo
* Um processo é um programa em execução com memória isolada.
* Cada processo tem um PID.
* Possui suas áreas de memória isoladas do resto, sendo elas:
  * Código
  * Dados
  * Heap: alocação dinâmica feita pelo programador, sendo desalocada com o garbage collector.
    * Usa-se `malloc() / new` para alocar memória.
    * Ou `free() / delete` para liberar.
    * Ocorre memory leak caso não seja liberada a memória.
  * Stack: chamadas de função e variáveis locais, gerenciada automaticamente, uma pilha (LIFO).
* PCB - Bloco de Controle de Processo
  * Estrutura interna que a SO mantém cada processo, contendo as informações necessárias de cada um, para que seja possível pausar e retomar sem perder o estado atual.
* Ciclo de vida de um processo:
  * Novo -> Pronto <-> Executando -> Bloqueado -> Executando -> Finalizado
  * Ao bloquear, é porque o processo aguarda o evento de E/S.
* Troca de Contexto:
  * Operação realizada pelo SO para pausar um processo e retomar outro.
  * Salvar: Salva o estado atual no PCB do processo que está saindo.
  * Escalonar: O algoritmo de escalonamento decide quem vai entrar a seguir.
  * Restaurar: O estado do novo processo é carregado do seu PCB para a CPU.
  * Essa troca consome tempo de CPU, por isso quantum muito pequeno no round robin pode ser ruim para o desempenho.

### Threads
* É o fluxo de execução dentro de um processo.
* Compartilham o código, dados, arquivos abertos e o heap.
  * Porém cada thread tem registradores e stack próprios.
* Menor overhead (consumo de recursos, custo de tempo gasto em trocas de contexto e decisões de escalonamento) que processos.
  * Pois como já foi dito, compartilham o mesmo código, dados, arquivos e heap, não precisando duplica-los.
* Múltiplas threads podem rodar simultaneamente.
  * Dessa forma dentro de um processo da pra ter execuções concorrentes.

### Concorrência e Paralelismo
* Concorrência: Alternância de tarefas que da a ilusão de simultaneidade, funcionando mesmo caso tenha apenas 1 núcleo.
* Paralelismo: Execução simultânea em núcleos diferentes (só funciona em multicore).

## Escalonamento de CPU
* Existem diversos algoritmos para isso.

### FCFS (First Come, First Served)
* Ordem de chegada na fila.
* Não é preemptivo (o processo roda até finalizar, não podendo ser cancelado pelo SO).
* O principal problema é que processos longos paralisam todos os demais (convoy effect).

### SJF (Shortest Job First)
* Menor tempo de execução estimado.
* Não preemptivo.
* Fica em starvation (processo nunca executa porque outros sempre têm prioridade) em processos longos e precisa conhecer o tempo antecipadamente.

### Prioridade
* Menor prioridade, podendo ser o número mais alto ou baixo, dependendo da implementação.
* É preemptivo.
* Starvation pode ser resolvido com aging (aumenta a prioridade de processos que esperam muito tempo).

### Round Robin
* Rodízio com quantum (fatia de tempo que um processo pode usar a CPU antes de ser preemptado) de tempo fixo.
* Preemptivo.
* Se o quantum for pequeno, pode ter muita troca de contexto (overhead).

### Multilevel Queue
* Múltiplas filas com critérios diferentes.
* É preemptivo.
* Mais complexo.

* O quantum muito grande vira FCFS, e muito pequeno tem overhead demais, portanto o melhor é ter um equilíbrio nisso.

## Sincronização e Deadlock

### Race Condition
* Ocorre quando múltiplas threads acessa um dado compartilhado e pelo menos uma delas realiza uma escrita, sem sincronizar.
* Dessa forma cada thread estará vendo um valor, criando imprevisibilidade e inconsistência.
* Porém se for lido sem escrita não vai existir esse problema.

### Sincronização
* Alumas formas de sincronização:
  * Mutex: Apenas uma thread acessa o recurso por vez (exclusão total).
  * Semáforo: Controla N threads simultâneas (usa contadores para o controle).
  * Lock: Implementação prática do mutex, com `lock()`, e `unlock()`.
  * Seção Crítica: Trecho de código que acessa dados compartilhados e precisa ser protegido.

### Deadlock
* Ocorre quando processos ficam esperando uns pelos outros indefinidamente, e para que ocorra, as 4 condições devem estar presentes simultaneamente:
  * Exclusão Mútua: Recurso não pode ser usado por dois ao mesmo tempo.
  * Hold and wait: Processo segura um recurso enquanto espera outro.
  * Não preempção: SO não pode tomar o recurso a força do processo.
  * Espera circular: A espera B e B espera A.
* Se qualquer uma das condições for quebrada, não ocorre o deadlock.

## Gerenciamento de Memória

### Memória RAM (primária)
* Volátil, ou seja perde os dados ao desligar.
* Acesso muito rápido.
* Tipicamente entre 8GB até 64GB.
* Usada para dados de processos em execução.

### Memória Virtual
* Usa o disco como extensão.
* Não volátil, ou seja, persiste os dados.
* Muito mais lenta.
* Permite rodar programas maiores que a RAM disponível.
* Arquivo de swap/pagefile armazenado no disco.

### Estratégias de Alocação de Memória

#### Particionamento Fixo
* Divisão em partições de tamanho pré-definido e imutável.
* Fragmenta internamente, pois pode sobrar espaço dentro da partição.

#### Particionamento Dinâmico
* Partições criadas sob medida para cada processo.
* Fragmenta externamente, pois fica com "buracos" entre as partições.

#### Paginação
* Blocos de tamanho fixo, sendo páginas (lógicas) e frames (físicos).
* Resolve a fragmentação externa, mas pode ter internamente devido a última página ser menor.

#### Segmentação
* Segmentos lógicos de tamanhos variáveis (código, heap, stack, etc).
* Pode ter fragmentação externa, pois vai ter segmentos de tamanhos diferentes, ocasionando que "sobre" espaço.

### Hierarquia de Memória
* Primeiro tenta os registradores que fica dentro da CPU.
* Cache L1 que fica dentro do núcleo.
* Cache L2 que fica próximo ao núcleo.
* Cache L3 que é compartilhada entre núcleos.
* RAM
* SSD

## Virtualização
* O Hypervisor é o software que cria e gerencia e isola as VMs (VirtualBox é um exemplo). 
* Host é computador físico, o guest é o dentro da VM.
* O snapshot salva um estado da VM, permitindo restaura-lo depois,

### Hypervisor Tipo 1 - Bare-metal
* Roda diretamente no hardware, sem SO intermediário.
* Maior performance.
* Usado em Datacenters
* Hyper-V, VMware, etc.

### Hypervisor Tipo 2 - Hosted
* Roda como programa em um SO.
* Mais simples.
* Ideal para testes e desenvolvimento.
* VirtualBox, VMware, Workstation, etc.

### Recursos de uma VM
* Uma VM simula um computador completo via software.
* Possui recursos isolados de CPU, RAM, Disco e Placa de Rede.
* O disco virtual pode ser alocado dinamicamente, que cresce conforme o uso.

### Modos de Rede no VirtualBox
* NAT (Padrão): Tem acesso a internet, mas não está visível na rede e não se comunica com as VMs
* Bridge: Tem acesso a internet, está visível na rede (tem IP) e pode se comunicar com outras VMs.
* Rede Interna: Não tem acesso a internet nem está visível na rede, mas pode se comunicar entre outras VMs.
* Host-only Não tem acesso a internet nem está visível na rede, mas pode se comunicar com outras VMs e com o host.