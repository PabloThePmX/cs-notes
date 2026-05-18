# Aula 19

## Funções em VHDL
* Apesar de parecer com software, o resultado final sempre vai ser hardware.
* Funciona como qualquer outra função em linguagens de programação.
* Recebe entradas e produz uma saída.
* Pode receber zero o mais parâmetros, e pode usar variáveis locais (que existem apenas dentro da função).
* A sintaxe para criar uma função parece com TS.
```vhdl
function soma(a : integer; b : integer)
    return integer is
begin
    return a + b;
end function;
```
* Para declarar uma variável, usar `variable r : integer;`
  * Colocar isso antes do `begin`.
* São úteis para comparar e converter vetores.
  * O `bit_vector` representa a sequência de bits.
* Quando tem dois parâmetros do mesmo tipo, da pra definir apenas no último.
  * `function igual(a, b : bit_vector) return bit is`.
* Função na `Architecture` (hardware) ou `Package`?
  * `Architecture` é mais simples, e é para uso local.
  * A `Package` é para reusar entre arquivos, como se fosse uma biblioteca de projetos.
    * Bom para funções comuns.
* A sintaxe para criar uma `Package`:
```
package util is 
    function eh_zero(x : integer) return bit;
end package;

package body util is
    function eh_zero(x : integer) ...
```
* Ou seja, declara a interface e a implementação em si.
* Da pra usar `switch case` e `lambdas`.
* Função não é o melhor lugar para guardar estado.
  * Função deve ser pensada apenas como lógica.
  * O `process` é quem deve fazer isso.
* Tipos de Ferramentas:
  * Função: Lógica combinacional que retorna um valor.
  * Process: Comportamento agrupado, podendo ser sequencial ou combinacional (e pode armazenar estado e clock).
  * Componente: Bloco maior de hardware reutilizável.