import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
except socket.error as e:
    print("Conexão falhou!\n"
          f"Erro: {e}")
    sys.exit()
else:
    print("Socket criado com sucesso")

host = input("Host ou IP: ")
port = input("Port: ")

try:
    s.connect(
        (host, int(port))
    )
except socket.error as e:
    print(f"Não foi possível efetuar a conexão no host {host}\n"
          f"Erro: {e}")
    sys.exit()
else:
    print(f"Cliente TPC conectado com sucesso. HOST {host} / PORT: {port}")
    s.shutdown(2)
