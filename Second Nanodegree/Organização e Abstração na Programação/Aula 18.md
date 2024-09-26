# Aula 18

* Começa modelando o sistema pelas entidades.
* O service (negócio) vai gerenciar as regras de negócio.
  * Regras de negócio são as regras que vão ser definidas para o bom funcionamento do sistema para o usuário, ou seja, as verificações para não deixar que sejam colocadas informações inválidas no sistema.
  * Vai avisar que deu erro, mas não vai exatamente mostrar para o usuário, pois isso é responsabilidade da view.
    * Seria basicamente uma resposta do back, que vai enviar para o front mostrar para o usuário.
  * O service faz as verificações, e a api faz o envio e recebimento das informações.
    * Ou seja, são coisas diferentes.
* Camada de apresentação (view), é a parte que vai interagir com o usuário (a interface).
* Usar o `parseInt` do objeto `Integer` para tentar passar uma variável para `int`.
* Objeto `Comparator` para usar no sort de lista e afins.
* Existe o `equalsIgnoreCase()` para ignorar o case durante uma comparação.
* Para dizer que um método pode lançar exceções, devemos além de fazer um `throw` dentro do método, colocar na sua assinatura também, como `metodo() throws Exception {}`. 
  * E no método que chama, precisamos tratar com `try-catch`.
  * Uma exceção não mostra na tela.
    * Elas são usadas quando queremos trabalhar apenas no back, pois se usamos a exceção agora, só precisamos depois "pegar" no front, sem precisar realizar novas alterações no service.
      * Caso fossem usadas mensagens normais, como `sysout` por exemplo, esse não seria o caso pois seria necessário fazer alterações na camada de serviço para implementar o front.