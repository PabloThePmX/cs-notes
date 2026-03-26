# Aula 16

## Cisco Packet Tracer.
* Salvar em `.pkt`.
* Da pra configurar um pequeno servidor, com DHCP, DNS, etc.
* Fazer conexões usando o "raio".
* A rede WIFI vai ter uma outra faixa de rede para que aumente o a quantidade de hosts, visto que não vai coincidir com a faixa de IP da rede cabeada.

## Protocolos

### RIP (Protocolo de informações de roteamento)
* Baixa complexidade.
* Indicado para topologias pequenas.
* Feito mais para simulações.
* Tem arquitetura XNS.
* É limitado a 15 saltos (ou seja, passa por 15 roteadores).
* Permite dar continuidade ao pacote de dados, ou seja, ele permite a internet passar.
* Ele escolhe o caminho com menos saltos, mesmo que a velocidade seja pior (isso acaba sendo uma desvantagem).
* Utiliza o serviço de UDP na porta 520.
* Faz o uso de dois tipos de mensagens:
  * De pedido.
  * De resposta.