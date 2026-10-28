# Aula 22

## Modelos de Fundação
* O modelo que já vem pronto.
* A biblioteca transformer para baixar modelos do Hugging Face.
* Fine tunning é muito mais leve que o pre treino.
* `system`, `user` e `assistant` são tokens especiais.
* As três peças de um prompt: Papel, Contexto, Tarefa e formato.
* Few shot prompting.
  * Mandar perguntas curtas com respostas, para dar de exemplo.
* Menor temperatura para modelos de RAG, para retornar o mais fiel possível.
* A alucinação diminuiu muito decorrente da possibilidade de buscar na internet.
* Ele não sabe dizer "não sei".
  * Modelos pequenos não são bons de lidar com fatos.
    * Colocar mecanismos de RAG para funcionar melhor nesse cenário.
* Matemática também é uma área que modelos pequenos não vão ser bons.
* Modelos abertos e por API.
  * OpenRouter.

## RAG
* A aplicação mais básica com IA.
* Problema: o modelo não conhece o seu documento.
* Usar como MCP.
  * Uma WIKI com informações.
* A pergunta do usuário busca os trechos parecidos, cola os trechos no prompt e a partir disso o modelo responde.
  * Os trechos parecidos são os documentos.
  * Base vetorial dos documentos.
    * Pode ser em grafo, busca semântica, por palavras, etc.
* Não precisa treinar, pois a IA vai conversar com o documento.