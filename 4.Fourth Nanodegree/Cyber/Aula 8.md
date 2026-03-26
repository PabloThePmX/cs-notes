# Aula 8

* A primeira versão do kernel (núcleo) Linux saiu em 1991.
* `Slackware` foi uma das primeiras distribuições.
* `Red hat` é mais focada em sistemas corporativos.
* Começou com UNIX, depois GNU e depois MINIX, e a partir disso saiu o Linux.

## Sistema de arquivos.
* Ext2, Ext3, Ext4, XFS, Btrfs e NTFS.
* Era criada uma pequena partição com um volume NTFS para que dual boots pudessem se comunicar, visto que ambos visualizavam essa partição.
* O Ext2 é o mais antigo, suportando nomes de arquivos até 255 caracteres.
  * Hardwares mais recentes não suportam ele.
* O Ext3 inclui journaling.
* XFS é recomendado para servidores com grandes quantidades de dados.
  * Mais rápido para fazer leitura.
* O Btrfs é mais recente, e é utilizado mais para RAID (trabalhando com mais de um disco físico, espelhando ou criando apenas um lógico).

## Arquitetura de Diretórios
* `/`- Raiz (nível mais alto).
  * Por boas práticas não tem senha.
  * Não tem o `cd ..` pois não tem para onde ir mais acima.
* `/root` - Diretório do administrador do sistema.
* `/home` - Diretório de usuários.
* `/etc` - Diretório de arquivos de configuração.
* `/var` - Diretório de configurações e logs.
* `/opt` - Diretório de pacotes comerciais.
* Não existe o `C:\`.
* O `.` significa onde estou, e o `..` o nível acima (anterior).
* Palavras maiúsculos são variáveis de ambiente.
* `/bin` e `/usr/bin` - Diretório de comandos padrões.
* `/lib` (`lib64`) e `/usr/lib` - Diretório de bibliotecas.
* `/dev` - Diretório onde ficam os dispositivos.
  * Precisa montar depois.
* `/tmp` - Diretório temporário (qualquer usuário tem permissão de escrita nele).
* `user/local/bin` - Diretório usado para pacotes não nativos.
* `/proc` - Diretório para informações do sistema (telemetria).
* `/mnt` - Diretório para montagem de unidades.
* `/sbin` - Diretório usado para admin e controle do sistema.
* `/boot` - Diretório para inicialização do sistema.
* `/usr` - Diretório onde ficam a maior parte dos pacotes. 