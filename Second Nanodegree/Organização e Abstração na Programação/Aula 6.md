# Aula 6

### Chave Primária
* Chave Natural: Um atributo que já existe nos dados e que pode ser usado como chave primária, como o CPF.
* Chave primaria composta é quando temos mais colunas como PK.
* Chave substituta (surrogate key) é uma chave que não tem impacto nos dados em si, e é usada apenas para ser chave primária (como um ID).

### Chave Estrangeira
* Vai sempre usar o código da outra tabela, evitando assim ter campos com valores muito grandes.
  * Pois ao invés de armazenar um nome completo por exeplo, vai salvar apenas a chave primária.

### Chave Alternativa
* Chave Alternativa (alternate key ou candidate key): É como fosse uma chave "alternativa" para a primaria.
  * Ex.: CPF e código da pessoa, podemos usar a PK como o código, e o CPF como alternativa para caso seja mais fácil de buscar pelo CPF
    * Pois ambas as chaves são únicas.
  * Não é uma constraint, e sim um "conceito".

### Modelo ER Lógico
* É uma representação mais detalhada do modelo de dados.
* Diferente do conceitual, o modelo lógico já começa a incorporar regras de negócios, tipos de dados, restrições e outros detalhes necessários para a criação do esquema físico.
* Diferenças:
  * Não é tão abstrato quanto o conceitual
  * É mais detalhado.
  * É preciso já pensar em possíveis peculiaridades de cada SGBD, visto que tipos podem variar de acordo com o SGBD usado.