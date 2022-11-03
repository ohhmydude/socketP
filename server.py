from concurrent.futures import thread
from http import server
import socket
from sqlite3 import connect
import threading

'''import time
time.sleep(1)
print("hell")'''


HEADER = 64

PORT = 5050
#SERVER = "172.20.129.104"

SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!Disconnect"



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)



def handle_client(conn, addr):
    print(f"[New Connection] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")

            conn.send("Message recieved".encode(FORMAT))
    conn.close()


    

def start():
    server.listen()
    print(f"[LISTENING] SERVER is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print("[Active Connection] {threading.activeCount()-1}")

print("Server initiating")

start()