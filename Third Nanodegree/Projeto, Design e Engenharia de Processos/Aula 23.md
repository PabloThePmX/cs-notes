# Aula 23

* Para descobrir a quantidade de páginas, vai ser feita a divisão entre a quantidade de itens totais e a quantidade de itens mostrado por página.
* A autenticação vai pelo header.
* Usar interceptor para pegar o envio e o retorno das requisições.
  * Seria como um middleware.
    * Se der erro, ele vai pegar o erro e se for login por exemplo, vai fazer um `.map()` modificando a requisição com o token novo, ou seja, vai enviar a mesma requisição porém com um token novo.
* Soft delete: Coloca uma coluna nova do tipo booleano para dizer se aquele registro foi ou não apagado, sem que apague ele, evitando dar problemas.
  * Em E-Commerce, geralmente se replica o item em uma tabela de itens da compra, dessa forma ele vai sempre ter um registro do item comprado, bem como vai salvar as informações que foram disponibilizadas no exato momento da compra.
  * No back, deve-se avaliar se é realmente plausível fazer um hard delete, pois geralmente tudo precisa ter algum registro, principalmente em e-commerce, que além dos pedidos, a loja, as pessoas e afins precisam existir pois pedidos anteriores dependem delas.