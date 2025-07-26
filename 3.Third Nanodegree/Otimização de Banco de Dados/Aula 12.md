# Aula 12

* No banco, uma linha com colunas se chama tupla.
  * É só a resposta dos dados que foram retornados, sem que aloque um espaço na memória como um vetor..

## Transações (ACID)
* ACID
  * **A**tomicidade - Tudo precisa funcionar, se não, nada vai ser executado. (como um condicionamento com AND, tudo ou nada, commit ou rollback).
  * **C**onsistência - Transações isoladas preservam a consistência do banco.
  * **I**solamento - Uma transação não deve interferir nas outras.
  * **D**urabilidade - Persiste as alterações de transações que deram sucesso, ou seja, se deu sucesso é garantido que vai estar salvo.
* Existe em banco relacionais, e alguns não relacionais (MongoDB).
  * Precisa ser ACID compliance.
* Concorrência a recurso (execução concorrente).
  * Race condition.
    * São problemas em sistemas multiusuário.
* Monousuário ou multiusuário (multiprocesso).
  * Como o UNIX, com várias "contas" no PC.
  * Monousuário é single core.
* Como se fosse um bloco lógico, capaz de voltar ao estado anterior a execução desse bloco em caso de erro.
  * Ou seja, a transação assegura que o processo seja completado ou não.
* O sistema que o PostgreSQL usa para garantir a integridade chama-se WAL.
  * Essa camada de código que fica verificando as ações realizadas no banco, guardando em logs.
  * Elimina o registro após verificar que deu certo.
* Uma transação é uma sequência de operações que são tratadas como um bloco único e indivisível (atômico).
* `Commit` "manual".
  * No pgadmin, tem o `auto commit` por padrão.
    * Ou seja, vai executar cada comando em transações separadas.
* O `SELECT` não tem trava, pois não está modificando os dados.
* No `postgres` usa-se o `BEGIN` para dizer quando vai iniciar a transação, e `COMMIT` ou `ROLLBACK` para finalizar.
  * No Oracle não tem comando de inicio.
  * Se for fazer isso, desabilitar o `auto commit` no pgadmin.
    * Da pra setar um valor padrão com o `\set AUTOCOMMIT off` na linha de comando da DB.
    * Dessa forma, vai salvar apenas na conexão, e so vai enviar para o banco com o commit.
* As APIs também possuem a opção de desabilitar o `auto commit`.
* Da pra criar procedures como transações separadas.
* Da pra usar `SAVEPOINTS` na transação, para poder retornar a pontos anteriores.
  * Tipo um checkpoint.
  * Ex.: `ROLLBACK TO SAVEPOINT point2`.
  * Não é muito usado, pois é mais recomendado deixar as transações menores, para ser mais fácil de debugar. 
* Estados de uma transação
  * Active
  * Idle
  * Idle in transaction: iniciou mas não emitiu nenhuma consulta na transação.
  * Idle in transaction (aborted): a transação foi iniciada, mas encontrou um erro e reverteu.
* Usar o `pg_activity` para listar os processos realizados no banco no terminal.
  * Da pra verificar as atividades por PID.
    * Da pra fazer um `SELECT` para finalizar um PID específico.
* Dead lock
  * Uma transação trava pois depende de outra, etc.
  * Cada transação fica esperando e não consegue finalizar.


### MVCC (Multiversion Concurrency Control)
* Para gerenciar a execução simultânea de transações, usa-se o MVCC.
  * Significa que cada transação executada simultaneamente, vão estar visualizando a mesma versão do banco.
    * Cada um tem a sua versão.
    * Vai ser apenas "visto" que foi alterado, no momento do `commit`, assim, as outras transações verão essa nova versão. 
* Podemos configurar para quando existe uma disputa por um registro, vai esperar ou lançar um erro (estados da transação).
  * Se ele esperar, ele pode fazer um `commit` ou `rollback` posteriormente.
  * Por padrão ele vai esperar.
    * Para não esperar, usar o `NO WAIT`.
* Tem que ter cuidado para que se esperar, não ocorra problemas por ficar com muitas transações penduradas.