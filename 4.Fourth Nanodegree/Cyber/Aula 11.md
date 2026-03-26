# Aula 11

* Criar uma rede interna visível somente pro VirtualBox.
  * Ai habilitar a mesma no `.yaml` dentro da pasta `netplan`.
    * E depois rodar `netplan apply`.
* Instalar o `iputils-ping` para conseguir executar o comando de ping.
* Para mudar a data, usar o comando `date`, com o mês, dia, hora, minuto e ano como ordem.
* Usar `laodkeys` para mudar o idioma do teclado.
* Para pegar log do sistema, instalar o pacote `rsyslog`.
  * Depois fazer um `tail` no `syslog`.
  * No `.conf` (`50-default.conf`), retirar a linha de `INFO`.
  * Tem o `status`, `restart`, etc.
* Para fazer que um programa execute na inicialização do SO, executar o comando `systemctl enable <APLICACAO>`.
* Instalar o `chrony`.
* Usar o `ip route list` para ver os IPs.