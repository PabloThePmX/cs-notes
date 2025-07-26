# Aula 24
* Dry: Don't repeat yourself

### Diagrama de classe
* Como se fosse o modelo ER, mas para classes.
  * Explora o relacionamento entre as classes.
* Geralmente usado em sistemas POO.
* Classes abstratas são representadas com `<<>>` no nome.
  * Ou _`itlálico`_ (mais comum).
* No meio vai ter os atributos/propriedades.
  * Vai ter o tipo (`nomeAtributo : tipo`)
* Abaixo os métodos
  * Os métodos vão ter os parâmetros de entrada, e o seu retorno.
    * Os parâmetros precisam ter o nome e o tipo também.
* Acessadores:
  * `-` = privado
  * `+` = público
  * `#` = protegido
  * `~` = pacote/default
* Os tipos, seguir o padrão da empresa ou da linguagem em si.
  * `String` ou `string`, etc.
* Formas de relacionamento:
  * **Herança**: flecha lisa, filha apontando para a classe mãe.
  * **Associação**: Flecha lisa sem ponta, somente usado para dizer que de alguma forma há relacionamento entre as classes.
    * Na flecha pode dizer o que acontece, por exemplo, `Herói ATACA Inimigo`.
  * **Composição**: Flecha lisa com ponta "diamante"fechada, é usada para demonstrar que uma classe não pode existir fora da sua composição (instanciação).
    * Aponta para a classe que vai ser agregada.
      * Ex.: Um time é composto por jogadores.
    * Usado para tipos de atributos/propriedades. 
    * Maior parte das classes do sistemas são de composição. 
  * **Agregação**: Parecido com composição, flecha lisa com diamante ABERTO, usado quando é algo que vai agregar na classe, ou seja, pode funcionar fora dela.
    * Pode ou não precisar usar ela.
* Fazer o diagrama de classes apenas nas partes mais importantes do programa.