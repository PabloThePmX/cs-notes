# Aula 3

### HTML
#### Meta tags
* `<meta name="description" content="lalala" />` coloca a descrição do site no sistemas de busca (Google).
* `<meta name="robots" content="index,follow" />` é um conjunto de de orientações para que os mecanismos de busca entendam se a página deve aparecer nas pesquisas ou não.

#### Tags
* `<form>` para fazer formulários. 
* O `<body>` possui margem de 8px por padrão.
  * Se diz "User agent stylesheet" quer dizer que é coisa do navegador. 

### CSS
* O "." indica que é uma classe.
  * Para adicionar na tag, colocar `class="nome"`
* Usando display block, podemos usar `margin-inline: auto` para dizer que as margens devem ser iguais para cada lado.
  * O que acontece é que usando display block, tudo fica para a esquerda por padrão, então, usando a margem com `inline`, diz que vai definir a margem da linha.
    * Dessa forma, o `auto` vai dizer que ele vai verificar o espaço que sobrou a direita e vai dividir para encontrar o meio, e assim, centralizar.
* `display: block` usa toda a "linha" começando pela esquerda.
  * Usar o `margin-inline: auto` pra deixar ele centralizado.
* Classe utilitária é quando uma classe faz somente uma coisa, como `w-100` que é apenas para setar `width: 100%`.
  * O tailwind e o bootstrap faz bastante o uso disso
* Podemos ter várias classes para uma definição, só precisamos usar a vírgula para separa-las.
* Para que o browser saiba onde deve ir, podemos colocar um id nas tags.
  * Para chamar em algum lugar, devemos colocar o `#` na frente do nome do id.
* Podemos definir o que está dentro daquela classe, seja mudado.
  * `.footer a {}` vai alterar apenas as tags `<a>` dentro da tag que usa a classe footer.
    * Qualquer estrutura, ou seja, se o `<a>` estiver dentro de outra tag dentro do footer, vai funcionar igual.
      * Se quiser que seja filho direto, deverá ser usado o `>`, ou seja `footer > a {}`. 

### Anotações
* Construir o site de fora pra dentro.
* Pexels, pra buscar imagens grátis.
* Margin é pra fora, e padding pra dentro.