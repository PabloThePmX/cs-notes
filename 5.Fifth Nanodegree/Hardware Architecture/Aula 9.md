# Aula 9

## Flask
* O flask é uma micro-framework para criar apenas o essencial de aplicações web.
* Utiliza o Werkzeug para manipulação HTTP e segurança.
* O Jinja2 é o motor de templates para gerar HTMLs dinâmicos.
* O ideal é criar um ambiente virtual para isolar as dependendencias do projeto
  * Criar utilizando `python -m venv venv` e `source venv/bin/activate` para ativa-lo.\
  * Dentro dele podemos utilizar o pip pra instalar o flask.

### Código
* Enviar o nome da aplicação no construtor do Flask, e salvar essa instancia em uma variável.
* Cada função vai ter um decorator para dizer a rota para acessa-lo, e vai ser utilizado a instancia do Flask.
  * Ou seja `@app.route('/')` acima da função.
  * O retorno da função vai ser o que vai ser enviado.
  * Da pra ter rotas fixas ou dinâmicas.

## Templates Jinja2
* Criar uma pasta chamada `templates`.
* Para utilizar variáveis no html, usar o binding `{{ nome }}`.
* Para lógica `{% if ... %}`.
* E para renderizar, no python usar o `render_template()`.
* Utilizar o `url_for()` para gerar URLs dinâmicas para arquivos estáticos.
* A pasta `static/` é usada para armazenar CSS, imagens, js, etc.