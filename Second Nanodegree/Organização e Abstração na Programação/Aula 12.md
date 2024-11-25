# Aula 12

* Linguagens Interpretadas e Compiladas
  * **Interpretadas:** são aquelas que o código fonte é executado linha por linha pelo interpretador, sem precisar compilar.
    * Python, Javascript, PHP, etc.
    * Maior portabilidade, pois não precisa gerar para infras diferentes (windows, linux, mac).
  * **Compiladas:** Requerem que seja compilado antes da execução. O código é traduzido para linguagem de máquina e é produzido um arquivo executável.
    * C, C++, etc.
    * Mais rápidas e eficientes.

### Java
* Write Once, Run Anywhere (WORA).
* Multiplataforma
* Vai ser mais pesado.
* A Oracle adquiriu a Sun e consequentemente pegou o Java.
* As principais versões atuais (LTS):
  * Java 22
  * Java 21
  * Java 17
  * Java 11
  * Java 8
* O JDK é o compilador, que vai gerar o bytecode (`.class`).
  * E vai ser a JVM que vai ler isso.
* O Java é interpretado e compilado, pois vai gerar o bytecode e depois vai ler com a JVM.
* O JIT (Just in Time) é um compilador em tempo de execução, que verifica se uma parte do código é chamada várias vezes, e assim, ele vai compilar aquela parte apenas uma vez e armazenar em cache, sendo assim, pode buscar diretamente do cache sem a necessidade de compilar novamente.
* JDK, JRE, JVM
  * JDK para desenvolvimento, contém o JRE e o compilador, etc.
  * JVM é o ambiente virtual que execute o bytecode (`.class`)
  * JRE é o pacote que contém a JVM e componentes úteis para a execução de aplicações java.

* ### Desenvolvimento
* Desabilitar o inlay.
* Métodos e propriedades é em camelCase, e a classe PascalCase.
* O `javac` é o compilador, ele precisa receber o arquivo.
* Para executar o código, vamos colocar o `java` mais o nome da classe (sem a extensão no nome).
* Rodando automaticamente, ele vai jogar a `.class` em uma pasta temporária para ser executada.
* Se colocar apenas `class` vai ser uma classe `default`, que apenas funciona dentro da pasta atual, porém, o padrão é ter a declaração sempre como `public class`.
* É possível declarar a variável sem atribuir o seu valor.
* Precisa ter o método `main()` para iniciar o programa.