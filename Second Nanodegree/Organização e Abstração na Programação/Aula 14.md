# Aula 14

* Usar `printf` para formatar uma variável no print.
  * E usar o `%` para dizer onde a variável vai ser colocada.
    * É preciso especificar o tipo da variável, sendo `%s` para string, `%i` para int, etc.
      * Porém, ao fazer testes, notei que só se usa os númericos quando é feito algum tipo de formatação no valor em si, pois de resto, usar eles como string.
* Como no C#, quando temos apenas uma instrução na condição, não precisamos usar chaves `{}`.
* Podemos usar `else if` nas condições.
* Ao invés de usar `else if` podemos colocar o `switch`.
  * Sempre colocar `break` ao final de cada `case`, pois sem isso, ele vai executar todos os cases abaixo da condição que entrou.
  * A partir do JDK 12, existe switch com retorno usando arrow `->` (e não usa break, pois é apenas uma linha).
  * Usar `,` em cada condição do case, para fazer algo no estilo de um OR
    * Ex.: `case 1, 2, 3:`
* O `.next()` pega apenas antes do espaço, ja o `.nextLine()` pega toda a entrada.
  * O `nextLine()` vai "passar" para próxima linha, "limpando" o que restou.
* Encadeamento de método.