import socket
import threading

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

my_socket.connect(("127.0.0.1", 65000))

def sock_recieve():
    while True:
        data_in = my_socket.recv(1024)
        print(data_in.decode('ascii'))

my_socket.send(b"hello, i'm client_two")

rec_thread = threading.Thread(target=sock_recieve)
rec_thread.start()

while True:
    data = input()
    if (data == "0"):
        my_socket.close()
    my_socket.send(f"Client_two: {data}".encode('ascii'))
