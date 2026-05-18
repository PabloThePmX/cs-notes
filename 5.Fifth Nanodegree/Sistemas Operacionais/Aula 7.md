# Aula 7

## Docker Compose
* É uma ferramenta que permite definir e executar múltiplos containers dockers.
  * A partir de um único arquivo de configuração `docker-compose.yml`.
* Da pra descrever toda a infra em um único arquivo, e subir tudo usando `docker compose up`.
  * Para subir em background `docker compose up -d`.
  * Para subir reconstruindo todas as imagens `docker compose up --build`.
    * Tem que sempre usar caso ocorreu uma mudança.
  * Usar `docker compose stop` para parar, e `docker compose down` para parar e remover.
* Para ver o status dos serviços, usar `docker compose ps`.
* Para rebuildar as imagens sem subir, usar `docker compose build`. 
* O `dockerfile` e `docker-compose` são complementares um dos outros.
  * O `dockerfile` define como construir/montar uma imagem.
    * Um único serviço.
  * O `docker-compose` orquestra diversos containers (como deverá subir toda a aplicação).
    * Toda a aplicação (vários serviços).
* O docker compose é bom para uma aplicação inteira, com dependências de banco de dados, cache, filas, etc.
* Da pra ter um compose para produção, dev, etc.

### Anatomia de um arquivo compose
* A primeira seção é a versão do arquivo (`version`) - opcional.
* Depois os serviços (`services`) - obrigatório.
  * Cada filho é um container.
  * Colocar o nome, e esse nome vai ser o hostname na rede.
  * Portas, `.env`, volumes do serviço, políticas de restart, etc.
    * As variáveis de ambiente podem ser setadas no arquivo ou chamar de arquivos separados (melhor prática).
      * Ai então buscar elas de lá, para colocar no compose.
* Os volumes persistentes globais (`volumes`) - opcional.
* E por fim as redes personalizadas (`network`) - opcional.
  * Aqui vai cria-las, e elas serão definidas no serviço em si.
* Usar o `build` para os serviços de `dockerfile` local (ao invés de `image`, para imagens oficiais).
* As portas são definidas pelo padrão `HOST:CONTAINER`.
* Da pra dizer quais as redes podem acessar quais serviços.
* O `depends_on` garante a ordem do start.
  * Mas é recomendado usar o `healthcheck` para ver se já está rodando.
  * Coloca o nome do serviço dependente.
* O `command` no serviço sobrescreve o comando padrão da imagem.
* O `profile` agrupa serviços, e é possível definir quando cada profile vai ser subido.
* Para usar uma variável do ENV, usar `${NOME_VAR}`.