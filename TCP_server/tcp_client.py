import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)
client_socket.connect(server_address)

# Отправляем сообщение серверу
message = "Привет, сервер!"
client_socket.send(message.encode())

# Получаем ответ от сервера
response = client_socket.recv(1024).decode()
print(f"Ответ от сервера: {response}")

# Закрываем соединение
client_socket.close()