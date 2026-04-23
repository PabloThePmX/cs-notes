# Aula 1

## Sistemas Operacionais
* O SO age como um software intermediário entre o hardware e os aplicativos do computador.
* Gerencia recursos computacionais e fornece serviços essenciais para a execução de processos.

### Kernel
* É o coração do SO, gerencia a CPU, memória e hardware, e é a ponte entre o software e o hardware.
* Roda com privilégio máximo (modo kernel) e é o único que acessa diretamente o hardware.

#### Modos de Operação
* Existe o modo usuário e o modo kernel.
* Se o computador estiver travando ou reiniciando, é kernel (pode ser um driver ou hardware danificado), mas se apenas um aplicativo estiver travando, é no modo usuário.

* **Usuário**
  * Separado entre aplicação, kernel e hardware
  * Tem acesso restrito ao hardware (sem acesso direto a memória, processador, etc).
  * Se precisar interagir com o hardware, precisa pedir autorização usando System Calls.
  * Se algo falhar, não compromete o funcionamento do sistema.

* **Kernel**
  * Separado em vários anéis de privilégios, sendo eles camadas de drivers e aplicativos.
  * Controle total sobre o hardware.
  * Executa operações críticas para o funcionamento do sistema.
  * Qualquer erro grave no kernel pode travar ou reiniciar o computador.

#### System Calls
* São as as chamadas que fazem a ponte entre os aplicativos e o kernel.
  * Sempre que o usuário precisar usar algum recurso do hardware, ele faz uma system call.
* Parecida com uma API, mas funciona em uma camada diferente.
  * A API é mais alto nível.
* Permite que apenas ações seguras sejam executadas.
* Interrompe processos que tentam acessar recursos não permitidos.
* Ao salvar um arquivo, o editor de texto não tem acesso ao disco, portanto ele faz uma system call para que o kernel grave no sistema.

#### Tipos de Kernel
* Existem 3 tipos de Kernel

* **Monolítico**
  * Todos os serviços do sistema estão no kernel.
  * É mais rápido pois existem menos trocas de contexto.
  * Qualquer erro pode derrubar o sistema.
  
* **Microkernel**
  * Apenas as funções essenciais ficam no kernel.
  * Serviços como drivers rodam separadamente.
  * É mais seguro, mas pode ser mais lento.

* **Híbrido**
  * Mistura entre o monolítico e o microkernel.
  * Usado pelo Windows, macOS.

### Gerenciador de Processos
* Cria, pausa e agenda processos, distribuindo o tempo de CPU entre as aplicações.
* **PCB**: Bloco de Controle de Processo.
  * Estrutura de dados que armazena o estado de cada processo: registradores, PID, prioridade e ponteiros de memória.
* Threads e Processos.
* **Escalonamento** (Scheduling): Algoritmo que decide qual processo usa a CPU (Round-Robin, FIFO, etc).

* Estados de um processo:
  * Novo: O processo foi criado e aguarda a alocação de recursos.
  * Pronto: O processo está apto a ser executado, aguardando pela CPU.
  * Executando: Sendo executado na CPU.
  * Bloqueado: O processo aguarda um evento externo (como leitura de disco).
  * Finalizado: O processo terminou e seus recursos foram liberados.

### Gerenciador de Memória
* Controla o uso da memória RAM e memória virtual, alocando e desalocando espaço para os processos.
* **Memória Virtual**: O SO usa o disco como uma RAM extra, permitindo rodar programas que demandam mais memória que o disponível (porém é mais lento).
  * A movimentação de dados entre a RAM e o disco é chamada de swapping.
  * Basicamente uma extensão da RAM.
* **Paginação**: A memoria é dividida em blocos de tamanho fixo chamado páginas.
  * Primeiramente a memória do programa é dividida em páginas.
  * Depois a RAM é dividida em frames do mesmo tamanho.
  * O SO então coloca cada página do programa em qualquer frame disponível.
  * Uma tabela de páginas guarda onde cada página está na memória.
  * Basicamente essa funcionalidade permite que um programa seja dividido em partes e armazenado em qualquer lugar da memória.
* **Segmentação**: Divide a memória em partes lógicas: código, dados e pilha. 
  * Diferente da paginação, a divisão é de tamanho variável.
  * O código contém as instruções do programa.
  * Os dados são as variáveis globais.
  * Heap é a memória alocada dinamicamente (em tempo de execução).
  * A stack é a chamada de funções.
  * Como funciona:
    * O programa é dividido em segmentos lógicos.
    * Cada segmento pode ter tamanhos diferentes.
    * O SO coloca cada segmento em algum lugar da RAM.
    * Uma tabela de segmentos guarda o endereço e tamanho de cada um.
* **Thrashing**: Quando a RAM está tão cheia que o SO passa mais tempo movendo dados entra a RAM e disco, do que executando os processos.

