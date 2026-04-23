# Aula 7

* O Raspberry Pi é um microcomputador (SBC) completo.
  * Com processador ARM integrado e pinos GPIO para eletrônica.
* É popular por:
  * Baixo custo.
  * Tamanho compacto.
  * Eficiência energética.
  * Comunidade global.
* A ideia nasceu em 2006, mas so lançou em 2012.
  * Tinha como missão a educação inclusiva, empoderamento social e impacto global.
* Além da linha normal, existem os modelos zero e pico.
  * O zero é ainda menor, enquanto o pico não executa OS Linux.
* Raspberry Compute Module (para industria)
  * Uma versão compacta sem portas padrão, projetada para integração em produtos personalizados (embarcados).
  * Ideal para fabricantes.

## SoC e Processador

* System on a Chip (SoC).
  * São integrados CPU, GPU e controladores nesse único chip otimizado.
* Usa arquitetura ARM, que são processadores de baixo consumo.
* Chips especializados em eficiência (Broadcom BCM Series).

## Portas e Redes
* Portas HDMI.
* USB 2.0 e 3.0.
* Ethernet
* GPIO
  * Pinos programáveis para projetos eletrônicos.

### Sem Fio
* Wi-Fi
* Bluetooth

## Pinos GPIO
* General Purpose Input/Output
* Possui 40 pinos.
* Os de entrada recebem sinais de sensores e botões.
* Os de saída controlam LED, motores e atuadores.
* Utiliza os protocolos de comunicação I2C, SPI e UART.
* Trabalha com 3.3V ou 5V.

## Armazenamento e Memória
* Usa um microSB para armazenar o SO.
* O USB 3.0 permite o uso de SSDs.
* O modelo 5 introduziu suporte PCIe para SSDs NVMe.

## SO
* O raspberry possui uma distro recomendada, ela é baseada em Debian e é otimizada para o Pi.
  * Disponível em versões server, desktop e full (com programas extras).
* Porém é possível utilizar outras distros, como o próprio ubuntu.
  * Tendo suporte ao 64bits.
* Outras distros com focos em multimídia (LibreELEC) e consoles retro (RetroPie).
* Para instalar uma OS no Rasp, é utilizado o Raspberry Pi Imager.
  * Ele mesmo envia para o microSD.
* O raspberry permite DualBoot.

## Python
* A linguagem oficial do Pi é o python.
  * A grande maioria das bibliotecas para o mesmo se encontra em python.
  * Existe a IDE Thonny, que é integrada ao SO e mostra variáveis em tempo real.

### Bibliotecas

#### RPi.GPIO
* Controle de baixo nível.
* Mais complexo.
* Importar o modulo `RPi.GPIO` da biblioteca.
* Precisa setar a numeração, que no caso é o `BCM`, usando o código `GPIO.setmode(GPIO.BCM)`.
* Depois setar o pino, e se é input ou output, utilizando o código `GPIO.setup(18, GPIO.OUT)`.
* Para então executa-lo, utilizar `GPIO.output(18, GPIO.HIGH)`.

#### GPIO Zero
* É mais simples e não tão baixo nível.
* Precisa apenas importar o modulo de `LED` da biblioteca.
* Setar o pino do LED com `led = LED(18)`.
* E piscar usando o método `led.blink()`.
  * É possível piscar fazendo um `led.on()` e `led.off()` com um `sleep` entre eles. 
* Para setar o botão, usar o método `bt = Button(2)`, do modulo de mesmo nome.
  * Para esperar ser pressionado, utilizar `bt.wait_for_press()`.