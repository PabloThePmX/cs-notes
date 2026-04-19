import socket  # Sockets

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Socket TCP
client.connect(('127.0.0.1', 65432))  # Conecta servidor

mensagem = input("Digite mensagem: ")  # Entrada usuário
client.send(mensagem.encode())  # Envia mensagem

resposta = client.recv(1024).decode()  # Recebe resposta
print(f"Resposta servidor: {resposta}")  # Mostra echo

client.close()  # Fecha socket