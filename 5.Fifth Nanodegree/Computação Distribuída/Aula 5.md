# Aula 5

## Processos
* É um tipo de atividade
* Se comunica com outros processos usando APIs
* O processador único usa um algoritmo de escalonamento para separar os processos.

## Sockets
* Forma de comunicação entre processos, usando endpoints.
* O ciclo de vida de um socket usa a arquitetura cliente servidor.
  * **Servidor**: socket, blind, listen, accept.
  * **Cliente**: socket, connect.
  * **Comunicação**: send, recv, seguido de close.
* Usa o Three Way Handshake como outras requisições.

## WebSockets
* Comunicação interativa bidirecional (full-duplex).
* Conexão continua com o navegador
* Abre o canal com um handshake, e um dos lados vai ser responsável por fecha-lo depois.
  * No HTTP só tem uma requisição e uma resposta, enquanto o socket fica com a conexão aberta para comunicação.
* Possível usar a framework `Tornado` no python.
* O tornado é uma framework assíncrona para desenvolvimento de aplicações web e serviços de backend, com suporte nativo a websockets.
  * Vai ter uma função para abrir a conexão, para fechar, e para receber a mensagem.
    * Essas funções que serão chamadas via conexão com o websocket no cliente.
  * Cada página vai ter o seu handler.