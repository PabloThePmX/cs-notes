# Aul1 13

## Navigation
* Instalar a biblioteca do `react-navigation`.
  * Para usar a stack navigation instalar a `react-navigation/stack`. (ou `react-navigation/stack-native`)
    * Para que seja uma navegação em pilha.
* Precisa instalar as dependências `react-native-screens` para as transições, e o `react-native-safe-area-context`.
* Para usar os comandos de ir e vir, instalar o `react-native-gesture-handler`.
* Par usar a navegação, é necessário setar um container para a aplicação, com o `NavigationContainer`.
  * Usar também a função `createStackNavigation`.
    * Necessário injeta-la em uma constante (que precisa ser PascalCase, por se tratar de um componente).
      * Pode-se criar várias stacks, umas apenas para telas que necessitam autenticação, outras que não, etc.
  * A aplicação precisa estar dentro desse `NavigationContainer`.
* Cada stack pode ter um profile, para separar as telas por funções.
* A navegação deve ser uma das primeiras coisas a ser definida ao criar um app.
* Dentro do container, criar as tags das constantes de stack, com o `.Navigation`, como em `<StackApp.Navigation>`.
  * E para definir uma tela, usar o `StackApp.Screen` com o `name` e o `component`.
    * Ao fazer a ligação, precisa chamar o nome que foi definido aqui.
  * Da pra definir o início da rota com o `initialRouteName`, sendo essa uma propriedade do `Navigation`
* O react navigation vem com um header por padrão.
  * Na tag da tela de navegação, da pra setar as `options`, e uma dessas opções pode ser o `headerTitle`.
    * Nas opções da pra desabilitar ele na tela especificada.
    * Como as cores, estilo, etc.
  * É recomendável criar um header próprio, e nao depender desse.
* As telas precisam receber a navegação via props, que será injetada.
  * Com esse atributo, usar a função `.navigate(<NOME DA TELA QUE VAI IR>, <PARAMETROS, COMO UM OBJETO>)` da propriedade.
* Como é uma pilha, as telas vão sendo renderizadas uma em cima da outra.
* Usar a prop de `route` para buscar os parâmetros da rota.
  * Usar o `.params` e desconstruir esse objeto.
* Usar a função `goBack()` para voltar na tela anterior.
  * O `pop()` remove a tela da pilha.
* Para navegar com botões da parte inferior, usar a lib `bottom-tabs`.
  * Usar como foi feito com as stacks, porem dessa vez injetar a `createBottomTabNavigator`.
  * Criar uma tag `Tab.Navigator` com várias Tab.Screen que serão os botões.
    * Cada tab vai buscar pela função que contem a navegação em pilhas.