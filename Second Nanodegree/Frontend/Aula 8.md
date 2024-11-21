# Aula 8

* Operações Assíncronas: operações que não sabemos se vai funcionar, e funcionar, quando vai terminar (`promises`).
  * Roda em paralelo (outra thread), pois precisamos esperar a resposta de algum lugar.
* DOM: estrutura do HTML que fica na memória.
  * Manipulação de DOM.
* O `<form>` detecta quando a pessoa clicou o enter (o evento de enviar um formulário).
  * Além de delimitar que é uma área de formulário.
* Tudo possui um evento.
* O `<button>` pode ser um método de `submit` usando o `type="submit"`
* No JS, ao fazer referências (pegar pelo id), utilizar `const`, pois a referência não muda.
* O `querySelector` é mais genérico, ou seja, não necessariamente precisa buscar por um Id.
* O `addEventListner` vai escutar e e dizer quando o elemento do DOM teve um evento disparado.
  * O primeiro parâmetro, é o tipo de evento que estamos escutando.
    * Ex.: `submit`, `click`, etc.
  * O segundo, é a função a ser disparada.
    * Por parâmetro na função de callback, podemos usar o `event` para receber o evento que disparou a função.
* Evitar chamar a função diretamento dentro do HTML, como `onsubmit` e afins.
* O `callback` é realizado quando é passada uma função por parâmetro para outra função.
* O comportamento padrão do navegador quando é disparado um evento submit, é de recarregar a página.
  * Usar o `event.preventDefault()` (ou `e`) para previnir que esse comportamento padrão seja executado.
* Para chamar um servidor (api), usamos o `fetch`, e ele retorna para nos uma `promise`.
  * É uma `promise` pois não sabemos se vai realmente retornar. 
    * Possui três estados
      * `pending`: está processando.
      * `fulfilled`: retornou com sucesso.
      * `rejected`: o processo foi rejeitado.
    * Usar o `.then()` no retorno, pra executar quando a promise for resolvida.
      * No parâmetro, podemos buscar a `response` e também executar uma função callback.
      * Transformar a `response` em `json`.
        * Fazer isso e retornar.
        * Vai retornar uma nova promise.
      * Colocar mais um `then()` depois de fazer o callback, pois como o retorno desse callback (o json) também é promise, precisamos esperar.
        * Fazer mais um callback nesse segundo `then()`.
          * O parâmetro desse then, vai ser o valor que foi transformado em json, ou seja `then(function(dados){});`  
  * Por ser assíncrono, roda em paralelo, em outra thread.
* Usar `template strings` para ficar dinâmico.
  * Colocar o valor do input na URL.
* O `innerText` apenas exibe o texto, enquanto o `innerHTML` renderiza caso existir html presente o texto enviado.
* Usar a `desestruturação` (ou desconstrução) em JS para pegar apenas as propriedades desejáveis.
  * Colocar nos parâmetros da função de retorno, criando uma const com `.then(function({nomeProp1, nomeProp2})){}`.
* API ViaCEP para buscar CEPs.