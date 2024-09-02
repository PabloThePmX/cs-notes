# Aula 3
Linguagem R

* R é uma linguagem de programaão desenvolvida para análise de dados.
* Se aproxima bastante da do C.
* Open Source.
* Pode trabalhar em conjunto com o Python.
* Utilizar a IDE do RStudio.
* Toda função no R termina com ().

# Distribuição de Probabilidade
## Variáveis Discretas (Contagens)
* *Bernoulli*
  > Modelar eventos do tipo sucesso/fracasso, onde a probabilidade é representada por p

  > Ex.: Lançamento de moeda.
  ```R
  # Na linguagem R:
  rbinom(n, 1, prob)
  ```
* *Binomial*
  > Modelar número de sucesso em uma sequência de n tentativas independentes, onde a probabilidade de sucesso é representada por p

  > Ex.: Lançamento de várias moedas.

  > Obs.: Ser totalmente indepentende, quer dizer que cada evento não interfere em nada no outro.
  ```R
  # Na linguagem R
  dbinom(x, size, prob, log = FALSE)
  pbinom(x, size, prob, lower.tail = TRUE, log.p = FALSE)
  qbinom(x, size, prob, lower.tail = TRUE, log.p = FALSE)
  rbinom(n, size, prob)
  ``` 
* (Aula 4)
  * Poisson
  * Geométrica