# Aula 18

* Um LLM é um algoritmo multiclasse.
* Quantas mais épocas, maior a chance de overfitting.
* Uma imagem é uma grade de pixel, e a cor varia de 0 a 255.
* Em colorido precisa verificar 3 grades de pixel, portanto, se possível, é melhor preto e branco.
  * Pois colorido é RGB, e vai ter uma grade pra cada.
  
## Redes Convolucionais
* Pegar a informação da vizinhança.
* Uma camada convolucional.
* A janela que "passeia".
  * Filtro de imagem, vai indo de lado a lado pelo pixel.
* Aprenda o peso de 3x3.
* A rede aprende o filtro, e como ele vai deslizar.
* Vai ter vários filtros pela imagem.
* Cada filtro vai aprender a capturar características da imagem.
* Vizinhança, peso compartilhado.
  * Peso compartilhado pois um peso percorre toda imagem (um filtro).
* Pooling = compactação forçada.
* Vira uma grid de acordo com a imagem.
  * Uma matriz com os valores de acordo com a cor.
* Diferente de uma rede densa.
* No final precisa achatar para mandar para uma camada densa.
  * Ou seja, no final tem uma camada densa no final.