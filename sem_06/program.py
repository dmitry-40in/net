import socket, threading
from time import sleep

# Открываем сокет
sock = socket.socket()

# Коннектимся
addr = ("158.160.19.47", 55555) # ip-адрес яндекса и https-порт
sock.connect(addr)

# Подготовим HTTP-запрос
# вначале b - переводим в двоичный вид
def sock_send(data):
sock.send(data)

def sock_recieve():
# Передаём размер буфера - по сколько байт будем перехватывать с нашей сетевой карты приходящих на неё данных и заносить в переменную
while True:
data_in = sock.recv(1024)
print(data_in.decode('ascii'))

sock_send(b"maxim")

rec_thread = threading.Thread(target=sock_recieve)
rec_thread.start()

while True:
data = input()
sock_send(f"maxim: {data}".encode('ascii'))
Alina: Я 3 прислала))