# Aula 12

## Arquiteturas de Processadores

## Modelo de Von Neumann
* Foi criada em 1945.
* Base para arquitetura mais complexas utilizadas hoje.
* Apenas uma memória para dados e instruções.
  * Nos registradores da CPU, existe o PC (Program Counter) para ver a próxima instrução a ser executada.
* Gargalo de Von Neumann
  * Também conhecido como barreira de memória.
  * Ocorre devido ao fato de possuir apenas uma memória para dados e instruções.
  * Dentro do processador existe a memória cache, para evitar a necessidade de buscar na RAM.
  * Para melhorar esse gargalo:
    * Melhorar componentes de interconexão e memória RAM, com um DDR-SDRAM.
    * Usar memória cache.
* A velocidade do processador é definida pelo clock e número de nucelos.
  * O clock se refere a quantidade de vezes que o processador consegue fazer um ciclo por segundo.
* Estão presentes em processadores x86 como Intel e AMD.
  * Em ARM que utilizam Cortex também.

## Modelo de Harvard
* Tem uma memória para guardar os dados, e outra para as instruções.
* É mais complexa.
* Utilizada principalmente em processadores DSP, também conhecido como processadores de sinais.

## Instruções
* Um programa é constituído por uma sequencia de instruções.
* Operação + Operandos (Dados) = Instrução.
* O hardware funciona através de ordens simples e básicas.
* O ciclo de instrução possui cálculos e decodificações.
* O processador é um dispositivo que opera em ciclos.
  * Ciclos de execução de instruções
  * Também conhecido como ISA (Instruction Set Architecture).
  * É a interface entre o software e o hardware.
* Processadores podem implementar conjuntos de instruções maiores ou menores.
* É comum que um novo processador herde o conjunto de instruções do mais antigo.
* Conjunto de Instruções: Quais operações estão disponíveis.
* Microarquitetura: Como estas operações são implementadas.
* Alguns conjuntos de instruções: x86_64, ARM, PowerPC, etc.
* Instruções são armazenadas em conjunto de bits.
  * Em algumas arquiteturas o tamanho é fixo (tipo o MIPS), e outras não.
* Toda a instrução deve conter (são divididos dentro dos bits):
  * Código da operação (opcode)
  * Referência do operando-fonte.
  * Referência do operando-destino.
* Opcodes são representados por abreviações chamadas mnemônicos, que indicam operações.
  * Exemplos: ADD, SUB, MPY, DIV, LOAD (para pegar um valor da memória), STORE (para atribuir um valor a uma variável), MOVE (para atribuir um valor que não precisa buscar na memória).
* Instruções podem ser agrupadas em:    
  * Processamento de Dados.
  * Armazenamento de Dados.
  * Controle de Fluxo de Dados.
  * E mais uma que não vi.
* Em instruções com 3 operandos, primeiro começa com o destino. 
  * Ex.: `ADD A, B, C` = A=B+C.
  * É a mais complexa pois gasta mais memória.
* De 2 operandos: `ADD A, B` = A=A+B.
* Com 1 operando: `ADD B` = ACC=ACC+B.
  * Usa um acumulador, que existe apenas um mas é limpo ao final de cada instrução.
  * Requer mais instruções, mas usa menos memória.
* Sobre os comandos, para passar da vida real para máquina, sempre faz da operação mais adentro.
  * Usando apenas 1 endereço, faz e atribui o valor, e repete esse processo.
* Exemplos:
1. Y = (A+B+C) * (D/(E*F))
```assembly
LOAD E
MPY F
STORE J
LOAD D
DIV J
STORE K
LOAD A
ADD B
ADD C
MPY K
STORE Y
```

2. Y = ((A+B) - C) / D^2
```assembly
LOAD A
ADD B
SUB C
STORE K

LOAD D
MPY D
STORE R

LOAD K
DIV R

STORE Y
```

3. Y = A^3 * (B^2/(C+D))
```assembly
LOAD C
ADD D
STORE K

LOAD B
MPY B
DIV K
STORE U

LOAD A
MPY A
MPY A

MPY U

STORE Y
```
* Existem computadores hipotéticos para simular arquitetura.
  * Ex.: Ahmes.