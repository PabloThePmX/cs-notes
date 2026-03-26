# Aula 3

## Cabos Coaxis
* Usados para transmitir sinais (até 10Gbps)
* Thicknet
* Thinnet
* Par trançado
  * Os cabos azuis (Cat5e).
    * O conector d Cat6 é diferente.
  * A versão "e" é a aprimorada.
* Existem cabos blindados que protegem os fios no chão de fábrica.
  * Usa aterramento para evitar interferências.
* Existem até Cat7 e Cat8.
  * Ambos vão ser sempre blindados por padrão.
  * Cat8 é geralmente reservada para conexões em data centers.
  
## IEEE
* Familia de padrões 802.
  * WI-FI, Ethernet, Bluetooth, etc.
* Padrões de WI-FI 6 e 7.
  
## Ethernet
* Camada enlace.
  * Enlace físico.
* A informação da rede ethernet é enviada em vários frames de bits.
  * Não em um fluxo contínuo.
  * Cada frame possui um header.
    * Bem como um campo de verificação de erros (FCS) para garantir a integridade da informação.
* O header possui:
  * O endereço MAC de destino.
  * O endereço MAC de origem.
  * O tipo da conexão
* Cada dispositivo em uma rede possui um endereço MAC.

## Wireshark
* É um software para visualizar os pacotes da rede.
  * O ncap é usado para pegar os pacotes da rede (sniff).
* Usar `arp-a` para verificar os IPs de cada Interface da máquina.
* O gateway padrão é o IP de saída para a internet.
* `dst` = destino, `src` = source.
* Possui filtragens.
* Usar `arp -d` para limpar a tabela arp (cache).
* O `ping` vai perguntar (who) que está chamando (está na informação da requisição).
* Broadcast em redes, quer dizer que vai ser mandado para todos.