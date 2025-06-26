# Aula 9

* Para câmbios, salvar um valor padrão (geralmente em dólar) no banco, e quando pedir, vai retornar esse valor porém convertido para a moeda escolhida.
* Envia o valor, a moeda de origem e a moeda de destino.
* Persistência de dados = guardar os dados.
* O spring possui uma dependência para o postgre.
  * Usa junto com o JPA.
* O `flyaway migration` vai controlar o versionamento do banco, verificando se o banco de dados está de acordo com o banco definido no projeto (criando tabelas novas caso necessário).
  * Ele cria uma nova pasta chamada `db` com uma pasta de migration.
  * Segue o mesmo principio das migrations do Entity Code First.
* Usar nas propriedades o `spring.datasource.url=jdbc:postgresql://<LOCAL DO BANCO>` para se conectar ao banco.
* A propriedade `spring.jpa.hibernate.ddl-auto` vai verificar se as entidades estão iguais ao banco.
  * Nesse caso, usando migrations, podemos deixar `none`, pois quem vai verificar isso é o `flyaway`.
* Dentro de uma entidade, usar a anotação `@Transient` para dizer que um atributo não sera persistido no banco.
* As declarações no repositório podem conter `AND`, `OR` para definir como que vai ser realizada a consulta no banco.
  * Usar o nome das variáveis para definir com o que e aonde.
* O jpa usa o `HikariPool` para controlar as conexões com o banco de dados.
* O `flyaway` cria uma tabela com o histórico de versionamento do banco.
* As migrations sempre vão seguir um padrão de nomenclatura, contendo `V1__<NOME>.sql`, `V2__<NOME>.sql`, ou seja, a versão precisa ser sequencial e o nome pode ser escolhido pelo usuário
  * Possui dois underlines
  * É o script SQL usado naquela versão.
  * Ele é executado automaticamente ao rodar a aplicação, quando ele verificar que é uma nova versão.
  * Ele gera um `checksum` para cada arquivo, para que antigos SQL não sejam alterados.
    * Ou seja, se ele ver que o script SQL foi alterado, da erro.