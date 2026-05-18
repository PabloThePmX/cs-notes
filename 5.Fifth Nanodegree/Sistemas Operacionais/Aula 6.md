# Aula 6

## Imagem vs Container
* Uma imagem é um pacote imutável e somente leitura, que contém tudo que a aplicação precisa pra funcionar.
  * Como o SO, runtime, deponências, código e variáveis do sistema.
* Container é uma instância em execução de uma imagem.
  * O ambiente em si, onde roda o código.
* As imagens que são distribuídas/compartilhadas, e não o container.
* Containers são descaráveis.
* A mesma imagem roda em igual em qualquer lugar.
* Em resumo, a imagem é o blueprint usado para instanciar um container.

## Dockerfile
* É um arquivo de texto simples, sem extensão, chamado exatamente de `Dockerfile`.
* Contém uma sequência de instruções que o docker executa para montar a imagem, camada por camada.
* A estrutura básica:
```dockerfile
# comentário
INSTRUÇÃO argumento
INSTRUÇÃO argumento
INSTRUÇÃO argumento
```
* Cada instrução vira uma camada da imagem.

### Como o Docker processa
* Ao executar o `docker build`
  * Le o `dockerfile` de cima para baixo.
  * Para cada instrução, cria uma nova camada.
  * Verifica se já existe cache para aquela camada.
  * Se existir cache e nada mudou, reutiliza.
  * Se algo mudou, reconstrói a camada e todas as seguintes.
  * Ao final, produz a imagem com todas as camadas empilhadas.

### Instruções
* `FROM` é o ponto de partida obrigatório, definindo qual imagem será usada como base.
  * Tudo que já está nessa imagem, estará disponível para as outras.
  * Toda imagem começa com isso.
* `ENV` usado para definir as variáveis de ambiente.
  * `NOMEVARIAVEL=1`.
  * Ficam disponíveis durante o build e quando o container estiver rodando.
* `WORKDIR` é o diretório de trabalho.
  * Todos os comando de copia, run, etc, vão ser executados a partir dessa pasta definida.
  * Se não for definida, o docker cria uma automaticamente.
* `COPY` copia os arquivos do host para a imagem.
  * O `.` é o diretório atual.
  * Não copia arquivos definidos no `.dockerignore`.
* `RUN` usado para executar comandos (de cmd) durante o build da imagem.
  * Cada `run` vira uma layer.
  * Usar `&&` para agrupar comandos.
    * Reduz o tamanho da imagem e quantidades de camadas.
* `EXPOSE` documenta a porta que a aplicação usa.
  * Porém não publica a porta automaticamente, isso é definido na hora da instanciação do container.
* `CMD` comando executado quando o container iniciar.
  * Usar o formato de array.
    * Cada "palavra" é um argumento.
  * Diferente do `run`, isso é usado toda vez que for instanciado o container.
  * Roda em tempo de execução.
  * Da pra usar o `ENTRYPOINT` para definir um comando inicial para os `CMD` seguintes.
* `ARG` argumentos de build.
  * Variáveis disponíveis apenas durante o build.
  * Busca o valor usando `$NomeArgumento`.

## Layers
* Cada instrução do `dockerfile` gera uma camada imutável que fica salva no disco.
* O docker empilha essas camadas para formar a imagem final.
  
### Sistema de Cache
* O docker guarda o resultado de cada imagem em cache.
* Então se a instrução não mudou, o docker usa o cache, e inicializa mais rápido.
* Caso mudou, ele precisa reconstruir a imagem.
* Não é uma boa prática copiar tudo logo no início, pois qualquer arquivo alterado, vai fazer o cache ser invalidado, rodando novamente o run.
* O que muda menos vai no topo.

## Inspecionando Imagens
* Para listar imagens usar o `docker images` ou `docker images ls`.
* Para ver as camadas da imagem `docker history <nome>:<versao>`.
* Inspecionar imagens com `docker inspect <nome>:<versao>`.

## Publicar no DockerHub
* Fazer o login no terminal com `docker login`.
* Criar a tag com o usuário `docker tag <nome>:<versao> <usuario>/<nome>:<versao>`.
* Publicar com o `docker push <nome>:<tag>`.
* Usar o pull para baixar.