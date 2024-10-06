# Aula 19

* Persistência, quer dizer que ele salva no banco, persistência de dados.
* As camadas (da ordem em que as coisas acontecem, ou seja, começa na tela, verifica e depois manda para o banco):
  * Apresentação (View).
    * `main`    
    * Interação com o usuário.
  * Negócio (Services).
    * Se der erro aqui, tem que mandar pra camada de view.
  * Persistência (Repositories).
    * SQL
* A entidade vai trafegar entre as camadas, até chegar no banco.
* Todas as classes herdam membros da classe mãe `Object.class`.
  * As classes omitem o extends dessa classe, e acaba sendo uma herança hierarquica.

### Herança
* Permite que classes herdem membros (atributos e métodos) de outra classe.
* Usar o `extends` na assinatura da classe.
* Uma classe que herdou outra, também pode ser considerada como uma instância da classe pai.
  * Um exemplo seria a da `List<ClassePai>` que também vai funcionar com a classe filha.
  * Uma variável pode ser declarada como o tipo pai, e depois atribuir uma clsse filha nessa mesma variável.
    * Esse vai ser o tipo concreto dela.
    * Se precisar de algum membro de uma classe filha, fazer o cast na classe pai.
      * Para fazer o cast em Java: `((ClasseFilha) ClassePai).usaProp()`.

### Polimorfismo
* Métodos herdados com implementações diferentes em cada classe, ou métodos com sobrecarga de método, ou seja, outra assinatura. 
* Existem dois tipos de polimorfismo:
  * **Estático ou sobrecarga (overload) de método.**
    * Mesmo nome com assinaturas diferentes (parâmetros diferentes).
    * Dentro da mesma classe.
  * **Dinâmico ou sobrescrita (override) de método.**
    * Usar o `@Override` como annotation do método.
      * Da pra fazer pelo `Source Action`
    * O método sobreescrito, vai ser chamado pelo objeto concreto.
      * Ou seja, vai ser definido durante runtime, pois em algum momento o objeto concreto vai ser um tipo (na hora de declarar por exemplo), e depois ao atriuir pode virar outro (se for atribuido algum dos valores filhos da classe de declaração).
    * Vai ser possuivel quando a classe herda de outra.
* Podemos implementar um método com menos parâmetros, que vai chamar o método com mais parâmetros (esses outro parâmetros seriam opcionais), enviando null nos parâmetros adicionais, evitando assim, que seja feito dois métodos com o mesmo código.