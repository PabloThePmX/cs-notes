# Aula 9

* `Sudo`: Super User Do.
  * Qualquer ação que eu for realizar, vai ser feita com maiores privilégios.
* Linux não tem executáveis, apenas binários. 
* Usuário de serviço são os usuários criados para cada serviço, ou seja, usado apenas para rodar aquele serviço.
* `^` incio de linha e `$` final de linha.
* O `OpenSSH` é o serviço que permite o acesso remoto ao servidor linux.
  * Tem a chave SSH também.
* No início (após instalar), usar o `sudo apt update && sudo apt upgrade` para verificar os repositórios e instalar atualizações para os pacotes presentes na máquina.
  * O `apt update` apenas verifica se existem pacotes para ser atualizados, sem atualiza-los.
  * Enquanto o `apt upgrade` atualiza.  
  * Sem nada vai fazer de tudo, porém da pra especificar algum aplicativo específico para realizar essa atualização.

## Comandos
* `ls -a` - Vai mostrar os diretórios ocultos (com o `.` na frente deixa oculto).
  * `ls -la` - Aparece os arquivos em lista.
* `cp` - Copia arquivos de um diretório para outro.
* `rm` - Remove ou renomeia arquivos e diretórios.
* `mkdir` - Cria diretório.
* `find` - Localiza arquivos e/ou diretórios.
* `cat` - Mostra o conteúdo de um arquivo.
  * `tac` - Usado para ler ao contrário (do final até o início). 
* `file` - Diz qual o tipo do arquivo.
* `vim` || `joe` (não existe mais) || `nano` - Editores de texto.
* `top` - Gerenciador de processos.
* `ps` - Lista processos.
* `kill` - Encerra processos.  
* `df` - Lista o armazenamento das partições.
* `du` - Lista o tamanho de um diretório.
* `free` - Retorna o tamanho da memória e utilização.
* `locate` - Localiza arquivos ou diretórios.
* `mount` - Lista partições montadas.
* `grep` - Usado para pesquisa de arquivos, diretórios e conteúdo de arquivo (filtrar).  
* `lastlog` - Liga os últimos usuários logados.
* `tail -f` - Lista conteúdos de um arquivo (por padrão as 10 últimas linhas) (continuamente).
* `head` - Mostra as 10 primeiras linhas.
* `date`
* `history` - Histórico de comandos.
* `man` - Mostra a manpage (manual) dos comandos.
* `pwd` - Mostra o diretório atual.

## Gerenciados de pacotes
* `.deb` para distros Debian.
  * `dpkg`, `apt`.
* `.rpm` para Red Hat
  * `dnf`, `aptitude`.