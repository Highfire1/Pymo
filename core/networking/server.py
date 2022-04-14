# Code from stackoverflow (god bless)

import asyncio



class EchoServerProtocol(asyncio.Protocol):
    def __init__(self, queueSend, queueReceive):
        self.queueSend = queueSend
        self.queueReceive = queueReceive
        

    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        #print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        # RECIEVE DATA FROM CLIENTS
        message = data.decode()
        #print('Data received: {!r}'.format(message))
        self.queueReceive.put(message)


        # SEND WORLD STATE TO PLAYERS
        #print('Send: {!r}'.format(message))
        if not self.queueSend.empty():
            self.transport.write(self.queueSend.queue[0].encode('utf-8'))
            #print("sending world state!")
        #else:
            #self.transport.write("Hello World")

        #print('Close the client socket')
        self.transport.close()


async def loadServer(queueReceive, queueSend):
    # Get a reference to the event loop as we plan to use
    # low-level APIs.
    loop = asyncio.get_running_loop()

    server = await loop.create_server(
        lambda: EchoServerProtocol(queueReceive, queueSend),
        'localhost', 8080)

    async with server:
        print("Starting network of server...")
        await server.serve_forever()