# Aula 11

## RFID
* Radio Frequency Identification
* Utilizado com id tags e pequenos textos.
* Usado normalmente para abertura de portões.
* RFID de baixa frequência, alta e ultra alta.
  * Podendo chegar até 12 metros (como o sem parar).
* Para usar na PI, o `MFRC522` é o módulo mais conhecido.
* Possível utilizar nos pinos SPI.
  * Para ativar os pinos, executar o comando `sudo raspi-config`.
    * Isso vai abrir uma UI, nela, navegar até `interfacing options`.
      * Setar como enabled o `P4 SPI` e reiniciar o PI.
* Os pinos do MFRC possuem integração com SCK (23), MOSI (19) e MISO (21).
  * Somente nesses pinos.
  * SCK: Serial Clock
    * Relógio que sincroniza a transferência de dados.
  * MOSI: Master Out Slave In
    * Envia dados da Master para a Slave.
  * MISO: Master In Slave Out
    * Envia dados do Slave para o Master.
* Instalar o `mfrc522` e o `spidev` com o pip.
* No código, declarar o leitor com o `SimpleMFRC522()` que é importado da biblioteca.
  * Para ler a tag, usar o método `read()` na variável com a instanciação do leitor.
    * Alimentar o retorno da leitura, em duas variáveis, uma que será a tag, e outra o texto (que é a informação que o cartão carrega).
      * Para ler somente a tag, usar o método `read_id_no_block()`.