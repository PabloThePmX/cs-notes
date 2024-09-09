# Aula 10

### Enapsulamento
* A prática de ocultar detalhes internos
* Na maioria das linguagens isso é feito usando os modificadores de classe:
  * `public`
  * `private`
  * `protected`: usável dentro do mesmo pacote.
  * `default`: sem modificador
* Modificadores de acesso no python:
  * Por padrão (default) os métodos/propriedades são públicos.
  * `__` para deixar privado
    * Porém na realidade, em runtime ele cria uma nova variável com o nome da propriedade sem a clase `veiculo__marca` fica `__marca` ao ser chamado.
      * Assim, gera exceção, pois em primeiro lugar, essa propriedade nem deveria ser acessível por ser privada.
* No python, precisamos criar os get e set como métodos:
  * Com os nomes `set_valor()` e `get_valor()`.
  
### Herança
  * Extende a classe.
  * No python deverá ser mandada a classe pai como parâmetro para a classe filha.
  * No construtor, usar `.super()`.
    * O `super` se refere a super classe, a classe pai.
  * Herança simples, de vários níveis, e múltipla.