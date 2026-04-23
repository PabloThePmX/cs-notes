# Aula 4

## Máquinas de Estado Finito

* É uma representação matemática utilizada para descrever o comportamento do sistema em todas suas situações possíveis.
* Podem ser divididas em dois tipos:
  * Aceitadores/reconhecedores: Esta máquina de estados apresenta estado final e inicial bem definidos.
    * Existe apenas uma transição para cada estado, ou seja, não é sensível a entrada do sistema, levando o sistema do ponto inicial até o final sempre pelo mesmo caminho.
  * Transdutores: Apresenta uma saída que depende do estado atual da máquina e da entrada do sistema. 
    * É largamente utilizado em aplicações de controle, através de máquinas de Mealy e Moore.   
* Existe uma outra diferença entre autômatos determinísticos e não determinísticos.
  * Os autômatos determinísticos (AD) são aqueles em que, para cada estado em que se encontram, há uma única transição bem definida para o próximo estado.
    * Dado um estado e um simbolo de entrada, existe somente apenas uma opção de transição possível.
    * São altamente previsíveis.
  * Os autômatos não determinísticos (AND) são aqueles que, para um dado estado e um símbolo de entrada, podem existir diversas transições disponíveis.
    * Com um AND pode escolher qual a transição.
    * Habilita múltiplas soluções.
    * Podem ser mais difíceis de serem implementados.

### Representações
* A forma mais comum de representar uma máquina de estados finitos é com uma tabela de transição de estados.
* Outra forma se da por diagramas de transição de estados.

### Máquinas de Moore e Mealy
* Toda máquina de Moore é equivalente à máquina de Mealy com os mesmos estados transições e funções de saída, alterando apenas a sua notação.
  * Semelhante uma conversão de Mealy poderá ser convertida em uma de Moore, porém essa conversão pode levar a um número maior de estados, uma vez que máquinas de Mealy, um estado pode apresentar múltiplas saídas.
* Máquinas de Mealy tendem a ter menos estados que as de Moore, porem apresentam um numero maioor de saidas.

#### Moore
* Mais previsível, mais estável.
* A saída depende apenas do estado atual.
  * Ou seja, entrou no estado, a saída já é prevista.
* A saída não muda imediatamente com a entrada, só quando muda de estado.
* É como um semáforo, a cor depende do estado atual, não importando o que acabou de acontecer.

#### Mealy
* Mais rápida, mais reativa.
* A saída depende do estado atual e da entrada atual.
  * Ou seja, a saída pode mudar instantaneamente quando a entrada muda.
* É como um controle, que ao apertar o botão, a tv liga na hora.