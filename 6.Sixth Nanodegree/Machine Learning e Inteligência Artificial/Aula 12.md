# Aula 12

## Regressão Linear Simples
* Se tiver um padrão linear, é preditivo.
  * Com proporcionalidade.
  * MMQ.
* Equação da regressão (Exemplo da Uber.): `preço = w0 + w1 * distância`
  * O `w0` e `w1` são peso/parâmetro.
    * Peso e parâmetro são iguais.
  * O w0 é a taxa fixa: o preço previso para uma corrida de 0km.
    * Linha de base ou vies.
  * O w1 é o preço por km: quanto o preço sobre a cada quilômetro.
    * Inclinação da reta.
      * Se for positivo, a reta vai ser inclinada para cima, e negativo o contrário.
* Tem o preço por dados passados.
* Probabilístico é algo que tem um certo grau de erro.
* Os parâmetros w1, w2, etc são os aprendidos por Machine Learning.
* O erro (resíduo) é a diferença entre o valor verdadeiro e o valor previsto.
  * Sempre que tiver `^` é previsto/estimado.
  * A distância do modelo para a realidade.
    * Queremos que isso seja o menor possível.
  * A reta é uma idealização do suposto padrão.
  * Pra encontrar a melhor reta, precisamos dos erros.
* Grau geral de erro.
  * O modelo é estimado para a média.
    * Por isso podem ter outliers.
* O erro quadrático médio (MSE).
  * A fórmula.
  * Eleva ao quadrado para eliminar os negativos.
    * Da mais peso para erros.
  * Quanto menor, melhor.
* Prever para testar o modelo.
* Gradiente descendente (usado pelas redes neurais).
  * Vai seguindo a inclinação.
  * Treinando e descartando.
    * Da pra distribuir em vários núcleos e depois junta tudo.
* Encontra os parâmetros a partir dos dados.
* O MMQ é pesado pois precisa inverter uma matriz.
  * Não da pra treinar um modelo grande com esse método clássico.
* O MMQ chega direto no valor mínimo, enquanto o gradiente vai ir chutando o valor para ir melhorando e encontrando o mínimo.
  * Vai calcular a derivada (a taxa de mudança de um valor a outro) do erro em relação ao parâmetro.
  * A derivada é a inclinação em algum ponto, vendo pra qual lado tem que ir pra diminuir o erro.
* O passo da derivada é um hiper parâmetro que permite fazer fine tuning.
* Nabla = simbolo do gradiente.
* O gradiente é um vetor de derivadas parciais.
* Equação de atualização de peso.
  * Taxa de aprendizado: o tamanho do paso.
* A `sklearn` é a biblioteca padrão de LLM para o python.
  * Mas o `TensorFlow` é para Redes Neurais.
* `Neuro Network Playground`.
* Uma regressão é uma rede neural sem camadas.
  * Uma rede neural é um amontoado de regressões, que vai recebendo valores que são filtrados por outras camadas.
* Validar o modelo é o mais difícil.
  * O benchmark em si.
* MAE: O erro médio, em reais.
  * Quanto menor, menor o grau de erro.
  * Para benchmark.
  * Métrica mais leiga para explicar para quem não conhece muito.
* RMSE: reais, punindo os erros grandes.
  * Pois eleva ao quadrado o MSE.
* As duas equações vão somente divergir se existir erros extremos.
  * Sem outliers.
* MAPE: mesmo erro, em percentual.
  * Quantos % de erro em cada predição/valor verdadeiro.
* R^2: Quanto maior melhor.
  * De 0 a 1.
  * A `sklearn` usa esse por padrão.
  * Poder explicativo.
* `y^ +- 2s`, sendo o `s` o erro/resíduo típico.
  * Para cada predição, são pegos os valores acima e abaixo, para ver a faixa de incertezas.