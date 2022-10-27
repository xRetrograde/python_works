# Создать клинтскую часть приложения, которая будет отправлять на сервер сообщения из командной строки

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 8888))

while True:
    msg = input('Введите сообщение: ')
    s.send(msg.encode('utf-8'))
    data = s.recv(1024)
    print(f'Ответ сервера: {data.decode("utf-8")}')
    choice = input('Продолжить? (y/n): ')
    if choice != 'y':
        break