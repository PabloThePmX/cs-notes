# Prova IA e Análise de Dados

## Questões

### Questão 1
Quais são as principais características de uma **rede neural de convolução**, utilizada para classificar imagens?
> As redes neurais de convolução (CNN) são amplamente utilizadas para classificar imagens.

### Questão 2
Com base no seu conhecimento de **Redes Neurais Artificiais** e suas respectivas estruturas, é correto afirmar que:
> O aprendizado por reforço (Reinforcment Learning) é um tipo de aprendizado de máquina em que um agente aprende a tomar decisões sequencias para maximizar uma recompensa cumulativa.

### Questão 3
Como é o padrão de armazenamento e aprendizado de redes neurais que trabalham com imagens digitais **coloridas**?
> Os tensores armazenam os valores numéricos dos pixels das imagens digitais coloridas, geralmente usando a representação RGB.

### Questão 4
Quais são os **passos** utilizados para que uma rede neural consiga aprender padrões a partir dos dados de entrada?
> Durante o forward pass, os pesos da rede são calculados com base no conjunto de treinamento, e as saídas são geradas na camada de saída.

### Questão 5
Sobre o **neurônio artificial**, assinale a alternativa que o caracteriza corretamente:
> Um neurônio artificial é uma unidade computacional fundamental em redes neurais artificiais, inspirada no funcionamento de neurônios biológicos.

### Questão 6
A partir do seu conhecimento de **Redes Neurais Profundas** (Deep Learning), o que é possível afirmar sobre o processo de aprendizado deste tipo de rede neural?
> Durante o aprendizado, as informações fluem da camada de entrada, passando pelas camadas ocultas, até chegar na camada de saída.

### Questão 7
Quais são as principais vantagens de uso do **Transfer Learning** para o treinamento de uma nova rede para classificação de imagens?
> Com o transfer learning, é possível aproveitar modelos de redes CNN já treinados em grandes conjuntos de dados, evitando a necessidade de treinar a rede do zero, o que reduz significativamente o custo computacional.

### Questão 8 (mesma da 3)
Como é o padrão de armazenamento e aprendizado de redes neurais que trabalham com imagens **coloridas**?
> Os tensores armazenam os valores numéricos dos pixels das imagens digitais coloridas, geralmente usando a representação RGB.

-------

## Conteúdos a partir das questões:
* Redes Neurais de Convolução
  * Extrair características relevantes de uma imagem.
* Redes Neurais Artificiais
  * Tentam imitar as redes neurais de uma pessoa, tendo inputs de entrada, as camadas escondidas (intermediárias) e a camada de perda (output).
    * Cada camada intermediária, é capaz de extrair padrões dos dados de entrada.
      * A extração ocorre em sequência, as representações mais abstratas nas camadas iniciais, para representações mais detalhadas nas camadas finais.
* Tensores
  * Um tensor é um array multidimensional usado para armazenar informações (sempre numéricas) do dataset, costumam ser tridimensionais como um cubo com eixos X, Y e Z.
  * Como se fosse várias matrizes que formam um dado complexo.
* Neurônio Artificial
  * Ele deve ser capaz de sintetizar o processo de sinapse que ocorre no cérebro humano, por meio da transferência de informações com a finalidade de obter conhecimento sobre determinada tarefa.
  * O conceito disso é criado a partir de uma representação matemática, muito similar a idade de modelos lineares, mas em tamanho e forma muito maiores.
* Deep Learning
  * Quanto mais camadas ocultas, maior é a parte intermediárias (Deep learning tem bastante dessas camadas ocultas).
* Transfer Learning
  * Utiliza o conhecimento já adquirido em outra task, para melhorar a performance do modelo.

-------

## Conteúdo
* Tipos de Rede Neural
  * Aprendizado por reforço (Reinforcement Learning)
  * Aprendizado Recorrente (Recorrente Neural Network - RNN)
  * Aprendizado em Camadas (Multi Layer Perception - MLP)

* Toda rede neural trabalha somente com **números** (ponto flutuante).
* As informações representadas em formato numérico são armazenados em tensores.
* Usa a multiplicação de matrizes para realizar o aprendizado.

* Tensor
  * A representação de uma imagem em um tensor segue o padrão `[#camadas,width,height]`
  * Uma imagem colorida possui camadas RGB

* Processo de Aprendizagem
  * Acontecem em 3 etapas:
    * Ida (forward): os pesos são calculados a partir do conjunto de treinamento em memória
    * Verificação de erro (loss): os valores calculados nas camadas geram uma representação na camada de saída, que é comparado com o valor esperado, e é calculado a distância (error) entre os valores.
    * Volta (backward): o erro calculado é distribuído entre os neurônios que participam do processo, e os valores dos pesos (weights) são atualizados.
  * Componentes:
    * Função de perda (loss).
    * Pesos (weights) armazenadas nos neurônios que representam o aprendizado.
    * Algoritmo de Otimização, responsável pela operação entre etapas de aprendizado (minimização).
    * Taxa de Aprendizado (learning rate), é o "tamanho do peso" que é dado em cada sequência de aprendizado, em direção ao menor valor (minimização).

* Redes de Convolução
  * São redes neurais utilizadas para trabalhar com imagens, e são conhecidas como CNN.
    * O funcionamento está relacionado ao operador de convolução, utilizado para extrair informações da imagem.
      * Além dessa operação de convolução, normalmente utilizamos também.
        * Simplificação (pooling).
        * Função de ativação (activation), responsável pela decisão de passar a informação a diante.
  * As características de imagens são extraídas de forma sequencial pelas camadas CNN, de forma a compor uma representação da informação contida na imagem.
  * As camadas podem ser classificadas como:
    * Extrair características (feature extractor layers).
    * Redução de informações/dimensionalidade (fully connected layers).
    * Classificação (head layer).

* Transfer Learning
  * Para acelerar o processo, esse método utiliza conhecimento já adquirido de outras experiências para acelerar o processo.
  * Para melhorar o resultado de classificação de imagens:
    * Aumentar o tempo de aprendizado (Epochs).
    * Utilizar aumento de dados (data argumentation).
    * Ajustar taxa de aprendizado (learning rate).
    * Trocar a rede CNN para extrair padrões (feature extraction).
    * Alterar a função de otimização (SGD, Adam, etc).

-------

## Informações pegas durante a apresentação
* Learning Rate
  * Learning rate baixa = treino longo que pode travar.
  * Learning rate alta = Aprende um conjunto muito rápido, abaixo do ideal e pode ter um treino instável.
  * Por definição:
    * The learning rate controls how quickly the model is adapted to the problem. Smaller learning rates require more training epochs given the smaller changes made to the weights each update, whereas larger learning rates result in rapid changes and require fewer training epochs.
    * A learning rate that is too large can cause the model to converge too quickly to a suboptimal solution, whereas a learning rate that is too small can cause the process to get stuck.
  * Quando está demorando demais para concluir o treinamento, aumentar o learning rate retirando uma casa decimal.

* Epochs
  * Define quantas vezes o algoritmo vai treinar naquele dataset.