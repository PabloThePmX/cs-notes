# import socket

# import socket

# host = '127.0.0.1'
# port = 65432

# with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
#     socket.sendto("Oi", (host, port))
#     print(f'Server listening on {host}:{port}...')
    
#     while True:
#         conn, addr = s.accept()
#         with conn:
#             print(f'Connected by {addr}')
#             while True:
#                 data = conn.recv(1024)
#                 if not data:
#                     break
#                 print(f'Received from {addr}: {data.decode()}')
#                 conn.sendall(data)


import socket

host = "127.0.0.1"
port = 5005
MESSAGE = b"Hello, World!"

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (host, port))