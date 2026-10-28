# Aula 20

* Pedir para o agente criar um `spec.md`, fazendo uma entrevista.
* Depois do spec pronto, pedir um `TODO` para usar em uma LLM com menos raciocínio (deixar isso explícito).

## LLM (Embeddings)
* Vetores existem em um espaço vetorial de 3 dimensões.
  * Da pra fazer cálculos de similaridade, para ver a similaridade das palavras.
* Os embeddings transformam o token em um vetor.
  * Cada token trocado pela sua linha: o embedding.
* Se o sentido for parecido, o vetor (embedding) parecido.
  * Ou seja, palavras em comum ficam "juntos".
* Começam espalhados, totalmente aleatórios, e o modelo aprende como vai relacionar cada um deles.
  * Os modelos parecidos, se tornam um vetor único, ou seja, um vetor com palavras parecidas.
    * E estes são os embeddings.
* `Transformer Explainer`: uma aplicação web para visualizar como o GPT-2 funciona.
* Existe cálculo de similaridade.
  * Usa `Norma L2`.
* Alta supervisão e paralelismo.
  * Preditores (entradas) e alvos (saídas) podem ser derivados do próprio texto.
* A geração de texto é sequencial, pois precisa da saída para agregar na entrada e ver o próximo token.
* Cada pedaço é uma janela de contexto.
* O tamanho do vetor vai ser do tamanho da janela de contexto.
* A janela de contexto virá uma matriz de embeddings.
* Função de perda para saber a probabilidade do vocabulário, de qual vai ser o próximo token.
  * Qual foi a probabilidade de aparecer o token certo?
  * Vai prevendo a partir dos tokens da janela de contexto.
* Sebastian Raschka.
  * Conteúdo de IA.
* A conta de atenção.
  * Ve as relações de tokens.
  * Relação entre os tokens, e como o embeddings vira um Q, K e V para usar na fórmula.
* Máscara causal.
  * Ve o token atual e o anterior, e define o peso para o próximo token (decoder).
  * Blinda o modelo do futuro.
* Bloco transformer.
  * Recebe o embedding, normaliza e passa para cabeças de atenção.
    * Conexões residuais.
    * Cada cabeça relaciona as palavras de uma forma diferente.
* Embedding posicional.
  * Sem ele, frases com as mesmas palavras mas ordem diferentes, ficam iguais.