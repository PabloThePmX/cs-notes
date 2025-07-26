# Aula 11

## Triggers
* No postgresql a implementação é um pouco diferente que em outros SGBD (trabalha com dois comandos).
* Vai ser disparada de alguma forma (Disparo automático).
  * Definição de uma ação que é disparada quando um evento ocorre.
* São sempre vinculados a uma tabela.
  * E uma apenas.
* Orientada a eventos.
* Os comandos disparadores são o manipuladores de tabela (DML) (`INSERT`, `UPDATE`, `DELETE`).
  * Quando ocorre ação x na coluna y de uma tabela z, vai fazer algo.
    * Da pra especificar uma coluna ou não.
* Da pra interceptar o comando antes ou depois de acontecer.
* Tem que cuidar com os encadeamentos, pois um trigger pode disparar outra que dispara outra e por ai vai.
* Não pode ser invocado pelo usuário.
* Precisa criar uma função que retorna um trigger.
  * Se for uma `AFTER`, vai retornar nulo, pois por padrão precisa retornar algo, mas como já foi feita a inserção, update, etc anteriormente, vai ser preciso apenas atualiza-la.
    * Porém se for um `BEFORE` vai precisar retornar a linha nova com o `NEW` ou cancelar a operação retornando nulo.
  * A função vai conter a lógica que vai acontecer, e a trigger vai dizer quando a função vai ser disparada.
  * Uma sintaxe básica de um trigger seria mais ou menos `CREATE TRIGGER <nome> <BEFORE|AFTER...> <CREATE|UPDATE|DELETE> ON <tabela> <FOR EACH ROW|STATEMENT> EXECUTE PROCEDURE <funcao>`
    * Pode-se usar `PROCEDURE` ou `FUNCTION`, ambos são equivalentes (porém tem que verificar a versão).
    * O `FOR EACH STATEMENT` diz que vai ser disparada apenas uma vez, ja o `FOR EACH ROW` vai disparar a função para cada linha.
      * Usado mais para auditoria.
    * Somente o `FOR EACH ROW` pode usar `NEW` e `OLD`.
  * A função precisa existir antes da trigger.
* A função pode verificar o valor antigo e o novo, com o `OLD` ou `NEW`.
* Uma trigger não pode ser recursiva.
  * Não da pra fazer a mesma modificação na mesma tabela.
* Race condition.
* Ao usar um `INSTEAD OF`, podemos salvar em uma view, e algum outro banco pegar o valor nessa view e salvar em uma tabela de outra db.
  * Funcionando como se fosse uma ponte, uma API.
* Geralmente não se faz `DELETE`, apenas inativa o registro.
  * Os triggers podem rastrear para impedir `DELETE`.
* Cuidar para sempre usar sequence implícita.
  * Na criação da tabela, quando for um tipo INT, usar o `GENERATED ALWAYS AS IDENTITY`.
* Para facilitar, geralmente se cria o trigger e depois a função.

### Principais Usos
* Geração automática de valores.
* Prevenção de transações inválidas
* Reforçar regras de negócio complexas.
* Prover auditoria.
* Prover logs.
* Restrições para efetuar algum DML.
  * Ex.: Restringir a partir de um horário.