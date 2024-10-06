# Aula 7

## Revisão
### HTML
* HTML é a estrutura.
* `Index` é a página inicial, como um main.
* A estrutura basica do HTMl é:
  * `<!DOCTYPE html>`
  * `<html>`
    * `<head>`
      * `<title>`
    * `<body>`
* HTML semântico é quando separamos a página em várias seções, como `header`, `section`, `main`, `footer`, etc.
* Podemos ter vários `header` ou até mesmo `footer`, pois podemos ter cabeçalho e rodapé para cada seção. 
* O `main` vai ter o conteúdo principal da página.
* A tag `<nav>` vai ter o menu.
* A tag de link (`<a>`) vai ter a propriedade `href` contendo o link para ser redirecionado.
* Propriedade `alt` para descrever a imagem.
  * Se deixar apenas a propriedade vazia, caso a image não carregue, o navegador vai entender que pode ignorar essa imagem pois não tem tanta relevância.
* Caminho relativo e absoluto.
  * Relativo: O caminho do arquivo no PC, e ele é relativo ao documento atual.
    * Ou seja, se não especificar nenhuma pasta, ele vai considerar que está na mesma pasta..
  * Absoluto: Uma URL, algo que cada um pode acessar ao enviar o caminho.

### CSS
* Estiliza o HTML.
* Para adicionar no HTML, podemos usar a tag `<style>` a propriedade `style` ou chamando com `<link>` declarando a propriedade `stylesheet` (rel).
* Classes são definidas com o `.` no início do nome.
  * Chama com a propriedade `class` dentro da tag.
* Ids são definidos com o `#` no início do nome
  * Não devemos ter dois ou mais elementos com o mesmo Id.
* Para estilizar todas as tags, é só necessário colocar o nome dela no css.
* Seletor vai selecionar os elementos HTML para aplicar o estilo.
  * O nome da propriedade no arquivo de estilização.
* `font-family` para alterar a fonte.
  * Fontes fallback, são aquelas fontes reservas.
  * Para mudar a cor da fonte, utilizar `color`.
* Box Model
  * `Margin`
    * Espaço da borda, pra fora.
  * `Border`
    * A borda em si.
  * `Padding`
    * Espaço da borda, pra dentro.
    * Ao aumentar o padding, vai deixar ele mais próximo do centro, e longe da borda.
  * Content
* Responsividade, adaptação a tela do usuário.
  * Mobile first.
* Media Queries, seriam as regras de acordo com alguns fatores (características) da tela, como largura da tela, etc.
  * `@media (max-width:600px) seletor {}`
* Flex box é uma forma de organizar as coisas na tela.

### Javascript
* Interações da página.
* Ao final da página, podemos chamar o arquivo js, ou dentro da tag `<script>` 
* `let` ou `var` para criar variáveis, e `const` cria uma constante
  * Dentre as variáveis, é melhor utilizar `let` pois cria apenas dentro do escopo (e `const` também).
  * É melhor sempre criar atribuindo um valor.
* Podemos usar `===` para igualdades, e dessa forma comparamos tanto o valor, como o tipo, pois `==` compara apenas o valor.
* Loops com `for` `while` e `do while`.
  * O `foreach` pode não ser considerado, pois ele precisa de um array para ser executado.
* Para criar array `let novoArray = [];`
  * Para adicionar um item no array `novoArray.push(item);`
* Tipos de dados: `string`, `number`, `boolean`, `null`, `undefined`, `symbol`, `bigint` (essas duas últimas são pouco usadas) e objetos em si.
  * O `null` é a ausência de valor.
  * O `undefined` é a falta de um valor, não definido.
* Função é igual método (código que podemos reutilizar).