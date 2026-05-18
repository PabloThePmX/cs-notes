# Aula 14

## Arquiteturas RISC e CISC
* CPU executa as instruções, e cada uma das filosofias tem instruções diferentes.
* CISC tende a instruções mais variadas e algumas mais complexas.
  * Meio híbrida.
  * Funções maiores com micro-funções.
* RISC tende a instruções mais simples, uniformes e forte uso de registradores.
  * Não sobrecarrega tanto a memória ram da máquina.
* ARM é baseada em RISC e x86 CISC.
* Não tem nenhum melhor, depende do produto.
  * A melhor escolha depende do objetivo.
* Ciclo básico se repete bilhões de vezes.
  * Busca.
  * Decodifica.
  * Executa.
  * Escreve de volta.
* x86 moderno não é CISC puro.
* Nem sempre o CISC vai ser pior em energia, ou o RISC vai ser o mais rápido.

### CISC
* Complex Instruction Set Computer.
* Tenta fazer mais trabalho por instruções.
  * Várias coisas em uma única instrução.
* x86/x86-64 (Intel e AMD).
* Hardware de decodificação mais complexo.
* Alguns processadores geram em CISC e depois quebram em instruções mais simples.
* Instruções de tamanho variável.
* Instruções ricas ajudam a economizar bytes.
* É compatível com décadas de softwares, sistemas e ferramentas.
  * Ecossistema forte.
  * Bem maior que o do RISC.
* Usa uma única instrução: `MULT 2:4, 4:1`.
* Mais usado em PCs ou Servidores.
  
### RISC
* Reduced Instruction Set Computer.
* Menos tipos de instruções.
* Forte uso de registradores (ponteiros para dados de memória.)
* ARM.
* Passos pequenos e bem organizados.
* Modelo LOAD/STORE.
  * Carrega cada dado requisitado, registra nos registradores, opera e salva.
  * O CISC faz as operações na memória.
* Menos complexo.
* Pipeline eficiente.
* Menor consumo de energia (bom para bateria) e portabilidade.
* Usa mais instruções: 
```
LOAD A, 2:4
LOAD B, 4:1
MULT A,B
STORE 2:4, A
```
* Mais usado em aparelhos móveis e embarcados.