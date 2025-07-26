# Aula 32

* O eclipse possui várias perspectivas, que são "telas" diferentes conforme a ação necessária.
  * Possível altera-las no canto superior direito.
* Criar um método com a anotação `@ExceptionHandler` para ser chamado todas as vezes que tiver uma exceção na classe.
  * Na anotação, colocar `@ExceptionHandler(Exception.class)` para dizer que são exceções geradas na classe ou em suas dependências.
  * Esse método vai retornar uma resposta com a mensagem da exceção.
    * Ex.: vai enviar um `BadRequest`, e no `body` vai enviar a mensagem de erro.
      * `ResponseEntity.badRequest().body(msg);`.

## Injeção de Dependência
* Na inicialização do programa, o `spring` vai ver que o construtor possui alguma dependência, e então ele vai precisar resolver isso instanciando a classe.
* Ele primeiro inicializa a dependência, e depois cria o objeto que possui essa dependência.
  * Ou seja, a classe é dependente da instanciação da outra.
* Por ser uma classe do tipo de serviço, com a anotação `@Service` o spring sabe que é ele que precisa gerenciar a sua instanciação.
  * E ele funciona apenas com as classes que tem essa anotação.

## Conexão com o banco
* Vai falar com o BD
* Pode usar ORM.
* `JPA` - Java Persistence API
  * Define uma interface padrão para salvar, atualizar, procurar, etc no BD.
    * A persistência, como deve funcionar.
  * Precisa implementar a interface do JPA usando uma ORM como o Hibernate, OpenJPA, etc.
  * `Spring Data JPA`
    * Facilita a implementação do JPA.
      * Complementa o JPA.
* Precisa usar as dependências no `pom.xml`.
  * Usando o `Spring Tools`, clicar com o direito no projeto, `spring > add starters`.
    * Colocar o `JPA` e o driver do banco SGBD, o resto (como o hibernate) vem como dependência dessa biblioteca.
* Em `resources`, abrir o arquivo `application.properties` e colocar as configurações necessárias para fazer a conexão.
  * Esse arquivo armazena as configurações tipo o app.config. 
  * A config `spring.jpa.hibernate.ddl-auto=update` permite que o banco atualize automaticamente conforme as colunas definidas.
    * Não usar em produção, pois pode ser perigoso ficar atualizando e alterando o banco.
    * Mesmo com essa config, ainda é necessário criar o database no banco.
    * Seria quase como o `connection string`, pois tem as informações do bd.
* Para declarar que a classe é uma entidade:
  * Colocar a anotação `@Entity` e para declarar seu nome `@Table(name = "user_tb"`.
* Para declarar um atributo (campo) como chave primária:
  * Usar a anotação `@Id` e dizer que o valor vai ser gerado automaticamente com o `@GeneratedValue(strategy = GenerationType.UUID)`.