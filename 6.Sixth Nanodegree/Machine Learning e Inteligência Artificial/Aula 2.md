# Aula 2

* Engenharia de IA combina software e aprendizado de máquina.
* No ML tradicional passa dados, para o modelo e ai par o produto.
  * Na Eng. de IA, começa com o produto, passa para a parte dos dados e então o modelo é criado.
* A arquitetura não é o diferencial, e sim os dados.
* O modelo calcula a probabilidade do próximo token baseado exclusivamente no contexto anterior.
  * Vai usar o vocabulário de tokens para isso.
  * De maneira recursiva ele prevê o proximo token a partir das probabilidades calculadas.
  * Modelos com fine-tunning nem sempre vão mostrar, as vezes vão apenas dizer para ser mais claro.
    * Mas os modelos base sim.
  * O que aparece primeiro, determina o que vai vindo depois.
* Aprendizado auto supervisionado.
  * `BOS`: Begin of Sentence.
  * `EOS`: End of Sentence.
    * Usados para dizer o início e o fim da frase.
* Modelos de fundação.
  * São sistemas multi modais, e eles recebem dados de várias formas (texto, imagem, vídeo) e podem gerar da mesma forma.
* RAG (Geração Aumentada por Recuperação).
  * Conecta o modelo a base de dados externas.
    * Internet, arquivos, etc.