### Sistemas de Arquivos
* Organiza, armazena, recupera e protege arquivos em dispositivos de armazenamento.
* Cada SO pode ter o seu sistema de arquivos, sendo alguns deles:
  * **NTFS**: Usado no Windows, possui Journaling, permissões de segurança e suporte a grandes arquivos.
  * **ext4**: Usado no Linux, possui inodes, journaling e é muito estável.
  * **APFS**: Usado por dispositivos Apple e possui criptografia nativa.
  * **FAT32**: Usado universalmente por pendrives antigos, e possui um limite de 4GB por arquivo.
  * **exFAT**: Usado universalmente por pendrives e cartões SD, suporta arquivos grandes e é ideal para dispositivos removíveis.
* Inodes: Estrutura que armazena metadados do arquivo como dono, permissões, datas e localizações dos blocos no disco.
* Journaling: Registro de transações pendentes, ou seja, mesmo se o sistema falhar, ainda é possível recuperar o(s) arquivo(s) sem corrupção de dados.

### Gerenciados de E/S (Entrada e Saída)
* Gerencia a comunicação com dispositivos periféricos.
* Os drivers são softwares que traduzem comandos genéricos do SO para comandos específicos de cada dispositivo.
* Buffer e Cache: O SO usa memória como buffer intermediário para suavizar diferenças entre CPU e dispositivos lentos.
* Sync vs Async: Na operação síncrona o processo espera a operação terminar, enquanto na assíncrona o processo continua e é notificado quando terminar (callback/interrupt).
* DMA (Direct Memory Access): Permite que dispositivos transfiram dados diretamente para a RAM, sem passar pela CPU, liberando assim o processador.

### Tipos de SO

#### Tempo Real (RTOS)
* Projetado para responder a eventos dentro de prazos rigorosos (deadlines). 
* Tempo de resposta é garantido e previsível.
* O sistema ABS de carro é RTOS, bem como a aviação, robótica, dispositivos médicos, etc.
* Hard Real-Time: Falhar o prazo é crítico, como em um marca passo, ABS, etc.
* Soft Real-Time: Atrasos degradam a qualidade mas não é catastrófico.
* Basicamente, a resposta deve ser garantida.

#### Monousuário Monotarefa
* Suporta apenas um usuário por vez, e executa apenas uma tarefa de cada vez, ou seja, simples e direto.
* O MS-DOS é um grande exemplo disso, mas ainda é usado em microprocessadores simples sem kernel.
* Sem proteção de memória entre processos, visto que existe apenas um.
* Um processo roda até terminar ou ceder.

#### Monousuário Multitarefa
* Suporta apenas um usuário logado, mas permite executar várias tarefas simultaneamente.
* Processos isolados entre si.
* A GUI roda em paralelo com aplicações.
* O Windows, macOS e Android são exemplos disso.
* Pode executar VMs simultaneamente.

#### Multiusuário
* Permite que vários usuários utilizem o sistema simultaneamente, com isolamento total entre sessões.
* Cada usuário vê apenas seus recursos.
* Sessões concorrentes via SSH ou RDP (Área de Trabalho Remota).
* Auditoria: todo acesso pode ser rastreado pelo usuário.
* São exemplos disso o Linux (vários SSHs) e o Windows Server.

#### Distribuído
* O SO gerencia um conjunto de computadores independentes que se apresentam ao usuário como um único sistema.
* Na prática seria como o Kubernetes.
* O usuário não sabe em qual máquina o processo roda.
* Tolerância a falhas, pois se uma cai, outra assume.
* Possível adicionar máquinas para aumentar a capacidade.
* Possui desafios como consistência de dados, latência e sincronização de relógios.
* Netflix pode ser considerado um sistema distribuído.

#### Redes
* SOs com recursos nativos para gerenciar redes de computadores e compartilhar recursos.
* Possui serviços de DNS, DHCP, NFS, Samba, FTP e HTTP integrados.
* Gerenciamento centralizado de usuários com Active Directory (LDAP).
* Monitoramento e segurança de rede.
* Exemplos como o Windows Server, Ubuntu Server, RHEL (Red Hat) e Debian.
* Maquinas permanecem independentes, apenas compartilham recursos entre si (diferente do distribuído).

#### Embarcados
* SO projetado para hardware dedicado com recursos limitados, otimizados para uma função específica.
* Geralmente o SO é armazenado em memória não volátil (que retém dados).
* Sem GUI.
* Pode rodar com pouquíssima memória.
* Usado em Smart TV, câmeras, sensores IoT, etc.

#### Móveis
* SO otimizado para dispositivos móveis: tela touch, bateria limitada, sensores e conectividade limitada.
* Gerenciamento agressivo de energia, colocando apps suspenso em background.
* Cada APP funciona de forma isolada, sem acesso ao sistema caso não tenha permissão.
* APIs para sensores.
* Exemplos com Android (Linux + ART), iOS (Darwin/XNU), HarmonyOS.
* Desafios únicos, com conectividade intermitente e diversidade de hardware.

