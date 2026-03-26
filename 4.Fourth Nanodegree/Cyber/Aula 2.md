# Aula 2

* O moden converte sinal digital para analógico.
  * Precisa pois a net discada usava sinais analógicos (pois a telefonia era analógica).
* Modulação e demodulação.
* Access Point: Cria uma rede local sem fio (WLAN) (camada 2).
  * Diferente de roteador wireless (camada 3 e 4).
  * Atua como ponte entre a rede sem fio e com fio.
* Porta SFP no Switch.
  * Usam com transceivers.

## Modelos de Comunicação
* É uma estrutura abstrata que define os elementos e as etapas envolvidas na comunicação.
  * Funciona como se fosse um mapa.
* Padrões IEEE 802.
* PDUs: Protocol Data Unit.
  
### Modelo de Camadas
* Usa interfaces para interligar as camadas.
  * Define o que as camadas entendem.
* Cada camadas precisa ser independente e isolada.
* Existem camadas de serviço (o que a camada vai ser responsável) e protocolo.
  * Entidades pares.
    * Ou seja, o receptor deve ser capaz de ler o que o emissor enviou (entidades pares).
* Usa protocolos de comunicação para se comunicar entre as camadas.
* Informação, formato, sinal e meio físico.
* O protocolo vai definir como a informação vai ser tratada.

### Modelo OSI
* É um modelo conceitual.
* É uma maneira de entender o modelo de camadas.
* Possui 7 camadas de comunicação.
  * São 7 no emissor, e 7 no receptor.
* Camadas:
  * Física: Bits brutos, energia elétrica, etc.
  * Enlace: Switch, endereço mac, etc.
  * Rede: Roteador, pacote, IP.
  * Transporte: TCP e UDP.
    * TCP prioriza a confiabilidade
    * UDP prioriza a velocidade.
  * Aplicação
    * Sessão: Estabelece sessão de início e fim de conexão.
    * Apresentação: Criptografado, compactação, etc.
    * Aplicação: HTTP, SMTP, POP, IMAP, DNS, etc.

### Modelo TCP/IP
* Arquitetura prática que roda nos computadores.
* Possui 5 camadas.
  * Física, enlace, rede (internet), transporte e aplicação.
* DPUs: Messages, Segment, Datagram, Frames e Bits.
* Existe o híbrido que tem 5 camadas.

### Sinais
* Existem frequências visíveis e invisíveis.
* Uma frequência é uma onda completa.
  * Ou seja, quantas vezes é realizada essa onda completa por segundo (quantos ciclos).
* Hertz.
* Corrente alternada é uma corrente que sai do 0 até o máximo e depois faz o negativo disso.
  * OV até 220V, 220V até 0V, 0V até -220V, -220V até 0V.
* Amplitude de onda.
  * A altura da onda.
* AM: Amplitude, vai mais longe, FM: Não tão longe mas tem maior qualidade.
* Sinal digital e analógico.
* O analógico tem uma variação praticamente infinita.
* Sinal digital tem uma variação definida (0 e 1).
* Usa a modulação (e demodulação) para transformar o sinal.

### Tipos de Sinais 
* Pulsos elétricos (cabos metálicos).
* Feixes de Luz (fibra óptica).
* Ondas de rádio (comunicação sem fio).

### Fibra óptica
* A fibra repele a luz.
* Fibra multi módulo e mono módulo.
  * A multi módulo refrai mais a luz.
    * Passa mais feixes por vez.
  * O mono vai mais reto (pois o cano é bem mais fino).
    * Passa praticamente um feixe por vez.
    * Vai bem mais longe.
    * Mais cara.
* Também tem padrão de cores.