# Aula 13

## Locks
* Precisa ter lock para que não perca dados, pois se há duas pessoas mexendo no mesmo local, um pode sobrescrever o outro.
* Evita que alguém "passe na frente".
* Dirty read: leu algo que não foi commitado ainda.
* O primeiro que executar, vai bloquear o registro alterado até que seja feito o `ROLLBACK` ou `COMMIT`, liberando esse registro para ser alterado em outras transações.
* Locks explícitos em nível de linha: `FOR UPDATE`, `FOR NO KEY UPDATE`, `FOR UPDATE SKIP LOCKED`, etc.
  * Isso é feito de maneira automática, porém se quisermos podemos fazer explicitamente.
  * Com o lock implícito, pode-se fazer o lock é na coluna, e não no registro.
    * Porém geralmente é no registro, e se for um DELETE, vai sempre ocupar todas as colunas.
  * 