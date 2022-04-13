import pygame
import sys
import os
import asyncio
import json
from core.controller import Controller
from core.sprites.level import Level
from meta.user import User
from core.server.out import loadServer

class Server:
    def __init__(self):
        pygame.init()

        # Global constants
        SCREEN_WIDTH = 1000
        SCREEN_HEIGHT = 800
        FRAME_RATE = 60

        # Creating the screen and the clock
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
        self.screen.set_alpha(0)  # Make alpha bits transparent (?)
        self.clock = pygame.time.Clock()

        


        # TODO: get user from server
        user = User()
        user.visible = False

        level = Level()
        self.controller = Controller(user=user, level=level)
        self.controller.server = True

        self.players = pygame.sprite.Group()
        self.users = self.load_users()


        # TODO: get game world data from server
        

    
    def load_users(self):
        users = []

        for fi in os.listdir("data\\users"):
            with open(f"{os.getcwd()}\\data\\users\\{fi}", "r") as user:
                data = user.read()

                u = User().fromJSON(data)
                users.append(u)
        
        return users

    def usersToJSON(self):
        data = []
        for user in self.users:
            data.append(user.toJSON())
        return json.dumps(data)
        
    def usersFromJSON(self, data):
        data = json.loads(json)
        users = []
        for user in data:
            users.append(json.loads(user))
        return user

    
    async def mainLoop(self):
        
        await asyncio.create_task(loadServer())

        print("this is not printing")
        

        while True:
            self.players.update()

            #self.level.draw(self.screen)
            self.players.draw(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # When user clicks the 'x' on the window, close our game
                    pygame.quit()
                    sys.exit()

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
            for user in self.users:
                if user.needSync:
                    print("SAVING DATA FOR A USER")
                    self.writeUserData(user)





    async def writeUserData(self, user: User):
        with open(f"{os.getcwd()}\\data\\users\\{user.id}", "w") as fi:
            fi.write(user.toJSON())

                    
    

            

            
