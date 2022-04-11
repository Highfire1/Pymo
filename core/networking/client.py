# Echo client program
import socket

HOST = 'localhost'    # The remote host
PORT = 8080              # The same port as used by the server


while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b'Hello, world')
        data = s.recv(1024)


    print('Received', repr(data))
