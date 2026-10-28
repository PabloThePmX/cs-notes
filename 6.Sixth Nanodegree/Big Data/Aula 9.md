# Aula 9

* Duplicação (deduplicação) de dados.
* Descartar é ruim, mas ficar fazendo retry também é ruim, pois não anda a fila da mensageria.
* Duplicatas não são um bug da pipeline, pode ser da natureza da operação.
* Em computação destruída, a a maioria dos sistemas vai priorizar confiabilidade ao invés de precisão.
* O custo de ignorar duplicatas vai de métricas infladas ou até agregações corrompidas que envenenam os modelos.
* Verificar a fonte das duplicatas.

## Para resolver o problema
* Não existe uma única coisa.
* Entrega At-Least-Once (broker vai dizer que recebeu, pelo menos uma vez)
  * Aguardam uma confirmação (ACK), tipo o handshake.
* Retentativa de Produtores.
  * Problema de webhook, registrando o evento duas vezes quando está com problema transitório (Ex.: em um balanceador de carga).
* Sobreposição entre Snapshot e Stream no CDC.
* Reinícios de Pipeline e Checkpointing.
  * O que acontece ao reiniciar o processo.

## Estratégias de Deduplicação
* Semântica Exactly One (exatamente uma vez).
  * Broker idempotente.
  * Flink também consegue implementar isso.
  * Não impede duplicatas no sistema de origem.
* Deduplicação com estado (stateful).
  * Guarda o estado, deixa salvo o histórico.
* Sinks idempotentes.
  * Se existe, faz um UPDATE ao invés de um insert.
    * No banco em si.
    * `ON CONFLICT DO UPDATE`.
      * O `UPSERT`.
        * Pode ser ruim se vier muitas duplicatas, e fazer um insert + update toda vez pode dar problema de performance.
  * É a última linha de defesa.
  * Cuidado com isso em um pipeline de IOT.
  * At most once (0 ou uma vez) vai remover duplicatas, mas pode remover outras mensagens também.
    * É aceitável para algumas aplicações (como telemetria).
* Deduplicação com janela de tempo.
  * Verifica um determinado tempo (por exemplo, os últimos 10 minutos).
    * Ou seja, verifica apenas as chave em uma janela de tempo.

* Idempotência: Entregar algo mais vezes, não tem problema pois não altera o valor.
* Lamport clock.
  * Ordena eventos sem precisar de um relógio.

## Deduplicação com FlinkSQL
* O FLinkSQL possui um padrão limpo e declarativo para deduplicação usando a função de janela `ROW_NUMBER()`.
  * A abordagem padrão do Flink.
  * As window functions fazem um recorte de uma tabela inteira.
    * Particionar os registros pela chave, ordenar pelo timestamp e deixar apenas o primeiro ou último registro.
  * Da pra usar com watermark do Flink também.
    * Pois é aplicado diretamente no source.
* Gerenciamento de estado.
  * O Flink mantém dados para cada chave única.
    * State TTL (Time to Live).
      * Expira automaticamente depois de um momento definido.
    * Deduplicação por tempo de processamento.
      * Usa `PROCTIME()` em vez de tempo de evento.
        * Uma função do Flink.
        * Tempo de processamento.
          * Horário do cluster que executou.

## Deduplicação no Nível do Kafka
* O Kafka também tem questões para evitar duplicatas.
* Produtores idempotentes.
  * `enable.idempotence=true` para ativar essa configuração.
* Escritas transacionais.
  * Cria uma transação como um banco relacional.
    * Deixa apenas um chegar para consumir.
  * Ou acontece tudo na transição, ou não acontece nada.
  * Fazendo commits e rollbacks.
* Isolamento do Consumidor.
  * Nos bancos relacionais isso é padrão, no ACID.