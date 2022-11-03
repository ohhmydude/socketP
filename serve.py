from email import message
import socket

from sympy import print_jscode

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5050

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5)

while True:
    communication_socket, address = server.accept()
    print(f"Connected to{address}")
    message = communication_socket.recv(1024).decode('utf-8')
    print(f"Message from IIST Kerala is: {message}")
    communication_socket.send(f"GOtcha!".encode('utf-8'))
    communication_socket.close()
    print(f"Coonection with {address} ended, Alas! :(")