# Aula 21

* Bloco transformer tem uma camada de atenção.
* A atenção junta informação de outras posições. 
  * A camada densa usa isso.
  * É responsável por entender o context.
* O modelo não reescreve o modelo do zero, ele vai recalculando o valor da entrada original.
  * Ou seja, o embedding é preservado mas mais informação é acrescentada à ele.
  * Agrega ao vetor, informações de contexto dos tokens passados.
* A normalização serve para a estabilidade numérica.
* Embedding do token + da posição -> Quatro blocos transformer -> Uma última normalização -> Uma camada densa com o tamanho do vocabulário de tokens do modelo.
  * `Logit`.
* O passo zero e a perplexidade.
  * Euler elevado na perda = perplexidade.
    * Diz entre quantos tokens o modelo está, em média, na dúvida.
* O otimizador `AdamW`.
  * É o que implementa o gradiente descendente.
* LLM treina por mais tempo, do que uma rede neural comum.
* Cálculo para saber quantas operações são usadas no treinamento.
* Quanto maior a temperatura, menos incisivo o modelo vai ser.
  * Está correlacionado com modelos mais criativos (temperatura alta).
* Top-p é melhor que o top-k.
  * Visto em agentes de pesos abertos.
* Um modelo que tendem a escolher sempre o mais provável, se repete muito.
  * Baixa temperatura, não olha outras opções.
* O modelo não reproduz o corpus, mas ele gera conteúdo a partir dessa informação de treinamento.
* O modelo não tem uma noção de verdadeiro e falso, um lugar para consultar um fato ou uma marca de onde veio cada coisa.
* Não existe um modelo neutro.
  * Ele reproduz o que está presente nos treinos, mesmo que seja "errado".
    * Mas os modelos mais famosos tem railbreakers (não censurado).
* Fine tuning = treinar mais.
  * Pegar um modelo aberto e treinar mais um modelo.
* Pré-treino, ajuste por instrução e por preferência.