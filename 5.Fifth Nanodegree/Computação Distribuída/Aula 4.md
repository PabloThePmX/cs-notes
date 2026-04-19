# Aula 4

## Programação Síncrona
* Sequencial, espera cada tarefa terminar antes de passar para a próxima.

### Vantagens
* É mais simples.
* Facilidade para depurar.
* Previsibilidade.

### Desvantagens
* CPU ociosa.
* Baixa escalabilidade.
* Interface congela.
* Desperdício de recursos.

## Programação Assíncrona
* Múltiplas threads podem ser executadas simultaneamente sem bloquear a principal.
* O `Event Loop` é um agendador inteligente que gerencia as threads em python.
  * Ele funciona no seguinte loop:
    * Ready Queue
    * I/O Operation
    * Context Switching
    * Completed Tasks
    * Ready Queue
* Os métodos possuem o `async` em `async def`.
* Os locais para pausar, utilizam o `await`.