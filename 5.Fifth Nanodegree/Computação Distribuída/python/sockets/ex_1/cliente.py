import socket  # Sockets

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Socket TCP
client.connect(('127.0.0.1', 65432))  # Conecta servidor

resposta = client.recv(1024).decode()  # Recebe resposta
print(f"Resposta servidor: {resposta}")  # Mostra echo

client.close()  # Fecha socket