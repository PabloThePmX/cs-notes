import threading
import time

# Cada conta é um dicionário com saldo e lock próprio
conta_alice = {
    "nome":  "Alice",
    "saldo": 1000,
    "lock":  threading.Lock()
}

conta_bob = {
    "nome":  "Bob",
    "saldo": 1000,
    "lock":  threading.Lock()
}

def transferir(origem, destino, valor):
    if id(origem["nome"]) > id(destino["nome"]):
        primeiro, segundo = destino, origem
    else:
        primeiro, segundo = origem, destino

    with primeiro["lock"]:
        with segundo["lock"]:
            origem["saldo"] -= valor
            destino["saldo"] += valor
            print(f"Transferido R${valor} de {origem['nome']} para {destino['nome']}")

t1 = threading.Thread(target=transferir, args=(conta_alice, conta_bob,   100))
t2 = threading.Thread(target=transferir, args=(conta_bob,   conta_alice, 200))

t1.start()
t2.start()

t1.join()
t2.join()

print(f"Saldo Alice: R${conta_alice['saldo']}")
print(f"Saldo Bob:   R${conta_bob['saldo']}")