# Создать клиентскую часть приложения, которая будет отправлять на сервер
# сообщения из командной строки при помощи UDP протокола.

import socket

host = 'localhost'
port = 9090

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = input('Введите сообщение: ')
    sock.sendto(data.encode(), (host, port))

    if data == 'exit':
        break

sock.close()