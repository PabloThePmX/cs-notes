# Aula 3

## Sockets
* São pontos de extremidade de um canal de comunicação bidirecional entre dois programas.
* Permite a troca de dados entre aplicações.
* São fundamentais para aplicações de rede.
* Fluxo de comunicação
  * socket(): Cria um objeto socket TCP/IP.
  * bind(): Associa o socket a um endereço IP e porta
  * listen(): Coloca o socket em modo de escuta.
  * accept(): aceita conexões.
* Em python:
  * Cria o socket com `socket.socket(AF_INET, SOCK_STREAM)`.
  * Conecta ao servidor com `socket.connect(HOST, PORT)`.
    * Bloqueia a execução até que a conexão seja estabelecida ou falhe.
  * Troca de dados com `send()` e `recv()`.
* Porém sendo síncrono, é possível existir apenas um cliente por vez.

## Sockets Assíncronos
* Gerenciamento de conexões em um único thread.
* Event loop coordena todas as operações de I/O.
* Precisa usar o `asyncio`.
* Reader e Writer são abstrações de alto nível que simplificam operações de I/O assíncronas