# Создать серверную часть, которая будет принимать сообщения от клиента и отправлять их обратно при помощи UDP протокола.

import socket

host = 'localhost'
port = 9090

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))

while True:
    data, addr = sock.recvfrom(1024)
    if data == 'exit'.encode():
        break
    print(data.decode())
    sock.sendto(data, addr)

sock.close()