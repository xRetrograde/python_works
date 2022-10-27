# Создать серверную часть, которая будет принимать сообщения от клиента и отправлять их обратно.

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 8888))

s.listen(5)
while True:
    client, addr = s.accept()
    print('Подключен клиент:', addr)
    while True:
        data = client.recv(1024)
        if not data:
            break
        print('Получено сообщение:', data.decode('utf-8'))
        client.send(f"Сообщение обработано!".encode('utf-8'))
    client.close()