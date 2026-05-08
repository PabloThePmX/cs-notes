# Aula 2

## Processo
* Um processo é um programa em execução que possui um espaço de endereçamento próprio e isolado.
  * Conjunto de registradores da CPU.
  * Contador de programa.
  * Estado atual da execução
  * Recursos alocados pelo SO.
* É uma entidade ativa com estados próprios e recursos dedicados.
* Ele é composto por segmentos de código, dados (variáveis globais), heap (alocação dinâmica) e stack (variáveis locais).
* Seu ciclo de vida consiste em
  * Novo -> Pronto (Aguardando CPU) <-> Executando (Pode ficar aguardando a I/O) -> Terminado
* PCB (Bloco de Controle de Processo)
  * É onde o SO mantém cada processo, armazenando as informações necessárias para poder retoma-lo caso o mesmo processo seja parado/pausado.
  * Contém o estado atual, contador (que diz a próxima instrução), registradores, informações de escalonamento, dados de memória e lista de arquivos abertos.

## Thread
* Uma unidade básica de execução dentro de um processo.
* Compartilha recursos do processo pai, como memória heap e arquivos.
* Possui seu próprio stack.
* Troca de contextos mais eficientes que processos.
* Custo de criação mais baixo pois compartilha recursos.

## Concorrência vs Paralelismo
* A concorrência é a alternância rápida entre tarefas em um único núcleo de processamento.
  * Uma CPU gerencia múltiplas tarefas.
  * Ilusão de simultaneidade.
* Paralelismo é a execução simultânea real em múltiplos núcleos.
  * Múltiplas CPUs trabalham juntas.
  * Simultaneidade verdadeira.
* GIL: Global Interpreter Lock
  * Mecanismo do python que permite apenas uma thread executar o bytecode por vez.
  * Protege a memória do interpretador que não é thread safe.
  * Impede paralelismo real em tarefas intensivas.
  * Liberado durante operações I/O.
  * Simplifica o gerenciamento de memória e evita condições de corrida no interpretador.
* Quando usar Threading ou Multiprocessing
  * Threading
    * Melhor para tarefas de I/O.
    * Requisições de rede, leitura e escrita de arquivos, etc.
    * Threads liberar o GIL durante operações de I/O.
    * Com essa lib, usar o `.join()` para aguardar a thread ser finalizada.
  * Multiprocessing
    * Melhor para tarefas de CPU.
    * Cálculos, processamentos de imagens, IA, etc.
    * Cada processo tem seu próprio GIL.
    * Com essa lib, da pra dizer quantos cores vão ser usados.

## Race Condition
* Ocorre quando threads competem pelo mesmo recurso.
* Quando ambas modificam o mesmo recurso, sem que haja uma sincronização, teremos resultados imprevisíveis.
* Difícil de detectar, pois dependem do timing.
* Ex.: Duas threads alterando o mesmo valor simultaneamente.
* Usar lock ou fila para prevenir esses erros.