# Seção 1
Como usamos dois serviços, a melhor abordagem é com o docker compose, pois fica mais simples e fácil de orquestrar ambos containers.
```yaml
services:
  meu-adminer:
    image: adminer:latest
    ports:
      - "8080:8080"
    networks:
      - rede-db
  
  meu-postgres:
    image: postgres:15-alpine
    ports:
      - "5432:5432"
    environment:
      POSTGRES_PASSWORD: postgres
    networks:
      - rede-db

networks:
  rede-db:
```

# Seção 2
- O arquivo vai criar 3 containers.
- O serviço "web" usa um dockerfile.
- Ele está nas redes interna e pública para ser como um intermediário entre o banco e o nginx.
- Não. O db está apenas na rede interna. O nginx está apenas na pública, então ele não consegue acessar o banco diretamente.
- Precisa mudar o `depends_on` do container web e a URL da database.
- O acesso principal é pela porta 80 (nginx). O web usa a 5000 porque provavelmente é a porta interna da aplicação, enquanto o nginx atua como proxy reverso
- Não, pois está exposta no arquivo. O correto seria a mesma estar presente em um arquivo .env que não é "público".

# Seção 3
```yaml
version: '4.0'
services:
  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_PASSWORD: postgres
    networks:
      - interna

  api:
    build: ./api
    environment:
      DATABASE_URL: postgres://postgres:postgres@db:5432/postgres
    ports:
      - "8000:8000"
    depends_on:
      - db
    networks:
      - interna

  adminer:
    image: adminer:latest
    ports:
      - "8080:8080"
    networks:
      - interna

networks:
  interna:
```

# Seção 4
```yaml
version: '3.8'
services:

  banco:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: senha123
      POSTGRES_DB: teste
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data
    
  api:
    image: python:3.12-alpine
    command: sleep infinity
    volumes:
      - ./api:/app

volumes:
  pgdata:
```

# Seção 5
```yaml
version: '3.8'
services:
  banco:
    image: postgres:15-alpine
    env_file:
      - .env.dev
    environment:
      POSTGRES_DB: producao

  api:
    build: ./api
    env_file:
      - .env.dev
    environment:
      DATABASE_URL: postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@banco:5432/producao
      SECRET_KEY: ${SECRET_KEY}
      DEBUG: "${DEBUG}"
    ports:
      - "8000:8000"
    depends_on:
      - banco
```
O arquivo `.env` de dev.
```env
POSTGRES_USER=admin
POSTGRES_PASSWORD=minha_senha_123
SECRET_KEY=chave-jwt-abc123-super-secreta
DEBUG=TRUE
```
O `.gitignore` ignorando ambos os `.env`, deixando apenas o `.env.example`.
```
.env
.env.dev
.env.prod
```
# Seção 6
Tudo ok.

# Seção 7
```yaml
services:
  banco:
    image: postgres:15-alpine
    restart: always
    environment:
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: ${POSTGRES_DB}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - backend

  redis:
    image: redis:7-alpine
    restart: always
    networks:
      - backend

  api:
    build: ./api
    restart: always
    ports:
      - "8000:8000"
    environment:
      DATABASE_URL: ${DATABASE_URL}
      REDIS_URL: redis://redis:6379/0
    depends_on:
      - banco
      - redis
    networks:
      - backend

  adminer:
    image: adminer
    restart: always
    ports:
      - "8080:8080"
    depends_on:
      - banco
    networks:
      - backend

volumes:
  postgres_data:

networks:
  backend:
```

O arquivo `.env`.
```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=produtosdb

DATABASE_URL=postgresql://postgres:postgres@banco:5432/produtosdb
```

O `requirements` da api python.
```
flask
flask_sqlalchemy
psycopg2-binary
redis
gunicorn
```

O Dockerfile.
```Dockerfile
FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
```

E por fim, a api em si.
```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import redis
import json
import os

app = Flask(__name__)

database_url = os.getenv("DATABASE_URL")

app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

redis_client = redis.Redis.from_url(
    os.getenv("REDIS_URL"),
    decode_responses=True
)

CACHE_KEY = "produtos"
CACHE_TTL = 60


class Produto(db.Model):
    __tablename__ = "produtos"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    preco = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "preco": self.preco
        }


@app.before_request
def create_tables():
    db.create_all()


@app.route("/produtos", methods=["GET"])
def listar_produtos():
    cached = redis_client.get(CACHE_KEY)

    if cached:
        return jsonify(json.loads(cached))

    produtos = Produto.query.all()

    resultado = [p.to_dict() for p in produtos]

    redis_client.setex(
        CACHE_KEY,
        CACHE_TTL,
        json.dumps(resultado)
    )

    return jsonify(resultado)


@app.route("/produtos", methods=["POST"])
def criar_produto():
    data = request.json

    if not data:
        return jsonify({"erro": "JSON inválido"}), 400

    nome = data.get("nome")
    preco = data.get("preco")

    if nome is None or preco is None:
        return jsonify({"erro": "nome e preco são obrigatórios"}), 400

    produto = Produto(
        nome=nome,
        preco=preco
    )

    db.session.add(produto)
    db.session.commit()

    redis_client.delete(CACHE_KEY)

    return jsonify(produto.to_dict()), 201


@app.route("/produtos/<int:id>", methods=["DELETE"])
def deletar_produto(id):
    produto = Produto.query.get(id)

    if not produto:
        return jsonify({"erro": "produto não encontrado"}), 404

    db.session.delete(produto)
    db.session.commit()

    redis_client.delete(CACHE_KEY)

    return jsonify({"mensagem": "produto removido"})


@app.route("/")
def health():
    db.session.execute(text("SELECT 1"))

    return jsonify({
        "status": "ok"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
```