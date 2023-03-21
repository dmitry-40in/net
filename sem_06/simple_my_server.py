import socket
import threading

HOST = "127.0.0.1"  
PORT = 65000  

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()


print("Server starts")
conn, addr = server_socket.accept()
print(f"Connected by {addr}")
while True:
    data = conn.recv(1024)
    if (data == "0"):
        server_socket.close()
    conn.send(data)
