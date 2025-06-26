# Aula 10

* Para criar um app do expo, usar o comando `npx create-expo-app <NOME APP> -t`
  * O template permite que mudamos a linguagem, de js para ts.
    * Neste caso, usamos o `blank`.
* O `app.json` vai ter todas as configurações do app.
* O `index.js` é a raiz, centralizando a inicialização do projeto.
  * É o `App.js` seria como se fosse a home.
* Usar o `npx expo start` para executar o app.
  * Precisei colocar um `--tunnel` para que carregasse.
  * O app do expo precisa estar pelo menos na mesma versão que a dependência dele.
* O React Native usa um objeto de estilo (não é CSS).
  * É `const` e tem vários objetos, onde cada um vai ser um seletor diferente.
  * A tag vai pegar o objeto especificado.
  * Precisa ter o `flex` para definir o tamanho do container.
  * O `alignItems` e `justifyContent` são ao contrário do CSS.
  * Para estilizar inline, usar `style ={{propriedade}}`
* A `StatusBar` vai ajustar os icones da barra superior do celular, mudando a cor, etc.
* A `View` é como se fosse a div do HTML.
* O componente default fica fora do `{}` pois seria como se ele fosse o padrão daquele arquivo.
* O react native espera retornar apenas uma view principal (apenas um item no return).
  * Ou deixar vazio com `<>`.
* O `button` usa o botão padrão do sistema.
  * Geralmente se faz botões com o `TouchableOpacity`.
    * Ele é como se fosse um container clicável.