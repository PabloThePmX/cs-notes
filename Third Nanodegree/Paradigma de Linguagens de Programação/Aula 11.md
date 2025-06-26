# Aula 11

## Mensageria
* É uma comunicação assíncrona.
* RabbitMQ (AMPQ)
* Vai enviar para um `exchange` que então vai enviar para uma fila, e depois vai enviar para os clientes.
  * Clientes podem estar em várias filas.
  * Vai publicar na fila.
* Muito usado por e-commerce para fazer a confirmação do pagamento, pois fica aguardando a confirmação do mesmo pela fila da mensageria.
* Se o serviço esta fora, quando ele voltar, ele vai verificar se tem algo na fila para ser processado.
* Todos os serviços podem ficar independentes e autônomos.

## Microservices Patterns
* Vem de um livro.
  * Existe uma página microservices.io com os padrões.
* Quem pede, é sempre o cliente.

### Alguns Patterns
* Health Check Api - Verifica se o sistema está online ou não, e outras informações (No java, com o actuator). 
* Database per Service - Ter uma db para cada serviço.
* Externalized Configuration - As configurações da API não devem estar no código em si (hard coded).
  * Colocar em um arquivo, variáveis de ambiente ou um servidor só pra isso.
* Service Registry - Precisa de um local para checar as instancias que estão rodando, é um serviço que não chama ninguém (Eureka).
* Self Registration - As instancias se registram automaticamente no serviço de registro.
* Client Side Service Discovery - Pega a lista de instâncias que estão rodando no discovery, para saber se o serviço que vai ser chamado existe e está rodando. (O cliente vai ser responsável por verificar as instancias que ele vai chamar).

## Resilience Patterns
* O que fazer caso algo parou de funcionar, maneiras de contornar, etc.
* Falhas são inevitáveis, alta disponibilidade, isolamento de falhas, recuperação automática, experiência do usuário.
* No java temos o `Resilience4j` para o spring.

### Alguns Patterns
* Rate limiting - Controlar o número de requisições recebidas por segundo, para evitar ataques DDOS.
* Retry - Tenta realizar a operação novamente após falhas temporárias.
* Timeout - Define um limite de tempo para as chamadas a serviços externos, evitando que o sistema fique preso aguardando resposta.
  * Pode ser perigoso em requisições assíncronas, pois se um serviço depende de outro que tem um timeout maior, pode ser estourado um erro.
* Fallback - Uma ação alternativa realizada quando uma operação falha.
* Caching (Cache) - Armazena temporariamente respostas ou dados para evitar chamar repetidamente algum serviço.
* Bulkhead - Uma técnica para isolar falhas em sistemas distribuídos (vem da técnica de isolar vazamentos em navios).
  * Microsserviços e container podem ser consideradas técnicas de bulkhead.
  * Threads e processos também.
* Circuit Breaker - Vem do conceito dos disjuntores, ou seja, fechado significa que o sistema está rodando, e aberto quer dizer que houve uma quebra no mesmo.
  * Solicita e recebe a resposta (fechado, pois vai e volta).
  * Quando aciona a função fallback e incrementa o contador de falhas.
    * Quando atinge o limite de falhas, fica em estado aberto e nem tenta mais se conectar, e para isso é definido um tempo em que ele vai ficar aberto.
  * Ficar no estado meio aberto é quando ele vai tentar se conectar novamente após abrir, e para isso é definido quantas vezes vai ser tentado.
  * Vai tentar pelo menos n vezes, caso a % especificada de erro for atingida após realizar as chamadas mínimas, pode abrir o circuito.

## Fallback e Circuit Breaker
* Ao usar o `Resilience4j`, precisa criar uma classe que vai ser o fallback da interface que pode dar o erro.
  * O método vai retornar o fallback designado.
  * A classe precisa implementar essa interface.
  * O `Resilience4j` precisa ser habilitado na classe "pai" que vai ter o fallback.
    * Isso vai ser colocado dentro da anotação do `FeignClient`, e vai apontar para a classe de fallback.
      * Ou seja, se der um erro no Feign, vai buscar a implementação do fallback.
* A classe de fallback precisa ser um componente (bean), ou seja, precisa ter a anotação `Component`.
* Usar a propriedade `spring.cloud.openfeign.circuitbreaker.enabled=true` para habilitar o fallback (circuit breaker) no OpenFeign.
  * Entretanto, dessa forma vai usar as configurações padrão.
    * Para modificar o circuit breaker de cada classe, usar as propriedades de `instance`.
      * A instancia vai ser o nome da interface + o método + o tipo de dado dos parâmetros.
* Para mostrar as informações do circuit breaker no actuator, usar a propriedade `management.health.circuitbreakers.enabled=true`.

## Caching
* Usar a dependência `Spring Cache Abstraction` e `Caffeine`.
  * Usar o `Caffeine` para cache local.
  * O `Caffeine` precisa ser pego do Maven repository (mvm repository).
    * Só copiar o xml dessa dependência de lá.
    * Não precisa usar tag `version` pois o spring é quem vai cuidar disso.
* Na classe de entrada, precisa usar a anotação `EnableCaching` para dizer que vai usar cache.
* No local em que vai ser usado o cache, pode ser feito de várias formas, sendo uma mais imperativa, verificando se tem cache, e então apenas caso não possuir, é que vai buscar.
  * Dessa forma, fazer uma injeção de dependência da classe CacheManager, que vai ser responsável por gerenciar isso.
    * Com ele da pra adicionar, remover, buscar do cache.
* Cache sempre vai ser chave valor.
* Para ler do cache, usar o método `getCache()` buscando pelo nome do cache, e depois, usar o `get()` para buscar por uma chave especifica dentro desse cache.
  * Da pra deixar classes em cache. 
  * Para salvar no cache, fazer a mesma coisa, porém usar o `put()` ao invés do `get()`.
    * Ambos precisa dizer a chave, e o que vai salvar/buscar.
* Nas propriedades, dizer que o cache vai ser do caffeine com a propriedade `spring.cache.type=caffeine`.
* Para definir o tamanho máximo, e em quanto tempo expira: `spring.cache.caffeine.spec=maximumSize=500, expireAfterWrite=10m`.
* Da pra ver os caches pelo actuator.