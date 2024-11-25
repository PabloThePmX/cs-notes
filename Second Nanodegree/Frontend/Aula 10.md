# Aula 10

* As variáveis são colocadas fora do return (obviamente).
* A arrow function seria apenas uma função sem nome e usada apenas uma vez.
  * `const teste = () => {}`
    * O que vem depois do `=>` é o retorno.
    * O `()` pode receber parâmetros, tipo o `(res)` do `fetch`.
  * Existe diferença no `this` de uma função normal para uma arrow function.
* Para utilizar o valor de uma variável dentro do HTML, colocar chaves e chamar o nome da variável.
  * Ex.: `<h3>{nomeVar}</h3>`

### React Props (um pouco mais antigo)
* Parâmetros para o componente.
* Dentro da tag, passar uma propriedade com seu nome e seu valor para o componente, ou seja, `<Header titulo="Produtos"/>`
* O nome a ser usado na função do componente, costuma ser apenas `props`
  * Ex.:`function Header(props){}`
  * Para ver o valor da propriedade: `<h1>{props.tiulo}</h1>`
* Pode ser função, objeto, outro componente, etc.

### JS Destructuring (desconstrução)
* Desconstrução de objeto, ou seja, pego somente a parte do objeto que me interessa.
* Por exemplo, na função, utilizar `function({titulo})`.
  * Assim vai desconstruir o objeto de propriedade, pegando apenas o valor que é necessário.
  * Da pra atribuir um valor padrão dentro dessa desconstrução, pra que seja usada caso a propriedade vier vazia.
    * Usando React props não tem como fazer isso direto, apenas com `if else` dentro do componente.

### Renderização condicional
* Utilizar if ternário dentro do JSX `<>`.
* Colocar a condição dentro de chaves.
* Da pra colocar como retorno da condição, tags, componentes, etc.
* Para fazer um ternário sem else, usar `&&` no lugar do `?`.
  * Mais comum fazer dessa forma.
    * Ou seja, ao invés de fazer `if else`, fazer dois `ifs`
      * Um dos ifs é normal, e o outro é negado.

### Estados de componente
* Mudança de estado de componentes, Ex.: vazio para preenchido.
  * Salva o estado atual de algo, como valor de variável, objeto de retorno de pi, etc.
* "Atualização" da tela após um valor é alterado, estilo o `OnPropertyChanged` do WPF.
  * Vai renderizar o componente de novo ao trocar o estado.
* Usa desconstrução de array.
  * O retorno do useState é um array, e cada item vai ser atribuído na const.
* Para converter uma variável para tipo de estado, usar o `useState`.
  * Ex.: `const [isLogged, setIsLogged] = useState(false);`
    * O valor inicial é o que vai no `useState()`
      * Pode ser vazio, caso não haja valor inicial.
    * O primeiro item é a variável do estado atual, e o segundo é o "método" que vai atualizar (alternar) o valor com o novo estado (estilo `toggle` do js).
      * Por convenção, o segundo item usa o prefixo `set`.
  * É um pacote, precisa importar.
    * `import{useState} from "react";`
      * Seria como se estivesse importando uma classe, pois useState é um hook.
* Para alterar o estado:
  * Chamar uma função (arrow function) e alterar o segundo item, `setIsLogged(NOVOVALOR)`
    * Usado em onClick ou afins.

### Hooks
* Códigos que podemos reutilizar.
* É algo pra utilizar as mesmas funcionalidades de uma classe.