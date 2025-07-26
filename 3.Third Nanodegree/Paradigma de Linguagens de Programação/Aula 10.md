# Aula 10

* O microsserviço de configuração é um pattern.

## Comunicação entre Microsserviços
* Temos ambas as comunicações assíncronas e síncronas.
* Através de requisições HTTP ou mensageria (protocolo AMPQ).
  * Dependência `OpenFeign` para se comunicar entre microsserviços via REST, de forma declarativa.
    * Ele seria como uma dependência que facilita o `fetch`, pois além de buscar os valores, vai pegar o json e alimenta-lo nos atributos de uma classe.
* As classes que vão receber a reposta de outro microsserviço, ficam no pacote `clients`.
  * Ou seja, precisa ler o json que recebeu e transforma-lo em uma classe, alimentando seus atributos (classe `Response`).
    * Quase como se fosse um DTO, vai ter apenas os campos que quer buscar, ou, apenas os campos que serão usados.
  * Dentro desse pacote, criar a interface feign, usando a anotação `@FeignClient(name = <NOME DO SERVIÇO QUE VAI LER>, url = <URL DO SERVIÇO>)`
    * E essa interface precisa ter os endpoints.
      * No endpoint, receber os `@PathVariable` e enviar a `Response`, conforme foi definido na controller do microsserviço.
* O cliente feign precisa ser injetado na controller.
* Na classe inical, alem de ter a anotação dizendo que é uma aplicação spring, também dizer que é uma aplicação Feign, usando o `@EnableFeignClients`.
* O feign é síncrono.
* Para não sobrecarregar tanto um microserviço, instanciar o microsserviço quantas vezes for necessário.
  * Para isso, duplicar as instancias pelo spring boot dashboard.
  * Usa variáveis de ambiente para dizer a porta de cada um.
  * Para simplificar, mudar o nome da cada instância para dizer qual porta está usando (só não fazer isso com o "original").
  * O projeto fica sempre o mesmo, ele apenas vai ser executado por uma porta diferente.
  * Precisa alterar no cliente, pois lá está hardcoded.
    * Usar o discovery pattern para encontrar esse microsserviço.
* O Discovery Pattern tem como objetivo saber quais instancias estão ativas e qual a porta delas.
  * Ele faz um round-robin (esse é o padrão, mas da pra configurar), fazendo requisições de um em um para verificar quais estão ativos.
  * Balanceamento de carga (Load Balance).
    * Vai redistribuir as requisições entre as instâncias disponíveis.


## Eureka
* Dependência criada pela Netflix.
* Discovery Pattern
* Criar um projeto que vai ser o servidor (`Eureka Service`) enquanto os outros projetos serão os clientes.
* Na classe inicial, usar a anotação `@EnableEurekaServer` para dizer que vai utiliza-lo também.
* Usar as propriedades `eureka.client.fetch-registry=false` e `eureka.client.register-with-eureka=false`, para que não fique tentando se registrar sozinho.
* Precisa ser inicializado primeiro.
  * Quando os outros microsserviços são inicializados, eles vão se cadastrando no Eureka.
    * Precisa adicionar o client nas dependencia deles.
  * Ele so fica esperando alguém dar sinal a ele.
* Os clientes precisam conhecer o servidor Eureka, onde ele está rodando.
  * Para isso colocar a propriedade `eureka.client.service-url.defaultZone=http://localhost:8761/eureka`
    * Dessa forma ele se registra e pega a lista de microsserviços cadastrados.
* O `eureka.instance.prefer-ip-address=true` diz que vai usar o IP ao invés do DNS localhost.
* O Eureka vai mostrar quantas instâncias estão rodando de cada microsserviço.
* Gerencia usando load balance.
* No Feign, para pegar o que está no Eureka, tirar a url fixa do cliente.