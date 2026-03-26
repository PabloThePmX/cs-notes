# Aula 25

* para encontrar os ips da rede usar o netdiscover - r
* nmap -sV IP para ver qual o tipo da maquina
* msfconsole para abrir o metasploit framework
  * search portscann
  * use para selecionar uma opção apresentada
    * auxiliary()
  * show options
  * SET RHOST para setar o alvo
  * run para rodar o escaneamento de portas abertas
  * search para verificar uma porta especifica, ou tipos de servicos
    * Ele vai buscar os exploits
    * vai procurar pelas palavras, por exemplo unix + serviço
  * Lhost para fazer shell reverso, colocando o host da maquina com a porta que está escutando
    * SET LHOST
    * L de local
    * auxilia usando portas padrões pois com elas o firewall deixa passar (80, 443, etc)
  * show payloads para ver aqueles que são compatíveis com o modulo
    * set payload NUMERO para setar um desses payloads
  * msfvenom para criar um malware disfarcado de arquivo
  * meterpreter é limitado pois é um cmd normal (em maquinas mais recentes da pra tentar usar o powershell)]
* python -m http.server 8080 para subir um servidor web python
  * Acessar pelo IP.
* zaproxy permite escanear uma url
  * Ele fica entre o usuário e o site, escaneando as requisições e tentando atacar.
  * Funciona como um proxy mesmo.
  * Faz muitas requisições, portanto pode travar.
* php reverse shell
  * ediatar o ip e a porta
    * Colocar do kali
  * da pra tentar colocar um desses em um upload que salva na maquina, dessa forma sabendo o caminho da pra executa-lo
* o site cosumta ficar em var/www/ e a config do servidor no /etc
* no tmp todo munod tem permissão de leitura e execução, como no windows
* linpeas e winpeas para detectar as vulnerabilidades em um pc, para tentar escalar os privilegios (rodar no tmp pois pode executar)
  * conseguir o root da maquina
* proxychains antes do comando para fazer via vpn
  * ou tor (systemctl start tor)
  * precisa do tor pra funcionar
* proton ou vpnbook (openvpn e baixa o bundle do país) tbm