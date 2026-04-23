# Aula 3

## Processos e Threads

### Processo
* Um processo seria basicamente um programa em execução.
  * Quando é aberto o programa, o SO cria um processo para executa-lo.
* Cada um recebe um PID (Process ID).
* Um mesmo programa pode ter vários processos.
* O processo é segmentado em código, dados, heap e stack.

#### Heap e Stack
* Quando o SO cria um processo, ele reserva um espaço de endereçamento virtual para o mesmo.
  * Dentro desse espaço, os segmentos do processo ocupam suas regiões.
  * O que sobra entre o heap e a stack é espaço disponível.
    * Que ainda não foi alocado para nenhum dos dois.

* Heap
  * Área da memória usada para alocação dinâmica, controlada pelo programador.
    * Objetos criados dinamicamente ficam aqui, como objetos e arrays.
  * Cresce para cima no endereçamento virtual.
* Stack
  * Área de memória usada para chamadas de função, dados temporários e variáveis locais, gerenciada automaticamente pelo sistema.
  * Cresce para baixo no endereçamento virtual.
  * Stack overflow é o transbordamento de pilha, que acontece quando a pilha cresce além do espaço disponível.

#### Tabela de Descritores
* É uma estrutura do SO que mantém a lista de recursos abertos por um processo.
  * Como arquivos, sockets, pipes, dispositivos I/O, etc.
* Vai ter informações com File Descriptor (FD), arquivo, posição e permissões.
  * `stdin`, `stdout` e `stderr` são a entrada padrão (input como um teclado), saída padrão e erro padrão respectivamente.

#### Contexto de Processo
* É o conjunto de informações que representa o estado atual da execução de um programa.
  * Guarda exatamente onde o processo estava executando naquele momento.
  * Pois se o SO interromper, ele precisa voltar exatamente de onde tinha parado.

* Estrutura de Contexto
  * Program Counter (PC)
    * Guarda o endereço da próxima instrução que será executada.
  * Stack Pointer (SP)
    * Aponta para o topo da stack da função atual, permitindo que variáveis locais e funções continuem corretamente.
  * Registradores da CPU
    * A CPU possui registradores que guardam valores temporários usados pelo processo.
  * Estado da CPU.
    * Indica em que situação o processa está. (Running, ready, waiting, etc).

#### Bloco de Controle de Processo (PCB)
* Guarda todas as informações para o SO gerenciar e executar um processo.
* Quando um processo é criado, o SO cria um PCB para controla-lo.
* Salva informações como PID, estado, memória, prioridade, etc.
* Separa em contexto de hardware e software.
  * O de hardware engloba a parte de estrutura de contexto
  * O de software possui escalonamento, estado, informações de E/S, PID, memória e permissões.

#### Estados de um Processo
* **Novo**: O processo foi criado e aguarda a alocação de recursos.
* **Pronto**: O processo está apto a ser executado, aguardando pela CPU.
* **Executando**: Sendo executado na CPU.
* **Bloqueado**: O processo aguarda um evento externo (como leitura de disco).
* **Finalizado**: O processo terminou e seus recursos foram liberados.
* Um processo não fica parado, ele está constantemente mudando de estado, e isso é chamado de transições de estado.

#### Escalonamento
* É a política usada pelo SO para escolher qual processo ou thread vai usar a CPU.
* O scheduler decide qual processo, baseando-se na política (algoritmos) de escalonamento definidos pelo SO.
  * Dentre eles:
    * FCFS (First Come, First Served)
      * Quem chega primeiro é quem executa.
      * Processo longo pode travar todos os outros.
    * SJF (Shortest Job First)
      * Executa primeiro o processo mais curto.
      * Precisa saber o tempo antes, e processos grandes podem ficar esperando demais.
    * Por prioridade 
      * Executa aquele que tem maior prioridade.
      * Processos de baixa prioridade podem nunca rodar.
    * Round Robin
      * Cada processo recebe um quantum (tempo que o processo pode usar a CPU), e roda por um tempo fixo, caso não terminar, volta pra fila.
      * Muita troca de contexto se o quantum for pequeno.
    * Multilevel Queue
      * Divide processos em várias filas, com regras diferentes.
      * Cada fila pode ter o seu próprio algoritmo.
      * Mais complexo.
