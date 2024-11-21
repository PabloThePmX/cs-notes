# Aula 31

* MVC
  * Model View Controller
* JSON
  * Usado para trafegar os dados entre a api e o frontend.
* DTOs
  * Ajusta quais dados das entidades irão trafegar.
* O repositório persiste a conexão com o ORM.
* No eclipse podemos gerar os getters e setters automaticamente.
* No http, parâmetros são enviados via URL, depois do `?`.
* O Postman é um cliente.
* Usar o `@RequestBody` para dizer que o parâmetro do método é um objeto que estará vindo do corpo da requisição.
* UUID - Universally Unique Identifier
  * Usado quando há muitos processamentos de uma vez.
  * Evita ter PKs repetidas.
  * Pode ser gerado a partir do endereço MAC ou de forma totalmente aleatória (v4).
  * O java possui esse tipo.
* Usar o `BeanUtils.copyProperties` para passar o DTO para a entidade.
* No `POST` é comum retornar a entidade.
  * Usar a anotação `@JsonIngore` na propriedade, para não permitir que ela seja mostrada na resposta.
* Usar a anotação `@Service` para dizer que é uma classe de serviço.
  * Os métodos retornam a entidade.