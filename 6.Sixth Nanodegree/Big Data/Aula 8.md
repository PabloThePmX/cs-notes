# Aula 8

* Datastream -> TableAPI -> PyFlink (FlinkSQL)
* `DataGen` em `PyFlink`.
  * Um conector tipo o `Faker`.
    * Mas gera dados ainda mais aleatórios, sem filtros como o `Faker`.
* Destrinchar dados, de alguma forma.
  * Verificar onde vai separar, quais critérios.
* Executar o binário do flink, para colocar um job no ar.
  * `/opt/flink/bin/flink run -py rabbit.py`.
* Dentro do python, precisa declarar as bibliotecas do java.
  * Visto que foi escrito para o Java.
  * O python é apenas umas interface para ele.
* No dashboard do flink não deixa mandar em python, apenas JARs.
  * Dessa forma, o job precisa ser mandado via CLI como visto acima.
* Montar o pipeline no python.
  * Esse é o job que vai ser executado nele.
  * Source, data, sink, etc (depende do connector, do que ele tem).
    * O RMQ é para o RabbitMQ.
      * Ele chama o connector do java.
        * Por isso ele precisa existir, precisa ter o jar dele.
* SQL & Table API tem connectors diferentes do do datastream.
* No python ele precisa pegar o ambiente de execução.
* Pegar um datastream, transformar para Table API e ai sim trabalhar.
  * É o mais comum.
* Pelo `env`, da pra dar nome para o pipeline.
  * Nome do job do Flink.
* `INSERT ON CONFLICT`.