* Overhead é o custo de organizar tudo,
* Aging é a técnica para evitar que processos fiquem esquecidos na fila.
* Starvation é aquele processo que nunca executa.
  * Pode ser resolvido usando aging, pois existe um aumento gradual de prioridade.
* Context Switch refere-se a troca de processos na CPU.
* Throughput é a produtividade da CPU.
* Turnaround Time é o tempo total do processo.
* Os dois grandes grupos de tipos de escalonamento seriam
  * Não Preemptivos: O processo continua usando a CPU até terminar ou bloquear.
  * Preemptivos: O SO pode retirar a CPU de um processo.

#### Comunicação entre Processos
* Processos são isolados por segurança, por isso o SO disponibiliza o IPC para permitir cooperação, sincronização e troca de dados.
* Cada processo tem a sua memória e não acessa o outro diretamente.
* Alguns exemplos seriam as comunicações via fluxo, como Pipe, Socket e Fila de Mensagens, ou via memória, como a memória compartilhada, semáforo ou sinal.

#### Troca de Contexto
* O contexto como já visto, é o estado atual do processo.
* Pode ser separado em 3 partes
  * Salvar: A CPU para de executar o processo e salva todos os registradores, PC e Stack Pointers no PCB.
  * Interrupção: O escalonador receber o controle e decide qual processo entra a seguir.
  * Carregar: O escalonador aponta para o PCB do processo a ser executado, e a CPU carrega esses valores e retoma a execução exatamente de onde tinha parado.

### Threads
* Dentro de um processo, uma thread é um fluxo de execução, que geralmente roda na CPU.
* Seria uma tarefa dentro do processo, que pode rodar de forma independente, mas compartilhando os mesmos recursos do processo pai.
  * Compartilham a memória, mas tem sua própria execução.
* Seria a execução do processo.
* Todas as threads usam o mesmo código e podem acessar as mesmas variáveis.
  * Mas cada uma tem suas próprias stacks e registradores.
  * Pois cada thread precisa controlar a sua execução e guardar as suas chamadas de função.

#### Execução Concorrente
* Thread permitem que várias tarefas avancem ao mesmo tempo, alterando o uso da CPU.
* O SO alterna entre elas rapidamente com o escalonamento, criando a sensação de simultaneidade.
  * Porém em CPU com múltiplos núcleos, pode realmente ser paralelo.
* Paralelismo só existe se o processador for multi-core.
  * Dessa forma cada thread roda ao mesmo tempo em núcleos diferentes.
* Em resumo, concorrência seria alterar rápido, e paralelismo rodar ao mesmo tempo em diferentes núcleos.

#### Gerenciamento de Threads
* A thread é criada dentro do processo.
* O SO decide (escalonamento) qual thread vai rodar, e por quanto tempo.
* Troca o contexto ao pausar uma thread para continuar outra pelo estado do PCB.
* Sincroniza controlando o acesso a recursos compartilhados (isso faz com que não haja conflitos).

#### Problemas de Concorrência
* Caso várias threads acessam o mesmo dado, alguns erros podem aparecer.
* **Race Condition**: Resultado depende da ordem de execução.
* **Dados Inconsistentes**: Valores podem ficar errados.
* **Conflito de Acesso**: Duas threads modificam o mesmo dados.
* **Deadlock**: É uma situação em que dois ou mais processos ficam presos esperando uns pelos outros, fazendo com que nenhum consiga continuar (espera circular).
  * Da pra resolver dando prioridade para o primeiro que acessou o recurso.
* A sincronização garante o acesso seguro aos dados.
  * Mutex (Mutual Exclusion): Apenas uma thread por vez.
  * Semáforo: Permite várias threads ao mesmo tempo, mas controla quantas podem acessar o recurso.
  * Lock: Implementação prática do mutex, fazendo com que a thread trave e depois de utilizar o recurso, libere.