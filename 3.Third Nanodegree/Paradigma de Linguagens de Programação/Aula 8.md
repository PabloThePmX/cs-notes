# Aula 8

* Da pra injetar uma classe via construtor ou ousando a anotação `@Autowired`.
  * É recomendável fazer via construtor, para poder ter maior controle e declarar o atributo como `final`.
    * Não da pra declarar o atributo como `final` usando o `@Autowired` pois a alimentação é feita após a criação, enquanto se for usando o construtor, ele vai injetar "antes" de criar esse atributo final.
* Ao colocar uma anotação, vamos dizer ao spring que ele é responsável pela instanciação do objeto e seu ciclo de vida.
* As classes com anotações (component, controller, etc), são `beans` do spring. 
* No `JRE` presente no projeto, da pra alterar o jdk.

## Observabilidade
* É um padrão para acompanhar o estado de cada microsserviço.
* Usar a dependência `Spring Boot Actuator`.
  * Da pra colocar no `pom.xml` ou adicionar como starter do spring boot.
    * Ao fazer pelo `add starter`, precisa fazer um "merge" com o `pom.xml` atual.
  * Ao rodar o microsserviço, a dependência ja vai ser colocada.
* Essa dependência expõe endpoints que contém informações sobre a aplicação.
  * Para acessa-lo, ir no `/actuator`.
    * Para ver se está ativo, ir em `/actuator/help`.
* Usar a configurações:
    ```
    management.endpoints.web.exposure.include=*
    management.endpoint.health.show-details=always
    management.endpoint.env.show-values=always
    ```
  * Dessa forma vai mostrar mais informações (não é recomendável fazer isso em produção).
* Três pilares da observabilidade: métrica, logs e tracers.

## Servidor de Configuração (microsserviço de apoio)
* Usar o `Spring Cloud Config Server`.
* É uma API que os nossos serviços vão buscar usando REST para pegar as configurações.
* Precisa-se usar a anotação `@EnableConfigServer` na classe de entrada, para dizer que é um projeto do tipo servidor de configuração.
* Neste projeto, criar pastas dentro de uma pasta `configs` no `resources`, com pastas para conter as configurações de cada projeto.
  * A pasta do projeto deve ter o nome exatamente igual ao nome do projeto.
* Usar a propriedade `spring.cloud.config.server.native.search-locations=classpath:/configs/{application}` para dizer que o projeto precisa buscar as configurações dentro do projeto config.
* Colocar o `Config Server` na aplicação que vai buscar a configuração.
  * Usar a configuração `spring.config.import=optional:configserver:http://localhost:8888` para dizer de onde ele precisa importar as opções, com o parâmetro opcional para que não de erro caso não encontre.
  * Ele sempre busca também pelo perfil padrão.
* Por padrão ele busca configurações em um repositório do git.
  * Para definir a URI do git, usar a propriedade `spring.cloud.config.server.git.uri` (comentar a propriedade que busca de outro projeto, aquele com o `native`).
    * Da pra definir qual a branch padrão com a propriedade `spring.cloud.config.server.git.default-label`
    * Para definir o local dentro do repositório git, usar a propriedade `spring.cloud.config.server.git.search-paths`, e no local do nome da aplicação, usar a interpolação com `{application}`.
* Seguindo esse padrão do git, podemos colocar outras fontes externas, algumas vão precisar de dependências específicas.