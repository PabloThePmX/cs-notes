# Aula 24

* Da pra fazer um `post` com `/delete` e um body, para fazer a exclusão de mais itens de uma vez só, visto que o body vai receber uma coleção de IDs.
* Uma chamada dentro do app, para algo de fora, sempre usar o `async`/`await`.

## Cloudinary
* API que permite fazer o upload de imagens para a web.
* Da pra usar SDKs.
  * Mas nesse caso vai ser usada a chamada do endpoint do JS.
* Criar um `product environment`.
  * Produção e Desenv.
  * Na versão free so da pra ter um.
    * Portanto, da pra separar dentro da pasta do bucket.
* Criar `Upload Presets`, que é como um bucket.
  * Dentro do bucket, criar uma pasta para cada projeto.
* Deixar a imagem como não assinada, para que não necessite da API key.
  * Pelo fato de ser um e-commerce, que dai as imagens não tem problema de serem públicas.
* No upload, colocar o `cloudName` com o nome do environment e o `cloudPreset` com o preset.
  * E isso tudo vai ser juntado em uma `const` de data, que vai ser enviado no body da requisição.
* No postman da pra anexar um arquivo também (por trás ele transforma essa imagem em base64).

## Expo Image Picker
* É uma biblioteca do expo para seleção de imagens da galeria.
* Da pra acessar a câmera também.
* As permissões são colocadas no `app.json`, colocar lá para pedir para o usuário.
* Usar `*` para importar tudo do image picker, e colocar um `as` para alimentar isso em um alias.
* Ele tem um método para abrir a galeria.
* Da pra definir a qualidade do upload, para comprimir da galeria.
* Ao usar `base64: true` na requisição, na resposta vai vir o valor do base64 da imagem.
  * Usar um hook de `setImage` para salvar a imagem com o base64.
* Da pra usar o uri da imagem setada, como o source da tag `Image`.
