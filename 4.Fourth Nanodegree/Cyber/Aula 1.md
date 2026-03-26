# Aula 1

* Ética de anonimato.
* Anel de Giges existe na Internet, sendo VPNs, criptografias, etc.
* As Big Techs devem ser responsabilizadas pelo que é postado em suas redes?
* Uma rede sem senha, não possui criptografia.

## Começo da Rede de Computadores
* Começou com a ARPANET.
  * Foi em resposta ao lançamento do SPUTNIK.
  * Interligava bases militares.
  * Nos anos 80 se dividiu em Internet e Milnet (militar).
* Somente nos anos 80 foi começado a usar o TCP/IP.
* RNP

## Tipos de Redes
* LAN: Local Area Networks
* MAN: Redes metropolitanas
* PAN: Conecta a aparelhos próximos do indivíduo.
* WLAN: Rede local sem fio

## Topologias
* Ponto a ponto: dois aparelhos conectados fisicamente.
* Barramento (Bus): Todos os dispositivos são conectados em um único cabo principal.
  * Usa switch layer 1 (burro)
  * Replica a informação para todos os aparelhos conectados.
* Rede estrela (star): Tem um switch para centralizar.
  * O Switch tem um SO rodando para verificar todas as comunicações.
  * Se existir mais aparelhos com o mesmo endereço MAC na rede, não haverá comunicação (entretanto é muito difícil de ocorrer)
  * Ficam isolados um do outro.
* Rede árvore: Combinação da topologia estrela e barra.
* Anel: Fecha um circuíto de rede.
  * Protocolo token ring da IBM (unidirecional).
  * Hoje são bidirecionais.
  * Mais usado em redes metropolitanas.
* Malha: Um aparelho é conectado diretamente entre todos eles.
  * Mais complexa e robusta.
  * Se comunicam de forma ponto a ponto.
  * WI-FI Mesh

## Tipos de Conexão
* SIMPLEX: Comunicação unidirecional (controle remoto).
* HALF DUPLEX: Podem fluir em ambas direções, mas não simultaneamente (walk talkie).
* FULL DUPLEX: Fluem em ambas as direções simultaneamente.
  * Usa um par de fios para enviar, e o outro par para receber.
    * Ou seja, vai depender do cabo de rede, pois a maioria dos aparelhos suportam o full duplex.