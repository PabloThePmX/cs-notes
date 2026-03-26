# Aula 10

* Se está azul quer dizer que é um diretório.
  * Ou se tem um `d` nas permissões.
* O caminho `~` é o diretório do usuário.
* Duas interfaces de rede, uma com acesso interno e outra com acesso para a internet.

## Comandos
* `mv` usado para renomear ou mover.
* `touch` para criar um arquivo.
* Usar `echo > <ARQUIVO>` para colocar algo no arquivo.
  * Ou acessar com algum editor (como nano e vim).
  * Com o `>>` ele vai colocar ao final do que já existe, ao invés de sobrescrever.
* Para instalar, colocar `sudo apt install <PROGRAMA>`.
* `cat <ARQUIVO> | grep <PALAVRA PARA BUSCAR>` vai buscar por alguma ocorrência no arquivo. 
* Usar a flag `-v` significa que vai ser verboso, ou seja, vai dizer o que fez.
* Usar o `df` para trazer as informações do hard disk.
  * Existem flags para visualizar em Gb e afins.
* Usar o pacote e o comando `tree` para visualizar a árvore de diretórios.
* `rm -rf` para forçar apagar diretórios recursivamente.
  * Usar `rmdir` para apagar diretórios também.
* O `find /` vai buscar em todo o pc, enquanto o `find .` vai buscar no diretório atual.