import socket

# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect((socket.gethostname(), 1234))
#
# msg = client.recv(1024)
# print(msg.decode('utf-8'))

HOST = socket.gethostname()
PORT = 2048  # potência de 2 (no caso, 2048 == 2**11)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(bytes("Olá, mundo!", "utf-8"))
    dado = s.recv(1024)

print(f"Resposta do servidor: {repr(dado)}")
