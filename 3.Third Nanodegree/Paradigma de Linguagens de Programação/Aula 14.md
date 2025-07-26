# Aula 14

* O `spring net` é como se fosse um switch.
  * Ele é a rede que a conecta os containers entre si.

## Maven Wrapper
* Existem comandos de terminal para executar e buildar o projeto.
* Alguns são `mvn clean`, `mvn compile`
* Para empacotar, usar o `mvn package` para criar o pacote, ou `mvn install` para fazer o package e instalar no repositório local.
    * Usar o `mvn deploy` para fazer tudo e depois enviar para o repositório remoto do maven.
* Da pra fazer usando o mvn local, chamando o que está instalado na pasta `.\mvnw`.
  * Ele vai instalar o wrapper primeiro.

## Preparar os arquivos Docker
* Criar a imagem docker na pasta do microsserviço, com o nome `Dockerfile` e sem extensão.
  * O script para o java,
    ```docker
    FROM eclispe-temurin:17-jre-alpine
    VOLUME /tmp
    ARG JAR_FILE=target/*.jar
    COPY ${JAR_FILE} app.jar
    ENTRYPOINT ["java", "-jar", "/app.jar"]
    ```
* Dessa forma, executar o arquivo do docker dentro da pasta.
  * Usar o comando `docker image build -t <nome que desejo usar para imagem>:latest .`
    * O `.` é para dizer que o repositório da imagem está na pasta atual.
* Na pasta raiz de tudo, criar o `docker-compose.yml`.
* O build é quem vai fazer a imagem, e o compose vai executar ela.
  * O compose pode executar o build se for pedido.
* Fazer o `docker compose up --build -d` para subir o arquivo compose e buscar pelos build necessários. 
* Cuidar com propriedades com `localhost`, pois cada serviço vai estar rodando separadamente, portanto, com localhost diferentes.
* O gerenciamento do compose é feito somente com serviços locais.
  * O Kubernates permite fazer o gerenciamento de serviços que estão espalhados em servidores.
* Usar o `docker compose -d --scale <serviço>=3` para dizer a quantidade de instâncias que deverá subir para determinado serviço.
* Usar o `docker image history <serviço>` para ver as camadas da imagem.
* Da pra compilar no momento da criação da imagem.
  * Colocar o comando do Maven.