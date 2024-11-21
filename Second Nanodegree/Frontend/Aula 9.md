# Aula 9

### React
* É uma biblioteca javascript (e não framework)
* Tudo no react é JS.
* Ele manipula o HTML.
* Os componentes são blocos reutilizáveis.
* O ponto de entrada do React (entry-point) é o arquivo `index.js`, dentro da pasta `src`.
  * Ele vai chamar o `<App/>`, que é onde vai ter os componentes.
* Tudo vai acontecer dentro do `root`.
* O HTML fica dentro do JS, chamado de `.jsx`.
  * Os componentes em si são `jsx`, enquanto funções "normais" seriam apenas `js`
* Todo componente é uma função.
  * É o seu nome sempre começa com letra maíuscula.
    * Segue o padrão `PascalCase`.
* Componente sempre retorna HTML.
  * Para retornar um html com mais tags (mais linhas), colocar o `()` com as tags dentro, para dizer que é apenas um return.
* Depois de criar a função, exportá-la, usando `export default Nome;`
  * Podemos chamar o export logo na sua declaração `export function Nome(){}`
* Podemos criar vários componentes (funções) no mesmo arquivo.
  * Essa prática é comum.
* Criar uma pasta dentro do `src`, chamada `components` para armazenar os componentes.
  * Dentro dela, uma pasta do componente, com seu nome em maíusculo, como `Header`
    * E dentro, criar o `index.jsx`.
    * Tudo que for referente a ele, colocar na pasta, como o css do componente.
      * O nome do arquivo css pode ser o nome do componente, para facilitar.
* Importar os componentes com `import {NomeComponente} from caminho/arquivo;`
  * As `{ }` são necessárias apenas quando não há o `default` na exportação.
    * Os `{ }` seriam sub-componentes.
  * Para chama-lo, colocar a tag com o seu nome, `<NomeComponente />`.
* Importar o css, e utiliza-lo com `className` na tag.
  * Para importar, é so botar o caminho do arquivo.
* Para retornar dois ou mais componentes no App
  * Método antigo: circundar as tags do componente com uma tag.
    * Isso é quase uma gambiarra.
  * Método correto: `fragmentos`, circundando os componentes com tags vazias, como `<></>`.