# Aula 5

### Javascript
* Pode ser front e back.
* O mais "convencional" é deixar o js no final da tag body, pois deixando no início pode impactar a performance.
* Chamar no HTML usando a tag `script`.
  * Usar `src` para quando é pra pegar um arquivo de fora.
  * Lembrar de incluir a pasta (caso esteja em uma).
* Podemos declarar variáveis com `let` ou `var`.
  * Usar mais o `let`, pois ele cria dentro do escopo.
    * Ultimamente esse é o que mais está sendo usado.
* Nome de variável pode começar com letra, `$`, `_`.
* JS é case sensitive.
* Podemos interpolar um texto (template literals) usando crase e colocar a variável no `${}`.
* `undefined` significa que a variável existe, mas não tem valor.
* `null` é a ausência intencional de valor.
  * Usado muito pela questão do banco/API.
* Se for necessário inicializar uma variável vazia (não é muito comum de acontecer), é melhor defini-la como `null`.
* ### Tipos de Variáveis
  * Numérico
  * String
  * Bool
  * Null
  * Undefined
  * Symbol: Introduzido no ES6, cria valores únicos, como chaves.
  * Bigint
* Para declarar uma função, colocar `function nomeFuncao(){}`
