# Aula 7

## Properties e Component
* Podemos criar uma classe apenas para buscar o valor das propriedades.
  * Usar a anotação `@Component` e `@ConfigurationProperties("<PREFIXO-PROPRIEDADE>")`.
  * Dentro da classe, podemos criar atributos com o mesmo nome das propriedades, e o spring vai conseguir ler corretamente.
    * Mesmo que nas classes, os atributos sejam camelCase e nas propriedades seja kebab-case.
  * Dessa forma, quando queremos buscar os valores das propriedades, buscamos diretamente dos acessadores dessa classe componente.
    * Usar a injeção de dependência para implementar essa classe nos controllers.
      * É uma boa pratica deixar o atributo privado que recebeu a DI como `final`.
* Vamos ter vários arquivos de propriedades, para desenv, produção, etc.
  * Separar o perfil por `-`.
    * Ou seja, o nome de cada perfil vai ficar depois do `-`.
  * Dentro das propriedades "raiz", definir qual é o perfil que vai estar ativo.
    * Usar a propriedade `spring.profiles.active = <NOME APOIS O HIFEN>`.
* As configurações do programa podem ter várias fontes, podendo ser `.env` também.
  * Pode-se ter um microserviço responsável apenas por buscar essas configurações.
* Dentro das configs de inicialização do spring, podemos também criar variáveis de ambiente.
  * Usa-se o `SNAKE_CASE` para nomear as variáveis. 
  * Como isso não sobe pro git, da pra colocar as senhas e tudo mais.
  * As configs de linha de comando terão propriedade sobre as outras.

## Empacotamentos
* o `JAR` é um empacotamento de java, que salva os arquivos bytecode `.java`.
* Para executar um JAR, usar o comando `java -jar <app.jar>`
  * Para executar em um servidor, colocar a flag `--server.port=<porta>`
  * Da pra usar argumentos no inicializador da aplicação do spring.
    * Se não definir um argumento de porta, vai para o padrão que é `8080` 