# Aula 4

## Continuação da Aula 3
  * **Poisson**
      > Modelar o número de ocorrências de um evento em um intervalo, quando a média de ocorrências é conhecida.

      > Ex.: Número de carros que passam por uma determinada rua em uma hora de pico.

      ````R
      # Na linguagem R
      dpois(x, lambda, log = FALSE) # lambda = valor medio
      pgeom(q, prob, lower.tail = TRUE, log.p = FALSE)
      qgeom(p, prob, lower.tail = TRUE, log.p = FALSE)
      rpois(n, lambda)
      ````
  * **Geométrica**
      > Modelar o número de tentativas independentes necessárias até que ocorra o primeiro sucesso.

      > Número de lançamentos de uma moeda necessários até que saia cara pela primeira vez.

      ````R
      # Na linguagem R

      ````

## Variáveis Contínuas
  * **Uniforme**
    > Modelar uma situação em que todos os valores possíveis tem a mesma probabilidade de ocorrência.

    > Ex.: A escolha aleatória de um número entre 1 e 100.

    ````R
    # Na linguagem R

    ````

  * **Normal**
    > É caracterizada por uma curva em formato de sino, e é definida por sua média e desvio padrão.

    > Ex.: A altura das pessoas, o peso dos objetos, etc.
    
    ````R
    # Na linguagem R

    `````  

  * **Exponencial**
    > Modelar o tempo entre eventos raros ou a espera pelo próximo evento.

    > Ex.: O tempo de espera entre chegadas de clientes em uma loja.

    ````R
    # Na linguagem R
    ````

# Variabilidade
Pode ser classificado em dois grupos: **determinístico** (sem variabilidade) e **estocástico** (com variabilidade)
> Ex. Determinístico: Aceleração da gravidade.

> Ex. Estocástico: Nascimento de filhotes gêmeos de urso.

A variação ocorre em 2 níveis: **população** e **amostra**.