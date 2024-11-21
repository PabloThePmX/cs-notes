-- 1. criação das tabelas
CREATE TABLE clientes(
    id_cliente SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    data_cadastro DATE DEFAULT CURRENT_DATE
);

CREATE TABLE livros(
    id_livro SERIAL PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    preco NUMERIC(10,2) CHECK (preco > 0)
);

-- 2. inserção dos dados
INSERT INTO clientes(nome, email)
VALUES ('Thiagão','thiagao_rei_czo@gmail.com'),
('Jobescliude', 'email_lendario@hotmail.com.br'),
('Mário Balen', 'mbalen@gmail.com');

INSERT into livros(titulo, autor, preco)
VALUES ('Programação Muito Avançada', 'Sr Lizard', 100000.99),
('Programação Nem Tão Avançada', 'Jr Lizard', 39.99),
('Livro Legal', 'Cara Legal', 49.99);

-- 3. alteração de tabela
ALTER TABLE clientes ADD COLUMN telefone VARCHAR(15);

-- coloca valores na nova coluna
UPDATE clientes
SET telefone = '5440028922'
WHERE nome = 'Thiagão';

UPDATE clientes
SET telefone = '5541028923'
WHERE nome = 'Jobescliude';

UPDATE clientes
SET telefone = '2142028924'
WHERE nome = 'Mário Balen';

-- 4. seleção de dados
SELECT * FROM clientes;

SELECT * FROM livros
WHERE preco > 50;

SELECT nome, telefone FROM clientes
ORDER BY nome;