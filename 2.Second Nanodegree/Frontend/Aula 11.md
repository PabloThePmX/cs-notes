# Aula 11 - Revisão Prova

## NodeJs
* Roda JS no PC.
* Vem com o `npm`
  * Gerenciador de pacotes do node.
* O `npm install` vai pegar as dependências do `package.json` e baixar para o computador.
  * Cria a pasta `node_modules`.
    * Não subir pro git (colocar no `ignore`).

## Vite (existe também o `react create app`)
* Cria uma configuração inicial para rodar uma aplicação localmente (`boilerplate`).
  * Cria templates para vue, react, etc.
* Precisa do node.

### Js
* `setTimeout()`: Recebe dois argumentos, uma função e a outra é quanto tempo vai esperar até executar essa função (em ms).
* Desconstrução de Array: um array é separado e armazenado separadamente em outras variáveis.
  * O `useState` é um exemplo disso, pois ele retorna um array com dois itens, e assim os valores dos itens são associados aos dois itens definidos no const.
    * Primeiro item do array contém o valor, e a segunda contém uma função para alterar o valor.
* `fetch` vai chamar a API.
  * Faz requisições assíncronas, e retorna uma promise.
    * Promise: algo que não sabemos quanto tempo vai levar pra terminar, ou se vai realmente terminar.
  * Precisa esperar a promise ser resolvida do fetch (usando o `then`)
    * Existe 3 estados dela: pendente (pending), concluída (fulfilled) e rejeitada (rejected).
    * Se der problema, podemos pegar com o `catch` depois do `then`
  * Caso entrar no `then`, executar uma arrow function com o parâmetro `response`.
    * Converter essa resposta em `json`.
      * Porém essa conversão também é uma promise, portanto é preciso fazer mais um `then`
        * Nesse `then` executar uma arrow function que vai receber os dados (variável `data`)
          * Essa variável vai ter a resposta da api, usando o `.value`.
        * Possível desconstruir a `data` e pegar diretamente o valor, ou seja, nos parâmetros da arrow function, colocar `({value})` pois ele vai pegar apenas o item `value` da reposta.
  * Se não quisermos usar o `then` podemos usar `async` e `await` (js assíncrono).
    * Foi criado para simplificar o `fetch`.
    * A função precisa ser declarada como `async`, em arrow functions ficaria `const teste = async () => {}`.
    * O fetch é feito com o `await` na frente, para esperar a resposta.
    * Ele vai retornar diretamente a resposta.
      * Fazer um `await` ao transformar essa reposta em `json` também.
    * Tratar erros usando o bloco `try-catch`.
* `setInterval()`: Vai executar uma função a cada x tempo.
* Spread: permite que um array (ou objeto) ou item dele, seja copiado para outra variável. 
  * Usa a sintaxe `...` 
  * Usa-se para fazer merge de listas.
  * Podemos pegar um ou mais itens de um array e salva-los em outra variável.
  * Pode pegar um valor específico e salvar em uma variável (Ex.: `const numbers = [1, 2, 3, 4, 5, 6]; const [one, two, ...rest] = numbers;`, onde os primeiros dois valores são colocas em variáveis e o resto é colocado em um outro array).
  * Muito usado em desconstrução de arrays.
* Js assíncrono: é uma técnica que permite que uma tarefa seja executada enquanto outras ainda estão executando.
  * Precisa usar o `async` e usar o `await` para dizer que mesmo sendo assíncrona, ele precisa esperar pelo retorno de algo a partir daquele ponto.


## React
* Usado para reaproveitar códigos, pois são criados componentes universais.
* `jsx`: Um formato que colocamos `html` dentro do js.
* `hook`: Métodos capazes de controlar o ciclo de vida de alguns componentes (`useState`, `useEffect`, etc)
* Para exibir uma variável no html do jsx, é necessário colocar a mesma dentro de `{ }`.
* O React só renderiza a tela quando o estado é alterado.
  * Ou seja, mesmo tendo a variável alterada no JS, esse novo valor não é mostrado na tela até que o estado seja alterado.
  * Fazer esse gerenciamento de estados usando o hook `useState`
    * Para declarar `const[variavel, setVariavel] = useState("Valor Inicial")`
      * Assim, quando queremos que o valor alterado seja refletido na tela, fazemos a alteração usando o `setVariavel()` enviando por parâmetro o novo valor.
    * Precisa importar o `useState` do react
  * Estado é diferente de variável.
* `useEffect`: É como se fosse o `onLoad` do componente (ou quando o componente é destruído, não está mais na tela, uma variável troca de valor etc).
  * Recebe dois parâmetros, sendo o primeiro a função, e o segundo um array (geralmente vazio) `[]`.
    * Utiliza arrow functions para a função.
  * Não aceita funções assíncronas.
    * Porém podemos fazer uma arrow function que chama a função assíncrona.
  * Ele fica `monitorando`, e para dizer o que monitorar, passar o valor no array, se for vazio, funciona como onLoad.
  * Precisa importar também.
* É comum ter constantes com funções no react (usando arrow functions).
  * Elas podem ser chamadas em métodos `onClick` e afins (`onClick={constDefinidaComFuncao}`).
* Na hora de importar, as `{}` são usadas em componentes que não forma exportados como default.
* Para renderizar listas, dentro do html `<ul>`
  * Fazer um `map` (que é uma função que aplica algo a todos os itens da lista) em uma lista
    * Dentro dos parâmetros do `map` fazer uma arrow function recebendo o item da lista e colocando o mesmo dentro do `<li>`
      * Ou seja, ele vai pegar cada item, e vai colocar ele dentro de tags `<li>`.
      * Como se trata de uma const js, usar `{ }` quando for trabalhar com ela.
    * Cada `<li>` precisa de um atributo de `key` que vai usar o id presente na lista.
* Renderização condicional: Early return no componente.
  * Já o retorno do jsx só permite if ternário.
    * Usar `&&` para fazer um ternário sem else.
* Ciclo de vida de um componente:
  * Inicialização
  * Montagem
  * Atualização
  * Destruição
* `ContextAPI`: Armazena um estado para poder ser lido por qualquer componente do React (Ex.: vai ler o contexto para saber se está logado).
* `React-Router-Dom`: vai definir as rotas dos componentes, e vai permitir a navegação entre os mesmos, dizendo para onde deverá navegar ao clicar em um botão.