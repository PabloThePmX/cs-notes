# Aula 4

## Virtualização
* Virtualizar memórias, processador, SO, etc.
  * De forma simulada.
* Permite que uma única estrutura física possa ser dividida em várias "máquinas".
* Camada de software fica isolada da camada de hardware.
* VMs são capazes de se comunicar entre si, mas geralmente estão totalmente isoladas uma das outras.
* Um SO não consegue distinguir uma VM de uma máquina física.
* A virtualização mais comum é a de servidores.
  * Sai de 1:1, para 1:N, onde um servidor físico, pode ser vários servidores virtuais.
* Usa o Hypervisor (software) para virtualizar.
  * É uma camada de software instalada entre o hardware e o SO.
* Virtual Machine Monitor - VMM (outro nome para hypervisor).
* O desempenho e a escalabilidade do hypervisor definem a qualidade da virtualização.
* Temos hypervisors de tipo I (bare metal ou nativo) e II (hosted).
  * Tipo I: Executa no hardware do servidor diretamente, fazendo o controle do hardware e o acesso do SO guest sem necessitar da ajuda de um SO host.
    * Ou seja, não precisa de um SO entre a VM e o hardware.
    * Usado em servidores que usam maior processamento e exigem mais segurança.
    * Exemplos como o Microsoft Hyper-V e Citrix.
  * Tipo II: A aplicação é responsável por fornecer o ambiente de execução para outras aplicações.
    * Ele é executado em um SO nativo e não tem acesso direto ao hardware físico.
      * Como uma aplicação, ou seja, o hypervisor fica "em cima" de um SO.
    * Se o SO nativo falhar, vai afetar diretamente a VM.
      * Portanto, é mais recomendado para sistemas de clientes, nos quais a eficiência é menos crítica.
    * Exemplos como VirtualBox e VMware.
  * Ou seja, o Tipo I não precisa de uma SO padrão para funcionar, já o Tipo II, depende de um SO para executar a virtualização.

## Diferença entre Hypervisor e VM
* O hypervisor cria e gerencia as VMs.
* A VM é uma abstração do hardware físico.
* As VMs podem ser executadas simultaneamente.
* O hypervisor é uma nova camada, inexistente em um máquina "comum".