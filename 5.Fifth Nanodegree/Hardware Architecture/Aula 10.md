# Aula 10

* A raspberry pi possui 40 pinos, entre eles:
  * 28 pinos de entrada e saída com tensão máxima de 3.3V.
  * 8 GNDs (grounds).
  * 2 pinos de 5V.
  * 2 pinos de 3.3V.
* Nativamente leem e escrevem dados digitais, a não ser que haja um conversor em pinos com protocolo SPI.
* Utilizar o comando `pinout` para ver o número dos pinos.
  * Ao utilizar o `RPi.GPIO`, usar os valores do BCM.
* Com o `RPi.GPIO`, usar o método `GPIO.cleanup()` para redefinir as configurações setadas nos pinos.
* A raspberry possui resistores internos que podem ser ativados via software.
  * PULL-UP: O pino de leitura é conectado diretamente ao pino 3.3V, e enquanto o mesmo não estiver sendo pressionado, o valor é sempre `HIGH`.
  * PULL-DOWN: O pino é conectado ao GND, e o mesmo quando não estiver sendo lido, o valor vai ser sempre `LOW`.
  * Para setar isso no código, colocar no setup `GPIO.setup(pushbutton_up_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)`.
    * Para usar o Pull Down, utilizar `PUD_DOWN`.