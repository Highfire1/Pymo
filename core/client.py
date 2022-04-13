# Code from stackoverflow (god bless)
import socket

async def sendToServer(data):

    HOST = 'localhost'    # The remote host
    PORT = 8080           # The same port as used by the server

    data = data.encode('utf-8')

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(data)
        data = s.recv(1024)


    print('Received', repr(data))
