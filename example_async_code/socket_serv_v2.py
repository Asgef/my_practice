import socket


# Создаем объект сокета
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Устанавливаем опцию сокета для повторного использования адреса
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Привязываем сокет к локальному хосту и порту 11000
server_socket.bind(('localhost', 11000))

# Переводим сокет в режим прослушивания
server_socket.listen()

# Бесконечный цикл для обработки входящих соединений
while True:
    print('Before accept()')
    # Принимаем входящее соединение
    client_socket, addr = server_socket.accept()
    print('Connection from', addr)

    # Цикл для обработки запросов от клиента
    while True:
        # Получаем запрос от клиента
        request = client_socket.recv(4096)

        # Если запрос пустой, выходим из цикла
        if not request:
            break
        else:
            # Отправляем ответ клиенту
            response = 'Hello World\n'.encode()
            client_socket.send(response)
    print('Outside inner while')
    # Закрываем соединение с клиентом
    client_socket.close()
