import socket
import sys

from time import sleep

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error as e:
    print("Connection failed\n"
          f"Erro: {e}")
    sys.exit()
else:
    print("Connection made successfully")

host = "localhost"
port = 5432

s.bind((host, port))

message = "OK"

while True:
    datas, address = s.recvfrom(4096)

    if datas:
        print("Wait..."); sleep(1.5)
        s.sendto(message.encode(), address)
