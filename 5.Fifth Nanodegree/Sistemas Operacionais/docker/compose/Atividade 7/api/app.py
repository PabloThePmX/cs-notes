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