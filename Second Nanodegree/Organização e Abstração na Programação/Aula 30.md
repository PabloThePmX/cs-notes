# Aula 30

* Request e Response
* URI são as identificação dos recursos
  * O endereço do link em si.
* Todo protocolo tem headers.
  * Tanto o request como o response terão essas informações.
* HTTP não tem estado, e sim sessões.
* Existe o socket que abre a conexão, e permite que seja feita qualquer requisição no sistema.
  * Porém não é muito usado, e é bem mais complexo, pois as requisições precisam ser feitas manualmente.
  * Da um controle maior.
  * É usado em apenas ocasiões bem específicas.

### Spring
* Spring framework e spring boot.
* O `Maven` serve para fazer o build da aplicação e gerenciar as bibliotecas.
  * É um XML.
  * Estilo `npn`
* No spring, a convenção do package seria a junção do group e do artifact.
  * Tudo minúsculo.
* O `pom.xml` é o arquivo de configuração do Maven.
  * Tipo o `csproj`, onde terá as dependências e afins.
* Todas as classes precisam ficar dentro do pacote em `src\main\java\pacote`
  * Pacotes também, como por exemplo as controllers, que ficam em um pacote `.controllers`.
* Usar a anotação `@RestController` na classe, para dizer que é um controller.
  * Abaixo do controller, para colocar a rota, usar a anotação `@RequestMapping()` com o valor da rota nos parênteses, usando o `/`.
    * Ex.: `@RequestMapping("/status")`.
* O endpoint tera o retorno de `ResponseEntity<T>`
  * E o `<T>` vai depender daquilo que queremos retornar.
  * Ele permite retornar os códigos HTTP, como `ResponseEntity.ok("Resposta de Retorno")`
* Usar as anotações para definir os métodos também.
  * `@GetMapping` para declarar um método `GET`.
    * Podemos colocar o caminho do endpoint a partir do mapeamento do controller dentro dos parênteses do `GetMapping`.
      * Ex.: `@GetMapping({"","/"})`, ou seja, funciona com `controllername/` ou `controllername`.

### Tipos de API
* WebService API
* APIs de Bibliotecas
  * Fornecem funções e métodos para desenvolvedores.
* API de Sistemas Operacionais
  * Usada para integrar sistemas diferentes.

### SOAP API
* Utiliza o protocolo SOAP, que utiliza XML.
  * Isso poderia ser um problema, visto que o XML é muito verboso.
* SOAPHeader e SOAPBody.
* Acabava sendo muito complexo de se trabalhar.

### REST API
* Utiliza HTTP e JSON.
* As requests tem um método:
  * `GET`
  * `POST`
  * `PATCH`
    * Apenas atualiza um valor.
  * `PUT`
    * Atualiza ou cria um novo valor.
  * `DELETE`
* O cliente que faz as requisições.
* A resposta tem os códigos HTTP.