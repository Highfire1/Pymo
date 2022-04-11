import pygame
import os
from math import copysign

class Player(pygame.sprite.Sprite):
    def __init__(self, user, x = 200, y = 200, width = 30, height = 30, color = None):
        super().__init__() 

        # pygame things
        # image is what the sprite looks like   
        # rect is where image is drawn
        image_location = os.path.join("assets", "player.png")
        self.image = pygame.image.load(image_location)
        self.image = pygame.transform.scale(self.image, (50, 50))

        # rect is where image is drawn
        self.rect = self.image.get_rect()
        self.rect.center = (1000 / 2, 800 / 2)


        self.textRect = self.image.get_rect()
        self.textRect.x = 0
        self.textRect.y = 0

        self.contactCheckRect = self.image.get_rect()

        self.oldcollided = []
        self.collision = False

        self.user = user

    def update(self):
        return
        
        
    def draw(self, screen, x, y):
        if not self.user.visible:
            return
            
        self.rect.center = (x, y)
        # draw player
        screen.blit(self.image, self.rect)

        #print(f"player.py: {self.user.username} is at {x}, {y}")

        # draw x/y of player sprite


        #pygame.draw.rect(screen, (255,255,255), (self.rect.x, self.rect.y, 5, 5))


        
