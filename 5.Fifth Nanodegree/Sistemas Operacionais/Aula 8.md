# Aula 8

## Sistemas de Arquivos
* O arquivo possui o conteúdo e metadados.
  * O SO guarda isso em locais separados.
    * Os metadados ficam numa estrutura chamada de `inode`.
  * Os metadados possui as informações do arquivo, como nome, tamanho, permissões, etc.
* O file system interpreta os bytes do arquivo.
* Caminho absoluto: é o endereço completo a partir da raiz.
* Caminho relativo: É a partir de onde você está agora.
  * Já dentro de uma estrutura de pastas.

### Inode
* É a ficha técnica de cada arquivo no disco.
* Guarda o tamanho do arquivo, o dono, as permissões, datas e principalmente onde os dados estão no disco.
* O nome do arquivo não é guardado no inode, é apenas um índice que aponta para o inode.

### Regiões do Disco Rígido
* Superbloco: Informações grais do sistema de arquivos.
* Inodes: Onde ficam armazenados os inodes de todos os arquivos.
* Bitmap: Mapa de quais blocos estão livres ou ocupados.
* Dados: Onde ficam os dados reais dos arquivos.

### Informações Guardadas no Disco
* Existem 3 formas que o SO usa para isso.
* Contígua: O arquivo ocupa blocos seguidos no disco.
  * Rápido para ler, mas cria buracos quando algo é apagado.
  * CD e DVDs.
* Encadeada (FAT): Cada bloco aponta para o próximo.
  * Flexível, mas lento para acessar metade do arquivo.
  * Pendrives e Cartões SD.
* Indexada: O sistema mantém uma estrutura que aponta diretamente para os blocos no arquivo. 
  * Mais rápida e flexível.
  * Linux e Servidores.
* Se der problema, como cair a luz, caso o sistema de arquivos possuir journaling, o problema pode ser evitado, pois ele anota as coisas antes de realiza-las.
  * A maior parte dos sistemas de arquivos modernos possuem journaling.

### Sistemas de Arquivos que Existem Hoje
* FAT32
* exFAT
* NTFS
* ext4
* APFS
* Btrfs

* Ao renomear o nome do arquivo, ele não precisa mover os blocos, por isso é instantâneo.

## Dispositivos de Entrada e Saída (I/O)
* Tudo que permite o computador receber, enviar ou armazenar dados.
* Existem dispositivos que podem ser tanto de entrada ou saída.
  * Como CDs e Pendrives.
* Dentre esses, podemos ser separados como:
  * Dispositivos de Bloco
    * Guardam dados em blocos endereçáveis, como HDs, SDDs, etc.
  * Dispositivos de Caractere
    * Enviam ou recebem dados byte opor byte em sequência, como teclado, mouse, etc.
  * Dispositivos de Rede.
    * Enviam e recebem pacotes de dados, como Ethernet e wi-fi.
* Existem camadas entre o dispositivo e o hardware.
  * Usam-se system calls para chamar as camadas do kernel.
  * Tem um controlador de hardware (chip dentro da placa) que se comunica com o driver.
* O driver é o tradutor entre o SO e o hardware.

### Como a CPU sabe que o dispositivo terminou
* Temos 3 abordagens.
* Pooling
  * A CPU pergunta repetidamente se o dispositivo terminou, aguardando pelo "Sim".
* Interrupção
  * A CPU espera por um sinal elétrico (IRQ), enquanto a CPU vai fazer outra coisa.
* DMA
  * Para grandes volumes de dados, existe um chip dedicado que faz a transferência diretamente sem que a CPU precise ficar sabendo.

### Qual Ordem o HD Atende
* FCFS: Primeiro a chegar.
* SSTF: O mais próximo primeiro.
* SCAN: O elevador.
  * O braço (do HD, SDDs, etc) vai até o fim em uma direção, atendendo tudo e depois volta.
* C-SCAN: Elevador circular.
  * Mesmo que o scan, mas ao chegar o fim, ele volta ao início, sem fazer o caminho de volta.
