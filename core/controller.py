import pygame
import os
import asyncio
import json
import sys
from math import copysign
from meta.user import User
from core.sprites.player import Player
from core.sprites.chat import chatBox
from core.networking.client import sendToServer

'''
The controller
this place controls the player sprite and the map
'''

class Controller():
    def __init__(self, user: User, level):

        self.user = user
        self.sprite = Player(user, user.equipment[1])  
        self.level = level

        if self.user.x == 0 and self.user.y == 0:
            x, y = self.level.spawn
            self.user.x = x
            self.user.y = y
        
        self.server = False 
        self.serverThread = None

        self.chatBox = chatBox()

        self.connections = 0

        self.users = []



    async def update(self):
        
        #TODO: fix diagonal movement being op

        if self.user == None:
            return
        
        keys_pressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # When user clicks the 'x' on the window, close our game
                # TODO: close socket
                # close threads
                if not self.serverThread == None:
                    self.serverThread.exit()               
                pygame.quit()
                sys.exit()


            if not event.type == pygame.KEYDOWN:
                continue
            
            # handle chat 
            if event.key == pygame.K_RETURN:
                if self.chatBox.typing:
                    self.user.equipment[0] = self.chatBox.chatBuffer
                    self.chatBox.chatBuffer = ""
                    self.user.needSync = True

                self.chatBox.typing = not self.chatBox.typing

            elif self.chatBox.typing:
                if event.key == pygame.K_BACKSPACE:
                    self.chatBox.chatBuffer = self.chatBox.chatBuffer[:-1]
                else:
                    self.chatBox.chatBuffer += event.unicode

                        
        


        
        
        keys_pressed = pygame.key.get_pressed()

        if not self.chatBox.typing:
            modifierx = 0
            modifiery = 0  

            # X AXIS
            if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
                modifierx -= self.user.speed
            if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
                modifierx += self.user.speed
            
            # Y AXIS  
            if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
                modifiery -= self.user.speed
            elif keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
                modifiery += self.user.speed

            self.user.x += modifierx
            self.user.y += modifiery

            # creates a dynamic camera
            diffx = self.user.x - self.user.camerax
            diffy = self.user.y - self.user.cameray


            self.user.camerax = self.user.camerax + diffx/10
            self.user.cameray = self.user.cameray + diffy/10

        
        # SEND CLIENT INFORMATION TO SERVER
        # AND RECIEVE INFORMATION FROM SERVER
        if not self.server:
            serverData = await sendToServer(self.user.toJSON())
            #print(serverData)
            self.users = self.usersFromJSON(serverData)

    

    def usersToJSON(self):
        data = ""
        for user in self.users:
            data += user.toJSON() + "||||"
        #print("SENDING", data)
        return data
    
        
    def usersFromJSON(self, data):
        data = data[1:-1]
        data = data.split("||||")
        data.pop(-1) #cause i suck at coding

        users = []
        for user in data:
            u = User()
            u.fromJSON(user)
            users.append(u)
            self.chatBox.parse(u)
        return users
        
    def draw(self, screen):
        camx = int(self.user.camerax)
        camy = int(self.user.cameray)
        w, h = pygame.display.get_surface().get_size()

        x = 0 - camx
        y = 0 - camy
        
        # draw background
        self.level.draw(screen, x, y)

        # draw other players

        for user in self.users:
            if not user.hash() == self.user.hash():
                x = user.x - camx + w/2
                y = user.y - camy + h/2

                print(user.equipment)

                pl = Player(user, user.equipment[1])  # create sprite

                pl.draw(screen, x, y)
                #print(x, y)
        
        

        # draw the controller
        

        x = self.user.x - camx + w/2
        y = self.user.y - camy + h/2
    
        
        self.sprite.draw(screen, x, y)

        #print(f"player is at {self.user.x}, {self.user.y}. The camera is at {camx}, {camy}.")

        # draw hud
        # chatbox
        # TODO: gray box like in minecraft
        #if self.chatBox.typing:
        self.chatBox.draw(screen)
            #chatbox = self.chatboxfont.render(self.chatBuffer, False, (255, 255, 255))
            #screen.blit(chatbox, (0,h - 60))


        


        
