# Aula 5

* CIDR
  * Serve para que não haja uma discrepância tão grande entre os IPs possíveis para ser utilizados.
* VLSM
  * Máscaras de tamanho variável.
  * Octetos não são cheios.
  * Sub-redes.
* O `/` fala dos primeiros bits, e quais vão representar a rede.
* Para saber a quantidade de hosts, fazer a potencia do que sobra dos bits, ou seja `/29` quer dizer que 3 bits podem ser usados como host.
* Para calcular o número de sub-redes, fazer o mesmo que do host, mas com os bits de rede.
  * Porém so usa no cálculo o octeto que não é rede nem host (o quebrado).
* Broadcast sempre em ímpar, e endereço de rede sempre par.
* O range começa do endereço de rede até o broadcast (sem contar ambos valores).
* Menos que `/8` não existe.
* Da pra so converter em binário, aquele octeto que está quebrado e os hosts.
  * Teoricamente o primeiro octeto nunca vai mudar.
* Se preocupa apenas com a parte quebrada.
  * E o que é rede não muda, apenas a parte que é host.
    * E a rede vai ser o valor que sobra do octeto quebrado (e a parte de host fica 0).
      * E o broadcast vai ser o que sobra do host somado ao máximo.
        * Ou seja, se sobra 0000, o broadcast vai ser 1111.
* Endereço de rede é o "primeiro" IP e o broadcast seria o final.
  * O meio disso seria o range.

## Exemplo
* 192.168.5.14/21
  * 21 bits para a rede
  * 11 bits para host
  * 192.168 inalterados
  * O octeto alterado: 5 = 00000101 = 00000|101
  * Rede: 192.168.0.0 (pega o valor da rede que foi quebrado)
  * Broadcast: 192.168.7.255 (maximiza o valor do host que foi sobrado)