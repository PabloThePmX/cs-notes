# Aula 12

* O `chrony` é usado para setar a `timezone`.
  * Ou seja, ele vai ser o serviço responsável por sincronizar os relógios e datas dos equipamentos de uma rede.
  * Coloca-lo para inicializar com o sistema.
    * `systemctl enable chrony`.
  * Para validar o funcionamento, usar o `chronyc sources`
  * É importante ter o horário ajustado, principalmente ao se conectar com a internet, pois com isso errado, pacotes não são baixados.
* Existe o comando `ntpdate` que vai sincronizar apenas quando pedir, enquanto o chrony mantém atualizado sempre que o serviço estiver rodando.
* Usando o chrony, setar a timezone com o comando `timedatectl set-timezone America/Sao_Paulo`.
  * Para ver as timezones disponíveis, usar `timedatectl list-timezones`.
  * Usar só `timedatectl` vai mostrar as informações do relógio.
* O objetivo é de transformar a máquina para que possa trabalhar isoladamente, sem precisar usar serviços como de DHCP, DNS, etc da rede que está acessando.