# Aula 15

## Instruções de Máquina
* ISA é o conjunto de comandos que uma arquitetura entende.
  * Arquitetura de conjunto de instruções.
  * Define quais comandos a arquitetura entende.
* A CPU executa o ciclo de instruções.
* Cada camada aproxima o programa da forma que o hardware realmente entende.
  * Alto nível -> Compilador -> Assembly -> Assembler -> Código de Máquina -> CPU.
* Uma instrução é um comando básico em bits.
  * Fica armazenada na memória junto com dados do programa.
  * A unidade de controle busca, interpreta e coordena a execução.
  * O assembly é a representação mais legível, porém para a CPU o que importa é o padrão binário daquela ISA.
* As instruções são divididas em opcode e operandos (operação + dados).
  * Opcode: A operação (o verbo) a ser realizada (`ADD`, `MOV`, etc)
  * Operandos: Os dados, locais ou registradores envolvidos na operação.
* Cada instrução pertence a uma categoria de trabalho.
  * Movimentação de dados -> LOAD, STORE, MOV.
  * Aritméticas -> ADD, SUB.
  * Lógicas -> AND, OR, NOT, XOR.
  * Controle de fluxo -> JMP, CALL, RET e desvios condicionais.
  * Manipulação de bits -> deslocamentos e rotações.
* O modo de endereçamento diz onde o dado está.
  * Podendo estar nos registradores, memória, imediato (na própria instrução) ou indireto (é um endereço, ponteiro, que aponta para outro dado na memória).
    * O indireto seria como se fosse um banco em bucket, que nesse caso o banco tem apenas uma tabela com o endereço de todas as tabelas daquele cliente.
      * Dessa forma cada cliente vai carregar apenas aquilo que precisa, e não de outros clientes, visto que o endereço redireciona para a tabela necessária.
    * O imediato tem a `#` na frente.
    * O `R1`, `R2`, etc é dos registradores.
    * Na memória (indireto ou não), usa o `[]`.
* Ciclo de instrução != ciclo de clock.
  * No ciclo, a CPU busca, decodifica, executa e armazena.
* x86 e ARM tem vocabulários diferentes.
  * Cada um tem sua ISA própria.