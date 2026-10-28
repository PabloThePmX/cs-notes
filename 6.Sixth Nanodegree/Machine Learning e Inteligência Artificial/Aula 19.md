# Aula 19

* Um modelo de linguagem recebe um pedaço de texto e devolve as chances de cada continuação possível.
  * Da probabilidade de cada palavra do vocabulário.
* Um LLM no geral é um complementador de texto.
* The scaling loss.
* Das regras básicas surge uma complexidade.
  * Um processo simples muito escalado.
* LLM pre treinado e de fine tunning são diferentes.
  * Modelo de base + fine tunning = modelo de fundação (LLM pré treinado).
* Dá a probabilidade de todas as palavras possíveis.
  * Depende da temperatura, ranqueamento, etc.
  * Vai dar peso para as próximas palavras e vai ver qual delas tem peso maior.
* Tem um alto grau de aleatoriedade.
* Baseline para bater: `P(seguinte|atual) = contagem(atual, seguinte)/contagem(atual)`.
  * Descobre a probabilidade que tal letra aparece depois de uma outra definida.
  * Usa apenas p caractere anterior.
    * Não da pra usar combinações grandes, pois ficaria gigante.
* O NLP clássico deixava tudo em minúsculo e sem acento.
  * Nos modernos, até palavras comuns ficam, sem alterações.
* Precisa normalizar os caracteres Unicode.
* Por token (tokenizador BPE).
  * Quebra em mais ou menos sílabas (não é exatamente isso).
    * Tokenizador (algoritmo simples).
  * Dessa forma diminui a previsão com menos pedaços.
  * É o meio termos, para ter menos vocabulário e menos pedaços.
    * Se for caractere individual tem muitos pedaços, e por palavra tem muito vocabulário.
* Byte Per Encode - Encontre o par de tokens vizinhas mais comum no texto, junte as duas numa token nova e repita.
  * Vai repetindo e fazendo a separação do processo até encontrar a melhor forma.
* Se da empate no tokenizador, vence a que apareceu primeiro.
* Palavras que são muito utilizadas, viram tokens do tokenizador.
* Todo texto é uma lista de bytes, números de 0 a 255.
  * Ou seja, troca as palavras pelo seus bytes.
    * Isso é a codificação.
* Se tem um `·`, significa que é um espaço.
* O BPE opera sobre os bytes, por isso existem apenas 256 valores.
  * Cada caractere ocupa os bytes.
* O tamanho do vocabulário: `vocabulario = 256 bytes + 768 fusões = 1024 (tokens)`.
  * O 768 é quantas vezes o pais mais comum foi fundido.
* A fusão é a junção que é feita.
  * Começa de caractere em caractere e vai juntando.
* Ele pode reutilizar as tokens iguais.
* Fusão so acontece dentro das palavras.
  * No tokenizador oficial é assim.
    * Pra não perder quando a token for igual e mudar apenas o espaço, vírgula, etc.
* Codificador e decodificador precisa usar a mesma tabela.
  * Mapeia aquele texto para as fusões.
* Depois dos ids (que é o número do token), isso viram um vetor para ser usado com embeddings.
  * O id é so o endereço da token em uma tabela.
* Números acima de 255 são fusões.