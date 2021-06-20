# import socket
#
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind((socket.gethostname(), 1234))
# server.listen(5)
#
# print('---------- SERVIDOR ----------')
#
# while True:
#     client_socket, address = server.accept()
#     print(f'Conexão com {address} foi estabelecida com sucesso!')
#     client_socket.send(bytes('Bem-vindo ao servidor!', 'utf-8'))
#     client_socket.close()

import socket

HOST = socket.gethostname()
PORT = 2048

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

    with conn:
        print(f"Dados do cliente: {addr}")
        while True:
            dado = conn.recv(1024)
            if not dado:
                break
            conn.sendall(dado)
