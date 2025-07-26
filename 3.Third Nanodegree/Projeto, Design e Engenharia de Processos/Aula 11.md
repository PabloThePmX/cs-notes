# Aula 11

* O `onPressOut()` vai executar uma função logo após que o click for realizado no `<Pressable>`.
  * Também tem o `onLongPress()`, que vai ser executado apenas quando for pressionado por mais tempo.
  * Costuma ser usado com expressões lambda.
* O `<SafeAreaView>` define a área "útil" sem contar a parte de cima e a de baixo.
  * Nem sempre funciona.
    * Costuma funcionar em Iphone.
  * Funciona como uma view.
  * Se não funcionar esse `SafeAreaView`, vai ter que ser feito um `paddingTop` manualmente.
* Usar o `<ScrollView>` para dizer que aquele trecho pode mexer.
  * Para retirar a scroll bar da lateral usar a propriedade `showVerticalIndicator` com false.
  * Não é indicada para dados dinâmicos, que vem do banco de dados por exemeplo.
    * Para isso, usamos a `<FlatList>`
* Para criar um card, podemos usar um `map` em um array que tenha os itens, e esse map vai retornar uma `View` que vai ter o card com o item atual da coleção.
  * O `map` precisa ser usado para poder retornar o item.
  * Porém o aconselhado é utilizar a `<FlatList>`.
* O `<FlatList>` usa diversas propriedades para gerar uma lista com scroll.
  * Cada item terá uma chave. valores e a sua renderização.
    * A renderização vai retornar a lista.
  * Tem a opção de fazer um scroll infinito.
    * Dessa forma ele carrega x itens primeiro e depois vai carregando o resto conforme é feito o scroll.
    * Também tem a funcionalidade de fazer refresh no topo da tela.
    * Isso tudo são atributos do `FlatList`.
  * Da pra tirar a scroll bar da mesma forma que a `ScrollView`.
* A `<Image>` precisa ter definida o `source` (`URI`), `height` e `width`.
  
## Hooks
* O `react` (não o native) é onde devemos importar os hooks.
* Usa os hooks da mesma forma que o react normal.
* O `useState` tem o metodo que vai setar o atributo.
  * Ambos são declarados com alimentação do `useState(0)`, o 0 sendo o valor default (define dessa forma um valor numérico).
  * E a função `set` vai setar o novo valor enviando por parâmetro.
  * O valor não pode ser alterado manualmente, pois é readonly, ou seja, só pode atualizar pela função.
* Como o valor do useState é uma `const`, tem que usar as `{}` para mostrar o seu valor, visto que ele é js.
* No input, usar o `onChangeText` com a função set, para atualizar o valor do hook.
* O `useEffect` vai ser disparado ao carregar a tela (depois de carregar os componentes gráficos).
  * Ele recebe por parâmetro, uma função e um array vazio.
    * O array é alimentado com o valor que queremos "monitorar", vazio, vai executar apenas quando finalizar tudo.
* Existe também o `useLayoutEffect`, que executa antes do `useEffect`, durante a montagem da tela.