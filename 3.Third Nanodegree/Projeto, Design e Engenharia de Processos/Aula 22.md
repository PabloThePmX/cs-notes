# Aula 22

* O `fetch` é nativo do JS.
* Criar a informação da API com o `create` do `axios`.
  * Importa essa interface para ser usada.
  * Ela vai fazer a injeção do axios.
* Precisa fazer um `await` na chamada do axios (obvio).
* Tentar tratar a maior parte dos erros no front, para que não fique realizando tantas requisições a toa.
* Se não retornar sucesso, pegar o erro pelo `try-catch`.
* As chamada de autenticação podem ficar no contexto, para que a sessão fique salva.
  * Pois vai continuar com o token autenticado.
* Nas rotas, fazer um ternário verificando se tem usuário logado, se tiver, ele vai mostrar as telas, se não, vai direto na tela de login.
  * Ou seja, pode-se ter um arquivo apenas para as rotas, com o `routes`.
* Fazer um `parse` da resposta.
  * Usar o  `stringfy` para transformar em JSON. 
* Dentro do contexto de autenticação, colocar um loading para dizer se já finalizou o login ou não.
  * Dai colocar o `Active Indicator`.
* Tratar pelas rotas e pelo `useLayoutEffect`, para ver se o usuário tem acesso na tela que foi chamada.

## Async Storage
* Setar o usuário após o login.
* A chave costuma possuir um `@` na frente do nome.
  * Cada app tem seu cache, mas por padrão ainda se usa o nome do aplicativo no nome da chave.
* Dai no `useEffect` buscar pelo token com o `getItem`.
