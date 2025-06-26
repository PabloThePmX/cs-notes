# Aula 13

* Hypervisior é um software que permite criar virtualizações de várias máquinas virtuais.
* O VirtualBox virtualiza uma maquina virtual em cima de um SO.
* Bare metal é o termo usado para quando existe uma virtualização diretamente no servidor, sem que exista um SO no meio disso.

## Docker
* Sistema de virtualização baseado em software.
  * Roda em cima do Linux, e a partir dele cria containers.
  * A única coisa que todos compartilham é o Kernel, que por sua vez, é separado por namespaces.
* Inicialmente baseado em LXC (Linux containers).
* Escrito em GO.
* O host e os containers compartilham o kernel.
* Funciona do mesmo princípio que a virtualização de máquina virtual, isolando cada container.
* Ele usa as imagens Docker.
  * São um arquivo somente leitura para criar containers.
  * São armazenados em repositórios de Registry (DockerHub, tipo um github).
    * Tem imagens verificadas/oficiais.
* Da pra rodar microsserviços.
  * Kubernetes é um orquestrador de containers.
  * No docker, existe o `docker compose`.
* Tem sub redes internas, que se conversam, e que as vezes limitam o acesso apenas dentro delas (sem expor portas, ou apenas expor de um container, tipo um api gateway).
  * Da pra acessar terminais dentro dessas redes.
  * Os containers vão ser "máquinas separadas".
  * Usa DNS, olhando pelo nome do container.
    * E internamente se criam IPs.

### Docker Compose
* Geralmente se usa quando é uma aplicação pequena, etc, em outros casos é melhor usar o Kubernetes, para organizá-los.
* Permite que containers sejam "juntados".
* Usar o nome `docker-compose.yml` (precisa ser exatamente esse nome).
* O `.yml` precisa estar com identação correta.
* Nele vai ter os volumes e os serviços.
* Usar o comando `sudo docker compose up` na pasta do compose para executa-lo, usar a flag `-d` para colocar no background. 
  * Usar o `down` para remover os containers
    * Mas vai deixar o volume com os dados salvos.
* O `stats` vai mostrar como o compose está rodando e o que está consumindo.

#### Services
* Precisa definir coisas como, imagem (com a versão, pois sem, ele busca a última), nome, os volumes, a porta e um comando para rodar ao inicializar o container.
* Da pra dizer que o serviço é dependente de outro, ou seja, so vai inciar se o outro funcionar corretamente. 
* Os volumes podem ser read-only, com o parâmetro `:ro` no final do caminho.


## Docker em Linux
* Executar usando o `sudo docker`.
* Para executar um container, colocar `sudo docker run container run <NOME>`.
  * Se não existe a imagem localmente, ele vai fazer um `pull` para pegar do repositório padrão e baixar a imagem, criando-o e executando-o.
* Para lidar com container, usar o `docker container`, para imagens, `docker image` (usar o `ls` para listar).
* O comando `run` cria um container.
  * Os containers podem ter nomes customizados, ou aleatórios.
* Para realizar ações no container, usar o nome ou o id.
  * Da pra usar apenas o três primeiros dígitos do id.
* Usar a flag `-it` no run para deixar interativo-terminal.
  * Que pode mexer dentro daquele container. 
* Usar o `start -ai <nome container|id>` para executar um container existente.
  * Para parar, usar o `stop`.
* Usar o `--name` para colocar um nome no container.
* Containers podem mostrar logs.
* Usar o `prune` para apagar todos os containers parados.
* Com a flag `-p` podemos mapear uma porta para o container, ou seja `-p 8080:80`.
  * Assim, fica possível chamar esse container por fora do docker, como servidores web (`nginx`).
* Para dizer que vai rodar de background, usar a flag `-d`.
* Para mapear um volume, usar a flag `-v <caminho do arquivo:caminho do arquivo no container>`.
  * Da pra concatenar com o pwd.
  * O volume seria um arquivo/pasta compartilhada entre containers.