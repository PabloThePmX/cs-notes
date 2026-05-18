# Aula 18

## HDL e base de VHDL
* Software descreve passos. HDL descreve circuito.
* VHDL represente conexões, portas. registradores e lógica que existirão no hardware.

### Software
* Executa instruções.
* Depende da CPU.
* Fluxo linha a linha.
* Variáveis mudam durante a execução.

### HDL
* Descreve circuito.
* Portas e registradores.
* Sinais podem existir em paralelo.
* Precisa fazer sentido para a síntese (passo final).

* Do HDL para o hardware.
  * VHDL -> Simulação -> Síntese -> Implementação -> FGPA.
  * A simulação é feita antes, para que não haja problema depois no hardware.
* HDL é usado para projetar, simular e sintetizar o hardware.
* `Entity` é a interface. `Architecture` é a lógica.
  * A `entity` da o nome do circuito.
  * `Architecture` é a lógica interna que descreve como as saídas são produzidas.
* `Signal` é o fio interno usado dentro da architecture.
  * Faz a ligação entre os dados.
* Os tipos:
  * `bit`: 0 ou 1.
  * `std_logic`
  * vetores: sequência de bits.
* Cada linha executa em simultâneo, e não exatamente linha a linha.

### Combinacional
* Saída depende das entradas atuais.
* Não guarda estado.
* AND, OR, MUX (multiplexador).
* Precisa sempre ter um retorno.

### Sequencial
* Depende da entrada + estado.
* Guarda memória.
* Registrador, contador, FSM.

* `Process` agrupa comportamento, mas ainda descreve hardware.
  * Lista de sensibilidade.
* Clock sincroniza quando o estado muda.
* Um registrador guarda valor quando o estado muda.
* Circuitos sequencias costumam precisar de controle.
  * `Reset`: Coloca o circuito em estado conhecido, normalmente no início.
  * `Enable`: Permite atualizar apenas quando a condição de controle estiver ativa.

### FSMs - Máquinas de Estados Finitos
* Uma FSM tem:
  * O estado atual representa a situação do circuito.
  * Entradas definem transições.
  * Saídas dependem do estado, e as vezes, das entradas.
    * Tipo um semáforo.
  
* O HDL ajuda quando o circuito cresce.
  * Ele não elimina a complexidade, mas da uma forma legível de descreve-la, simular e revisar.
* Nem todo o VHDL vira hardware físico.
  * Sintetizável.
  * Apenas simulação.