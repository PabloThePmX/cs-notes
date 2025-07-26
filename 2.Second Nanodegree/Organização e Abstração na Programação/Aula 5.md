# Aula 5

### Modelo ER (Entidade-Relacionamento)
  * É essencial no design do banco de dados.
  * Para bancos relacionais.
  * É uma representação gráfica que descreve dados, em entidades, atributos e relacionamentos.
  * O "pé de galinha" é usada na entidade que tem muitos.
  * Modelo conceitual PODE só usar entidades.

  * ### Entidade
    * Representa um objeto, ou conceito do mundo real (livro, cliente, pedido, etc).
    * Físicas e lógicas.
      * Lógica: basicamente uma ação.
      * Física: Algo real.
    * Entidades fortes são aquelas que não dependem de outras, coisas que existem.
    * Entidades fracas precisam da existência de outra, como uma entidade de "Dependente".
    * Entidades associativas são as entidades que existem apenas se alguma associação for necessária, como uma tabela de "Compra".
      * É uma entidade de ligação.
        * Entidade de ligação é sempre 1:1.
  * ### Atributos
    * As características da entidade (no exemplo da entidade livro: título, autor, etc).
    * São as colunas da tabela.
    * Três tipos de atributos: Característica (nome), nominativos (chave primária), referenciais (chave estrangeira).  
    * Classificação dos atributos: Simples e Composto.
    * Não usa atributos FK neste modelo.
  * ### Relacionamento
    * Como as entidades estão associadas entre si (o cliente faz um pedido).
    * Em um diagrama ER, todos os relacionamentos são feitos por losangos que conectam as entidades participantes.
    * Tipos de Relacionamentos:
      * 1..1 ou 1:1 (um para um)
      * 1..n ou 1 (Um para muitos)
      * n..n ou N (Muitos para muitos)
        * Teoricamente não existe, precisa de uma ligação no meio.
          * Como a ligação Aluno-Disciplina, que diz os alunos que existem em uma disciplina, utilizando uma tabela chamada Matrícula no meio como entidade de ligação, com 1:n em cada ligação.