# Aula 6

* Os valores após o `?` de uma URL, são os parâmetros e seus respectivos valores.
* Da pra colocar valores nas propriedades da aplicação, colocando o `nome da aplicação.nomeProp`.
  * Pegar usando a anotação `@Value` buscando pelo nome definido nas propriedades.  
* As propriedades seguem o padrão `kebab-case`.

## Microservices (Arquitetura de camadas)
* Os microservices irão separar um projeto em vários projetos pequenos, assim, pode ser feito o deploy indepentende para cada aplicação.
  * Uma arquitetura de camadas monolítica é um projeto que tem todas as partes, não sendo separado por microserviços.
* Dessa forma é mais fácil de escalar a aplicação.
* Fica mais fácil de dar manutenção, pois iremos dar manutenção separadamente.
  * Dessa forma, pode ser feito um shutdown em apenas um serviços, sem que os outros sejam afetados.
* Como são projetos diferentes, cada parte pode ser feita usando uma linguagem diferente, bancos diferentes, etc.
* A UI se conecta com a API Gateway, e ela vai redirecionar pro microserviço designado.
* Monlítico usa configurações locais, enquanto um projeto usando microserviços, tem várias configurações para cada um dos microserviços.
  * No JAVA, tem o spring cloud config que vai ter todas as configurações.
    * HashiCorp Vault para armazenar senhas.