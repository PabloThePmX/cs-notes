# Aula 19

## Criptografia de Transposição

* Envolve a substituição de um símbolo de texto cifrado para um de texto claro.
* Permutação com letras.
* A mais simples é a cerca de trilho.
  * Coloca interrogação caso faltar.
* Transposição de matriz.
* Coloca a chave e ordena por quais letras aparecem primeiro no alfabeto.
* Pega a quantidade de linhas (depois de colocar a aqueles valores) e dai usa esse valor para preencher cada coluna com as letras, na ordem que foi colocada pelo alfabeto.
* Se repetir as letras, usar a ordem de qual aparece primeiro.

## Esteganografia

* Escondem a existência da mensagem, como colocar uma mensagem oculta dentro de outra.
  * Por exemplo, usando apenas a primeira letra de cada palavra.
* Marcação de caractere, tinta invisível, perfurações, fita corretiva, etc.
* Esconder uma imagem dentro de outra.
  * Ou no base64 dela.