# Aula 20

* Duas métricas de desempenho:
  * Vazão (throughput).
    * A quantidade de tarefas que podem ser resolvidas em um determinado tempo.
  * Latência: Tempo de resposta ou execução.
* MIPS:
  * Milhões de Instruções por Segundo.
  * Medidas de Throughput.
  * Não deve ser usado na comparação entre arquiteturas distintas.
* FLOPS
  * Operações em Ponto Flutuante por Segundo.
  * Medida de Throughput.
  * Mede operações e não instruções.

## Benchmarks
* Programas usados para avaliar o desempenho de sistemas operacionais.
* Tipos: Aplicação, Sintéticos.

### Aplicação
* Execução de aplicações reais.
* Jogos, compilação do kernel do Linux.
* Fornecem resultados próximos ao real.

### Sintéticos
* Conjunto de aplicações que tentam simular a aplicação real.
* Toy Benchmark, Passmark.

## Pipeline
* Pipeline de instruções.
* Enquanto algo é executado, outros também são executados.
  * Não precisa terminar para ir para o próximo.
  * Vários estágios em paralelo.
  * Semelhante a uma linha de montagem.
* Pipeline perfeita: O momento em que todos os recursos possíveis estão sendo usados.
* Dois estágios de uma instrução (simplificada): Ler e executar a instrução.
* Existem momentos durante a execução de uma instrução em que a memória principal não está sendo executada.
* A maioria dos pipelines atuais tem mais que dois estágios.
  * Com dois, ele pode ficar esperando uma instrução finalizar, e acaba ficando parado igual.
* Pipelines atuais geralmente tem 6 estágios, mas podem ter 15, 20, ou até 30 estágios.
* Os 6 tipos de estágios:
  * Fetch Instruction (FI)
  * Decodifica a instrução (DI)
  * Calcula operandos (CO)
  * Obter operandos (FO)
  * Executar instruções (EI)
  * Escrever operandos (WO)
* Nem sempre uma instrução passará pos todos os estágios.
* Pode ter desvio condicional.
* Não melhora a latência de uma única tarefa, mas melhora o throughput de todo o trabalho.
  * O tempo de execução de uma tarefa é o mesmo, com ou sem pipeline.
* O ganho começa a existir a partir da segunda tarefa.
* Conflitos (ou hazards) são situações que impedem que uma instrução planejada possa ser executada no ciclo de clock previsto.
  * Para solucionar, é necessário parar o pipeline (stall).
  * Conflitos Estruturais: Quando tenta utilizar simultaneamente um mesmo recurso de hardware.
    * Para solucionar: Reordenar, atrasar a busca de instrução, utilizar memórias de dados/instruções distintas.
  * Conflito de Dados: Ocorre quando uma instrução depende de um dado da outra, e ela ainda não finalizou.
    * Para solucionar: stall, bypass, reordenamento.
  * Conflito de Controles: Quando uma instrução de desvio (if, branch) é executada e pode alterar ou não o valor do PC (Program Counter).
    * Para solucionar: Adiantar a decisão do desvio de um estágio ou stall.

### Superpipeline
* Permite um aumento no desempenho do processador por ter duas tarefas executadas em um único ciclo de clock.
* A implementação de que técnica permite um aumento no desempenho do processador por ter estágios que executam tarefas em menos de meio ciclo.
* Quebra estágio em sub-estágios. Estágios menores demandam menos tempo para serem executados.
* Estágios menores demandam menos tempo para serem executados. Período menor e frequência maior.

### Superescalar
* A arquitetura superescalar possibilita a replicação de componentes internos do processador, de modo que se possa colocar várias instruções em cada estágio do pipeline.
* Possibilita a execução de instruções em pipelines paralelos.
  * Técnica de implementação que permite que várias instruções sejam iniciadas simultaneamente.
* Maneja várias instruções em cada estágio, o número máximo de instruções que ocorrem em cada estágio denomina-se o grau n.