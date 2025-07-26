# Aula 19

## Firebase
* Backend pronto feito pela Google.
* Dividido em módulos, como Auth, Cloud Functions, Cloud Storage, Hosting, Realtime Database (Web Socket), etc.
* Bando de dados NoSql.

## Supabase
* Open Source.
* Funciona da mesma forma que o Firebase.
* Porém usa bando de dados relacional.
* Possui diversos providers de autenticação.
* A parte de autenticação é feita usando uma tabela de Auth, que vai ser referenciada por uma outra tabela de usuário.
  * Essa tabela de Auth vai ser controlada e configurada pelo Supabase.
* O storage usa buckets.
* Bom para criar MVPs.
  * Pois é mais ágil para criar.

### No projeto
* Instalar via npm.
* Criar um arquivo de configuração para ele.
  * Usar o `createClient`.
  * A configuração mais simples usa a url e a key.
* Usar o módulo de Auth para fazer a parte de login/registro.
  * Esse modulo está dentro do cliente configurado.
  * Vai ter `sign up`, `sign in`, etc.