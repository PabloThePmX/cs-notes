# Aula 16

* Objetos possuem atribuição por referência.
  * Ao instanciar um objeto, ele não vai criar esse objeto, mas sim criar uma referencia na memória.
  * Ou seja, se for criado um objeto copiando o valor de outro valor, ambos vão ter seus valores igualmente atualizados quando forem atribuidos.
    * Conseguimos fazer isso sem referência, criando uma nova referência do objeto (`new()`)
* Tipos primitivos possuem atribuição por valor.
  * Duplica o valor da variável, ao invés de referencia-lo.
* Ao "declarar uma variável globalmente" na classe, estaremos criando os atributos (ou campos) que serão as propriedades da classe.
  * Depois serão feitos os métodos de getter e setter.
  * Deixando sem modificadores de acesso, o atributo vai ser default (que funciona dentro do pacote).
* O `this` é a instância atual do objeto, ele contém todos os dados armazenados nessa instância.
  * Valores de propriedades e métodos.
* Ao declarar a variável globalmente, teremos acesso a ela ao instanciar o objeto.
* O construtor padrão (sem parâmetros), não precisa ser declarado explicitamente.
  * Porém se colocar algum outro construtor, esse ctor padrão vai ser preciso declarar explicitamente.
* Ao clicar com o botão direito, temos a opção `Source Actions` e lá podemos criar construtores e selecionar os campos que vão ser inicializados nele.
* Sobrecarga de método.
  * Nomes iguais, assinaturas diferentes.
  * Geralmente o método com menos parâmetros vai chamar aqueles que tem mais parâmetros.
    * Não é regra, mas pode ser realizado dessa maneira.