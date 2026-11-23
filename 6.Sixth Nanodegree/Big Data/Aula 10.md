# Aula 10

## Apache Airflow
* Precisa de um banco de dados para funcionar.
* Orquestração.
  * Mapear e verificar um fluxo, e nesse caso, de dados.
  * Possui agendamento de tarefas.
* Foco principal em modelos batch.
  * Pois pode ser refeito/reprocessado (agendamento de tarefas).
    * É mais comum fazer isso no batch, e não no stream.
* Usa o conceito DAG.
  * Directed Acyclic Graph.
    * Grafo direcionado significa que as vertices tem direção.
    * O acíclico tem haver com ciclo, ou seja, nesse caso não tem ciclo.
      * Evita loops.
        * Sem a possibilidade de voltar para passo anterior.
* O grafo é uma representação, trabalhamos com vertices e arestas.
* O AirFlow vai chamar outras plataformas/scripts, como um agendador.
  * Ou seja, vai controlar o fluxo.
    * Tipo um `cronjob` do Linux.
  * Garante a ordem, sequencia, logs e alertas do workflow.
* Usa o python para definir os pipelines.
* Acima do SO, ficando na nuvem.
* A interface é mais para ver os fluxos criados.
  * Pois como comentado anteriormente, o pipeline é em python.
* Diagram de Gantt.
* Da pra setar se vai ser executado diariamente, por hora, etc.
  * Ou por triggers.
* Usam operadores.
  * Sobrecarga de operador para dizer a sequência `>>`.
  * E cada variável desse fluxo, é alimentada com o método/classe com a execução.
  * O operador seria o comando em si (importado da classe `Operators` do Airflow).
    * Da pra criar outros operators.
* Da pra integrar o Airflow com outras coisas externas, como API.
  * Da pra por exemplo, enviar dados para ele via API.
* Um DAG com várias tarefas.
* Da pra criar uma DAG para CI/CD.
* Colocar os scripts DAG na pasta designada.
* A própria interface do Airflow tem os logs.
* `python_callable` é a propriedade que recebe a função python no seu operator.
* `crontab guru` para auxiliar na criação do scheduler.
* Da pra fazer execuções em paralelo com `[task1, task2] >> task3`.
* Task com listeners, tipo tópicos do kafka disparando o pipeline.
  * Vem da lib `sensors`.
  * É `async` pois fica apenas escutando.