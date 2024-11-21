# Aula 28

* Down Cast e Up Cast (funciona apenas com herança)
  * `Object` é o up superior, ou seja, impossível fazer upcast do `object`.
  * Up cast é implícito (widening cast), enquanto o down cast não (narrowing cast), precisa colocar o tipo para o cast.
    * Down cast precisa ver se possui a instância do cast.
  * Se tiver uma variável do tipo object, é possível fazer um cast explícito (down cast) para outro tipo.

### Type Safety
* Dinâmico (faz em tempo de execução).
  * Linguagens fracamente tipadas.
* Estático (em tempo de compilação)
  * Linguagens fortemente tipadas.
  * Cast
  * Tipos genéricos.

### Tipos genéricos
* Dizer para a classe que ela deverá funcionar com genéricos.
  * Vai "receber" o tipo genérico.
    * Classes genéricas sempre precisam do `<>` que indica o que é, o "tipo".
  * `public class Classe<E>`
    * A convenção diz:
      * T para tipos.
      * E para elementos.
      * K para chaves.
      * V para valor.
      * N para número.
      * R para resultado.
* Usar esse tipo genérico nos locais desejados.
* Teoricamente, as classes não genéricas vão ter como "tipo" a classe `object`, e por isso é realizado implicitamente esse processo.
  * Ou seja, todas as classes possuem "tipo"
* Ele só existe para ser utilizado, não tem como instanciar.
* Enviar o tipo na instanciação da classe que usa genérico.
  * Possível declarar a classe já com o tipo específico também, principalmente quando queremos limitar o uso de algum método que utiliza uma classe genérica como tipo.
    * Ou seja `public void Metodo(Classe<TipoEspecifico> oi){}`
      * Mesmo sendo uma classe genérica, especificamos que só é aceito o TipoEspecifico.
      * Para usar todas as classes filhas de uma determinada classe `Classe<? extends ClassePai>`
        * O `?` é um wildcard.

### Interface
* O que vai ser feito, mas não como fazer.
* Precisa sempre ser instanciado, ou seja, a interface vai ser implementada a partir da classe usada no `new`.
* Usar o `implements` na declaração da classe, para dizer que a classe implementa aquela interface.