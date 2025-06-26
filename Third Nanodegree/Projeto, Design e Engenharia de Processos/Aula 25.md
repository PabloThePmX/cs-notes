# Aula 25

* O `onEndReached={}` chama a função quando chegar no final, para que faça uma nova busca no final.
  * Como o scrolling infinito de redes sociais.
*  Para alterar as imagens do expo, alterar os que estão na pasta `assets`.
*  No `app.json` diz onde tem que buscar essas imagens.
   *  A `splash` tem algumas propriedades extras.

## Gerando Build
* O `AAB` é um bundle que faz o build de várias versões para o android, otimizando para a versão designada.
  * É mais para distribuição em lojas.
  * Depende da versão do APK do android.
* A loja também vai otimizar o tamanho do build.
* O `APK` é mais usado para coisas fora de lojas, ou que ainda estão em testes e são passados uns para os outros.
  * Focado para o desenvolvimento, pois tem o kit de desenvolvimento do android.
* No IOS é o `IPA`.
* Precisa de conta no expo.
* Baixar o `eas-cli` que é do expo também (usar o parâmetro `-g` para que esteja disponível para todos os projetos).
  * Depois fazer o login com `eas-login` e ai então executar o build com `eas build:configure`.
    * Da pra fazer o build para cada ambiente e sistema operacional, dependendo dos parâmetros.
* Vai criar um arquivo `eas.json`
  * Contendo os ambientes de produção e desenv.
* Para o build do Android, precisa criar credenciais.
* Da pra configurar o ambiente java ou fazer pelo próprio android studio.

## Disponibilizar nas Lojas
* Precisa ser aprovado, o google faz essas aprovações de forma robotizada e humana.
* Leva entre 3 a 7 dias para aprovar.
* O `progressier` é um site usado para criar imagens para os aplicativos nas lojas.
  * Usar o screenshot generator.
  * Na apple precisa gerar um screenshot para cada aparelho (versões diferentes do IPhone e IPad).
* Da pra botar na play store e limitar para que apenas aqueles que tem um email específico possam ver e baixar.