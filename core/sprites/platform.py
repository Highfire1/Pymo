import pygame
import os
import math

class Platform(pygame.sprite.Sprite):
    def __init__(self, x = 0, y = 0, width = 30, height = 30, color = None):
        super().__init__() 

        # pygame things
        # image is what the sprite looks like   
        # rect is where image is drawn
        image_location = os.path.join("assets", "oink.gif")
        self.image = pygame.image.load(image_location)
        self.image = pygame.transform.scale(self.image, (300, 50))

        image_location = os.path.join("assets", "player.png")
        self.image2 = pygame.image.load(image_location)
        self.image2 = pygame.transform.scale(self.image2, (300, 50))

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.speed = 3

        self.contactCheckRect = self.image.get_rect()
        self.contactCheckRect.width = self.rect.width + 1
        self.contactCheckRect.height = self.rect.height + 1

        self.oldcollded = []
        

    def maxX(self):
        return self.x + self.width
    

    def draw(self, screen):

        # draw platform
        screen.blit(self.image, self.rect)

        # draw red dot for x/y
        pygame.draw.rect(screen, (255,0,0), (self.rect.x, self.rect.y, 5, 5))

        # draw bounding box
        #screen.blit(self.image2, self.contactCheckRect)




    def update(self, all_sprites):
        
        # check if anyone touching platform
        self.contactCheckRect.center = self.rect.center
        self.contactCheckRect.x -= 1
        self.contactCheckRect.y -= 1

        collided = []

        for sprite in all_sprites:
            if self.contactCheckRect.colliderect(sprite.rect):
                collided.append(sprite)
                sprite.collision = True
            
        
        self.move(collided)

        #self.oldcollided = collided
        
    def move(self, collided):
        w, h = pygame.display.get_surface().get_size()
        
        self.rect.x += self.speed
        cycle = self.rect.x > w

        if cycle:
            self.rect.x -= w + self.rect.width

        for sprite in collided:
            sprite.rect.x += self.speed

            if cycle:
                sprite.rect.x -= w + self.rect.width
        


