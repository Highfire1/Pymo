# Code from stackoverflow (god bless)
import socket

async def sendToServer(data):

    HOST = 'localhost'    # The remote host
    PORT = 8080           # The same port as used by the server

    data = data.encode('utf-8')

    socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    with socket_ as s:
        s.settimeout(3)
        s.connect((HOST, PORT))
        s.sendall(data)
        data = s.recv(16384)


    return repr(data.decode('utf-8'))
    
