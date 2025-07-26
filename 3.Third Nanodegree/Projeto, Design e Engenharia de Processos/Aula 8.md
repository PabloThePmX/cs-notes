# Aula 8

* Trabalhando com `promises` em js:
```js
//o reject vai ser mostrando quando for erro na promessa
function mostraGremio(resolverPromessa) {
    return new Promise((resolve, reject) => {
        if (resolverPromessa) {
            resolve("Grêmio");
        }
        reject("Time não encontrado");
    });
}

mostraGremio(true)
    .then((resposta) => console.log(resposta))
    .catch((error) => console.error("Ocorreu um erro!", error));

mostraGremio(false)
    .then((resposta) => console.log(resposta))
    .catch((error) => console.error("Ocorreu um erro!", error));
```
* Usar `async` `await` para dizer que a função é assincrona, e que deve pausar naquela parte do código.
* Usar o `fetch` para buscar uma requisição de alguma API.
* Algumas requisições usam parâmetros na URL, usando o `?NOME_PARAM=valor`.
* O `Promise.all()` pode ser usado para chamar um array de promises, ou seja, faz várias requsições de uma vez só.
  * Ele retorna uma lista de respostas.

## Axios
* Podemos usar a lib `axios` para fazer requisições mais facilmente.
* Inicalizar ele no projeto com `const axios = require("axios")`.
  * Ai chamar essa variável quando for necessário utiliza-lo.
* Ele usa os métodos http, como métodos da própria biblioteca.
* Para pegar o valor do body, usar o `.data` do responde, e então caso quiser pegar algo específico do body, usar o `.data.VALORDESEJADO`.

* O `npm init` vai gerar um projeto npm, que vai ter o `package.json`.
  * O `npm install` vai instalar todas as dependências do `package.json`, pois o `node_modules` não vai para o repositório remoto.