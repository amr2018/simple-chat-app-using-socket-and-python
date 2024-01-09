
import socket

HOST = 'localhost'
PORT = 6060

sok = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sok.bind((HOST, PORT))
sok.listen()
print('Listening.....')

conn, addr = sok.accept()

print(f'Connected to {addr}')

while True:
    msg = input(' Your msg : ').encode()
    conn.send(msg)
    print(conn.recv(1024).decode())