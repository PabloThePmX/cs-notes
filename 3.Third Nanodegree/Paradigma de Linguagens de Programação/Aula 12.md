# Aula 12

* O Factory Pattern fala sobre classes com métodos específicos para instanciação de classes, essa instancia é retornada pelo método.
* A injeção de dependência aplica o princípio de inversão de dependência.
* O bean é um componente do spring, que vai ser visto pelo mesmo.
  * Uma classe vira bean com a anotação do spring (RestController, Component, Repository, etc).
* O docker precisa rodar em kernel do Linux.

## Api Gateway
* O cliente sempre vai acessar o gateway, e ele vai fazer o balanceamento de carga entre as instâncias.
* Também é um microsserviço.
* Existe gateways reativas.
  * Libera a thread logo ao enviar, e reabre apenas quando receber a resposta.
  * Ou seja, o reativo é `async` e o outro não.
* Usar a dependência do spring (reactive gateway).
  * O tomcat é síncrono, portanto o reactive gateway não usa ele para ser rodado.
    * Usa o netty.
* Não vai funcionar se o Eureka não estiver rodando, pois não vai conseguir encontrar os serviços.
* Usar a propriedade `spring.cloud.gateway.server.webflux.discovery.locator.enabled=true` para dizer que o gateway vai descobrir as instâncias com o Eureka automaticamente.
  * A propriedade `spring.cloud.gateway.server.webflux.discovery.locator.lower-case-service-id=true` vai dizer que a url não precisa ser em upper case como está na lista do Eureka.
* Para chamar, vai usar a URL do gateway + microsserviço + controller + endpoint.
* Porém, podemos criar uma classe para fazer a configuração desse roteamento, dessa forma, realizando de forma mais lógica (dentro de um package `configs`, colocar uma classe `GatewayConfig`).
* Essa classe é um bean de `Configuration`.
  * A classe vai ter um método que vai retornar uma rota com `RouteLocator`.
  * Esse método vai ser um `@Bean`.
  * O método vai receber um builder `RouteLocatorBuilder`.
  * E vai ser construído dessa forma: `builder.routes().route(x -> x.path(<METODO HTTP, ex.: "/get">).uri(<LINK>)).build();`.
  * Nesse builder da pra colocar filtros, ou seja, mandar `headers`, `params`, etc.
  * No path do builder, colocar `**` após a barra, para dizer que qualquer link daquele caminho (`currency/1/2`) respeite sempre o URI.  
  * Vai encadear todas as rotas nesse mesmo builder, como é feito para as rotas da web.
  * No `uri`, usar o link com `lb` para dizer que vai utilizar o load balance.  
    * Ex.: `uri("lb://<LINK>")`.
  * A uri concatena com a path, ou seja `.path("/products/**").uri("lb://product-service")` transforma para `product-service/products/****`

## Server Side Discovery Pattern
* O servidor vai descobrir quais as instâncias estão rodando.