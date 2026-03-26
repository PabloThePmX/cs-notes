# Aula 7

* Lembrar do modelo hibrido, e o que engloba a camada de aplicação.
* Enlace tem o ethernet.
* IP tem tempo de vida.
* Usar o comando `ipconfig /release`.

## DHCP
* Dynamic Host Configuration Protocol
* É responsável por atribuir IPs de forma dinâmica.
* Possui 4 etapas
  * `DHCPDISCOVER`: Dispositivo envia mensagem para encontrar um servidor DHCP.
  * `DHCPOFFER`: Servidor oferece um endereço IP ao dispositivo.
  * `DCHPREQUEST`: Dispositivo aceita o endereço IP.
  * `DHCPACK`: Servidor configura a atribuição do endereço IP.
* É um protocolo que não tem segurança.

## DNS
* O DNS serve para transformar o IP em um nome e vice versa.
* Quatro tipos
  * Recursivo.
  * Autoritativo.
  * Servidor DNS raiz.
  * 
* `nslookup <URL>`
  * Usar `nslookuo -type=A <URL> <DNS>` para ver apenas os DNS tipo A.
* Roda na porta UDP 53.
* `PTR`: Ponteiro. 

## Principais Protocolos na Camada de Aplicação
* Telnet na porta TCP 23.
  * Usa para ver se as portas estão abertas.
  * Não é seguro.
  * Existe outras ferramentas.
* SSH (Secure Shell) na porta TCP 22.
  * Usa para conexão segura.
  * Uma versão segura do telnet.
* RDP na porta TCP 3389.
  * Remote Desktop Protocol.
* FTP na porta 20 (dados) e 21 (controle).
  * Não é seguro.
* SFTP
* SMTP
* POP3 e IMAP.
  * Para ler o email em si.
  * Suportam criptografia.
* HTTP na porta 80.
  * Trabalha em toda a camada de apresentação (por esse motivo a apresentação geralmente é tudo junto assim).
  * Está no HTTP/3 mas muitos ainda usam o HTTP/2.
