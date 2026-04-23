# Aula 2

## Virtualização
* Hypervisor é o software que cria e gerencia as VMs.
* A virtualização é a tecnologia que permite simular vários computadores dentro de um único computador físico.
* Uma VM tem uma CPU, RAM, disco e placa de rede virtuais.
* Mesmo sendo virtual, o SO acredita que é um computador real.
* O hypervisor controla o acesso das VMs aos recursos de hardware.
* O hypervisor "engana" o SO guest (aquele que está sendo simulado) usando uma camada de abstração de hardware.
  * Ou seja, a VM acha que está falando com o hardware, quando na verdade está se comunicando com essa camada extra.
  * Essa camada extra traduz tudo para o hardware físico.
* Ao configurar
  * Nunca ultrapassar os 50% de RAM do host e nunca usar todos os cores da máquina do host.
* Alguns exemplos de hypervisors: Hyper-V (tipo 1), VirtualBox (tipo 2) e VmWare (tipo 1 e 2).

### Tipos de Hypervisor
* Tipo 1 (Bare-Metal)
  * Roda diretamente no hardware.
  * Não precisa de um SO intermediário.
  * Maior performance.
  * Mais usado em datacenters e servidores.

* Tipo 2 (Hosted)
  * Roda como um programa dentro do SO.
  * Mais simples de instalar.
  * VirtualBox é o maior exemplo desse tipo.
  * Cria uma camada virtual acima do SO.

### Disco Virtual
* Dinamicamente alocado
  * Cresce com o uso, sendo mais eficiente.
  * Ou seja, não ocupa todo o espaço desde o início.

* Fixo
  * Reserva todo o espaço no host, mesmo que a VM não utilize tudo.
  * Pode ser um pouco mais rápido.

### Modos de Rede no VirtualBox
* NAT (Padrão)
  * O VirtualBox compartilha a internet do host.
  * Outros computadores da rede não enxergam a VM.
* Bridge
  * A VM ganha um IP próprio, virando um computador normal na rede.
* Rede Interna
  * VMs conversam entre si, mas sem acesso à internet.
  * Ideal para simular redes privadas.

### Snapshots
* São usados para salvar um estado de uma VM.
* Permite que seja possível restaurar esses estado posteriormente.
* Muito útil para versionar antes de atualizar servidores em produção.