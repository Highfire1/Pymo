from queue import Queue
import pygame
import sys
import os
import asyncio
import json
import threading
from core.controller import Controller
from core.sprites.level import Level
from meta.user import User
from core.networking.server import loadServer
from core.networking.client import sendToServer

class Server:
    def __init__(self):
        pygame.init()

        # Global constants
        SCREEN_WIDTH = 500
        SCREEN_HEIGHT = 400
        FRAME_RATE = 60

        # Creating the screen and the clock
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
        self.screen.set_alpha(0)  # Make alpha bits transparent (?)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Pymo Server!")

        


        # TODO: get user from server
        user = User()
        user.visible = False

        level = Level()
        self.controller = Controller(user=user, level=level)
        self.controller.server = True
        self.controller.serverObj = self

        self.players = pygame.sprite.Group()
        self.users = self.load_users()


        # TODO: get game world data from server

        

    
    def load_users(self):
        users = []

        for fi in os.listdir("data\\users"):
            with open(f"{os.getcwd()}\\data\\users\\{fi}", "r") as user:
                data = user.read()

                u = User()
                u.fromJSON(data)
                u.needSync = False
                users.append(u)
                
        
        
        return users

    def usersToJSON(self):
        data = ""
        for user in self.users:
            data += user.toJSON() + "||||"
        
        return data
        
    def usersFromJSON(self, data):
        data = data[1:-1]
        data = data.split("||||")
        data.pop(-1) #cause i suck at coding
        for d in data:
            print(d)
        users = []
        for user in data:
            u = User()
            users.append(u.fromJSON(user))
        return users
    
    def updatePlayer(self, userData: str):
        newUser = User()
        newUser.fromJSON(userData)


        for user in self.users:
            if user.hash() == newUser.hash():
                # if update from user, then overwrite their serverside things
                # yes there is no user validation 
                # i refuse to do that in python :)
                user.fromJSON(userData) 
                return user     

        self.users.append(newUser) # add if new player
        return newUser     



    
    async def mainLoop(self):

        queueSend = Queue()
        queueReceive = Queue()
        
        # wow threading and asyncio is incredibly painful thanks stackoverflow
        self.serverThread = threading.Thread(target=asyncio.run, args=(loadServer(queueSend, queueReceive),))
        self.serverThread.daemon = True # close this thread when main thread closes
        self.serverThread.start()
        #self.controller.serverThread = self.serverThread
        

        while True:
            
            # the secret sauce:
            # Get new information from clients :)
            #print(queueReceive.empty())
            if not queueReceive.empty():
                data = queueReceive.get()
                user = self.updatePlayer(data)
                #print("new data recieved from", user.username)
            
            # TODO: send the updates to clients

            queueSend.queue.clear() #clear the queue
            queueSend.put(self.usersToJSON())
            #print("ADDED", self.usersToJSON(), "The queue is currently", queueSend.empty())





            self.players.update()

            #self.level.draw(self.screen)
            self.players.draw(self.screen)

            #keys_pressed = pygame.key.get_pressed()
            #if keys_pressed[pygame.K_x]:
            #    print("Adding Player")


            
            await self.controller.update()
            self.controller.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)
            self.screen.fill((0,0,0))

            # recieve updates

            
            #print(x)



            # push updates to file and players


            # store user data to file
            #for user in self.users:
            #    if user.needSync:
            #        await self.writeUserData(user)
            #        user.needSync = False





    async def writeUserData(self, user: User):
        with open(f"{os.getcwd()}\\data\\users\\{user.username}", "w") as fi:
            fi.write(user.toJSON())

                    
    

            

            
