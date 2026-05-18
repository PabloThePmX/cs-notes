# Aula 17

## Arquiteturas DSP em FPGAs.
* Hardware reconfigurável para processamento paralelo de sinais.
* CPU executa instruções. FPGA é configurado para virar circuito.
* FGPA monta caminhos em paralelo, enquanto a CPU executa uma sequência.
  * A diferença entre ambos é o paralelismo.
* Dispositivos lógicos programáveis existem para reconfigurar a lógica.
* Permitem criar circuitos digitais sem fabricar um chip novo.

### Tipos

#### ASIC
* Chip dedicado.
* Ótimo em volume (é mais barato comprar em grandes quantidades)
* Alto custo inicial.
* Não configurável.

#### FPGA / CPLD
* Programável em campo.
* Ótimo para protótipos.
* Mais flexível.
* Bom para lógica e paralelismo.

#### CPU / MCU
* Programação em software.
* Baixo custo e simplicidade.
* Excelente para controle geral.
* Menos paralelismo físico.

### FGPA
* O FGPA faz sentido quando o problema tem um padrão repetitivo.
* Nem todo o problema melhora quando vai pra FGPA, pois pode ficar mais complexo.
* Recursos internos do FGPA.
  * LUT: Guarda uma tabela verdade pequena.
    * Entradas funcionam como endereço da tabela.
    * Pode ter portas AND, OR, XOR, etc.
  * BRAM: Armazena blocos de dados.
  * IOB: Conecta o chip ao mundo externo (EX.: GPIO da Raspberry). 
  * Flip-Flop: Memoriza 1 bit no clock.
  * DSP: Multiplica e acumula com eficiência.
  * Switch Matrix: Liga os blocos por rotas programáveis.
* Ele combina blocos lógicos, conexões e entradas/saídas.

### DSP
* É processamento digital de sinais.
* Sinais aparecem em áudio, imagem, sensores, rádio e controle.
  * Chagam como fluxo.
* Operação MAC (Multiply-Accumulate).
  * Acumulador
* O bloco DSP é uma peça pronta para contas repetitivas.
  * Entradas -> Multiplicador -> Somador -> Registrador.
  * Economiza LUTs para outras partes do projeto.

* Latência: Quanto tempo um dado demora para entrar, ser processado e sair.
* Throughput: Quantos resultados o sistema consegue entregar por segundo.
* Filtro FIR.
* Antes de gravar a placa, o circuito passa por ferramentas.
  * Ideia -> HDL -> Simulação -> Sintese -> Place & Route -> Bitstream -> FGPA.
  * HDL (Linguagem de máquina) descreve o circuito desejado, não uma sequência comum de software.
* Exemplos: Filtros de áudio, controle pwm, etc.