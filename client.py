
import socket

HOST = 'localhost'
PORT = 6060

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    print(client.recv(1024).decode())
    msg = input(' Your msg : ').encode()
    client.send(msg)