import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error as e:
    print("Connection failed\n"
          f"Erro: {e}")
    sys.exit()
else:
    print("Connection made successfully")

host = "localhost"
port = 5433
message = "Olá, mundo!"

try:
    print(f"Client: {message}")
    s.sendto(message.encode(), (host, 5432))
    datas, server = s.recvfrom(4096)
except socket.error as e:
    print("Connection failed\n"
          f"Erro: {e}")
    sys.exit()
else:
    datas = datas.decode()
    print(f"Server: {datas}")
finally:
    print("Connection terminated!")
    s.close()
