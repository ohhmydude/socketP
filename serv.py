import socket
import os
import sys
s = socket.socket()
host = socket.gethostbyname(socket.gethostname())

port = 12000
s.bind((host, port))
s.listen(10)
while True:
    c, addr = s.accept()
    print("Client Connected! Hurray", addr)
    print("Got connection from", addr)
    content = c.recv(100).decode()
    if not content:
        break
    
print(content)