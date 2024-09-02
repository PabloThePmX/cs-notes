# Aula 4

* A declaração do CSS se chama seletor.
  * Se usar o `.` vai ser uma classe.
  * Se não usar nada, vai ser a tag.
    * Usar apenas quando alguma tag do site tenha SEMPRE o mesmo padrão, ou seja, usamos para padronizar.
  * Se usar o `#` vai ser um id.
* AMP do Google para deixar mais performático.
  * Mas está caindo em desuso.
* A porcentagem é sempre relativo a aquilo que o objeto está "dentro".
* Fontes são pesadas, por cada caracter é um símbolo.
* Us

### Tipos de Escrita de CSS
* ### Interno
  * É mais performático, por não precisar requisitar o arquivo do css de fora. 
    * A renderização em si fica mais rápida.
  * Não fica no cache.
    * Não carrega tão rápido.
* ### Externo
  * É o recomendado.
  * Ele fica sempre no início do cóigo para que o navegador veja e faça a requisição do estilo logo ao entrar na tela.
* ### Inline
  * Não muito recomendada.
  * Usar o `style` na tag.
  * Não se beneficia do cache do navegador.
  * Não conseguimos sobrescrever o valor.