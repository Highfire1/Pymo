import pygame
import os
import asyncio
import json
from math import copysign
from meta.user import User
from core.sprites.player import Player
from core.client import sendToServer

'''
The controller
this place controls the player sprite and the map
'''

class Controller():
    def __init__(self, user: User, level):

        self.user = user
        self.sprite = Player(user)  
        self.level = level

        if self.user.x == 0 and self.user.y == 0:
            x, y = self.level.spawn
            self.user.x = x
            self.user.y = y
        
        self.server = False

        self.connections = 0


    async def update(self):
        
        #TODO: fix diagonal movement being op

        if self.user == None:
            return
        
        keys_pressed = pygame.key.get_pressed()


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

        
        # print coordinates

        if not self.server and self.user.lastJSON != self.user.toJSON():
            self.user.lastJSON = self.user.toJSON()
            await sendToServer(self.user.toJSON())

    def usersFromJSON(self, data):
        data = json.loads(json)
        users = []
        for user in data:
            users.append(json.loads(user))
        return user

        
    def draw(self, screen):
        camx = int(self.user.camerax)
        camy = int(self.user.cameray)

        x = 0 - camx
        y = 0 - camy
        
        # draw background
        self.level.draw(screen, x, y)

        # draw player
        w, h = pygame.display.get_surface().get_size()

        x = self.user.x - camx + w/2
        y = self.user.y - camy + h/2
    
        
        self.sprite.draw(screen, x, y)

        #print(f"player is at {self.user.x}, {self.user.y}. The camera is at {camx}, {camy}.")
        


        
