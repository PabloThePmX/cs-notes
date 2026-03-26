# Aula 4

* Endereço MAC é sempre a nível físico.
* A parte física é o enlace são quase iguais.
* Enlace tem rodapé.
* LLC e MAC.
  * Controle de enlace lógico e Controle de acesso ao meio.
  * LLC: Gerencia a comunicação de protocolos na camada de rede (3) como ipv4 e ipv6.
  * MAC: Um identificador único atribuído a cada dispositivo de rede.
* O enlace so recebe as informações, mas quem vai entregar é a camada de rede. 

## Camada de Rede
* Protocolos da camada de rede:
  * IPv4 (32 bits)
  * IPv6 (128 bits)
  * ICMP
  * IPX
  * ARP
* O IPv4 ainda é mais usado no mundo.
  * Por causa de sistemas legados.
* A comunicação ou é IPv6 ou IPv4, não é algo que da pra "misturar".

### IPv4
* O IPv4 é dividido em 4 octetos (binários).
  * Ou seja o max é 255.
* O primeiro octeto nunca vai ser 0.
* Uma parte do IP representa a rede e outra o host.
  * Os 2 primeiros octetos identificam a rede, e resto identifica os hosts.
    * Porém varia, as vezes 3 ou 1 octetos representam a rede.
  * Os octetos da rede devem estar iguais para que haja comunicação entre si.
* Um endereço de IP é único.
* Classes:
  * São divididos em 5 classes: A, B, C, D e F
    * As três primeiras são usadas.
  * Dizem como vai funcionar a separação do IP, entre rede e host.
    * Da pra saber a partir dos valores do primeiro octeto.
  * A classe A é a que mais vai poder ter hosts, pois so usa o primeiro octeto para representar a rede.
* O primeiro e último valores decimais não podem ser utilizados (0 e 254).
  * Tirar da rede e do broadcast.
* Hoje a classe é definida pelo valor da mascara de sub-rede.
  * Portanto, a classe da mascara vai dizer qual classe os IPs reais devem seguir para ver se funciona a comunicação.
* Da pra representar o número de octetos usando a barra, ou seja `/24` significa que tem 3 octetos (24 bits) de rede.