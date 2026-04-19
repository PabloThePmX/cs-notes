import socket

host = '127.0.0.1'
port = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    print(f'Server listening on {host}:{port}...')
    
    while True:
        conn, addr = s.accept()
        with conn:
            while True:
                data = "Hello Client"
                conn.sendall(data.encode())