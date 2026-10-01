# Aula 11

## Método dos mínimos quadrados.
* Criar uma reta em um amontado de pontos.
  * A linha vai criar uma "média" desses valores em um plano cartesiano, formando um gráfico.
* Transformar em matriz.
  * Ajustar a reta aos pontos (1,2) e (2,3).
    * Matriz de x e y.
      * Como coluna.
    * Com uma incognita.
    * Como tem uma incognita, ao passar pro outro.
    * Encontra os valores de cada uma, pra substituir e pegar a incognita.
  * Os dois lados precisam ser multiplicados sendo transposta.
  * Precisa deixar a primeira sempre transposta, e calcular baseado nisso.
    * `A^t x A, A^t x B`, sendo a matriz A o que vem do x.
      * E o resultado de cada, colocar na equação `y = mx`.
        * Lembrar que cada um desses é pego de cada ponto, os y e x.
* A pergunta vai começar com `ajustar a reta y= mx+b para os pontos...`
* Pode ter o `b` que seria o ponto de início no eixo y.
  * Se for 0 ele n aparece na equação.
  * Quanto tem o `b`, o valor vira uma coluna de matriz, e os outros valores precisam igualar, colocando `1`.
  * Pode gerar sistema, visto que tem duas incógnitas.
* A matriz do `m` seria o vetor (`v`).
* Quanto mais pontos, mais próximo da realidade fica a reta.
* Quando tem mais pontos, usar a fórmula, mas antes disso, fazer uma tabela com isso.
  * Fazer a soma dos resultados de cada coluna, para alimentar o sigma da fórmula.
  * O `n` é a quantidade de pontos.

## Derivada de uma Função
* Tava de variação instantânea.
* Equação de reta que vai tangenciar um ponto.
  * É uma reta que vai mostrar o comportamento de uma curva, se está crescendo, decrescendo ou constante.
* O valor: `f(x) = x^2 + 2x+ 4`.
  * Vira a derivada: `f'(x) = 2x + 2`.