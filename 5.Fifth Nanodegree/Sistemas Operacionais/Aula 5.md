# Aula 5

## Docker

* Antes os apps rodavam diretamente no servidor físico.
* Se um app consumisse muito, daria problema nos outros, visto que todos estava no mesmo SO.
  * Não havia alocação de recursos para cada aplicação.
  * Dava pra escalar o número de servidores, um app para cada app, mas era muito caro.
* Desse problema, surgiu as máquinas virtuais.
  * Que permitiram isolar cada aplicação em cada SO.

### Como funciona o Docker
* Cria containers isolados uns dos outros.
  * Dentro deles tem as aplicações e suas dependências.
* Usa a Docker Engine.
* Usa o mesmo kernel (do host) para todos os containers.
  * Portanto não da pra usar containers de kernel windows no kernel linux e vice-versa.
  * De tal maneira, compartilha o SO, drivers e CPU.
* Separado em 3 etapas:
  * Client, Docker Host e Registry.

#### Client
* Os comandos que o usuário usa para manipular o docker.
* Alguns exemplos seriam `docker run`, `docker build` e `docker pull`.
* Todo digitado vai para o Daemon. 

#### Docker Host
* O cérebro do docker.
* Recebe os comando do cliente e decide o que vai ser feito.
* Gerencia imagens e containers.
  * As imagens são os modelos prontos de aplicação.
  * Os containers são as instâncias rodando de uma imagem.

#### Registry
* É o repositório de imagens.

### Comandos Básicos
* `docker run`: Verifica se a imagem existe localmente, se não existe, faz o pull, e depois inicia o container.
* `docker build`: Monta o dockerfile em uma imagem e salva ela localmente.
* `docker pull`: Baixa a imagem do repositório.