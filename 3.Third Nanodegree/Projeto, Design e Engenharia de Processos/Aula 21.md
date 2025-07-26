# Aula 21

* A biblioteca `i18next` é usada para traduções.
* `Prop drilling`: Dados que são passados de uma tela a outra.

## Contexto da Aplicação (Context API)
* É um hook, que vai envolver toda a aplicação.
  * Como a lib de navegação.
  * O provider vai circundar.
* Nativo do React.
  * Redux é uma lib externa mais completa que faz essas coisas.
  * Zustand
* Se cria um arquivo para ele.
  * Dentro de uma pasta `context`.
  * Criar contextos específicos, para banco, temas, idiomas, etc.
    * Para buscas do banco, é interessante apenas para quando for um valor que precisa ser usado em várias telas diferentes.
* Provider é o contexto que vai ser exportado.
* O provider retorna o contexto com o children dentro dele.
  * A tag de contexto vai ter os valores que vão ser exportados.
* A prop `children` aceita qualquer valor, tela, etc.
  * Tudo que está circundado pelo provider na tela, esse vai ser o valor do `children`.
* Usar o `useContext()` pra pegar o valor do contexto na tela.
* Geralmente se coloca na raiz do projeto.
* Vai aninhando os providers.
* É como se fosse uma injeção de dependência, pois a tela vai ter aquela informação, mas não vai declara-la.

## Async Storage
* O `asyncStorage` salva como a session.
  * O cache.
* Está ma biblioteca do `react-native-async-storage`.
* É NO SQL, portanto utiliza chave valor.
* Usar o `setItem` e o `getItem` para colocar os valores no cache.