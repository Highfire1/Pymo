import pygame
import os
from math import copysign

class Player(pygame.sprite.Sprite):
    def __init__(self, x = 200, y = 200, width = 30, height = 30, color = None):
        super().__init__() 

        # pygame things
        # image is what the sprite looks like   
        # rect is where image is drawn
        image_location = os.path.join("assets", "player.png")
        self.image = pygame.image.load(image_location)
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect()
        self.rect.center = (1000 / 2, 800 / 2)

        self.speed = 5
        self.verticalVelocity = 0
        self.platform = None

        self.setText("placeholder")
        self.textRect = self.image.get_rect()
        self.textRect.x = 0
        self.textRect.y = 0

        self.contactCheckRect = self.image.get_rect()

        self.oldcollided = []
        self.collision = False


    def setText(self, text):
        font = pygame.font.Font('freesansbold.ttf', 32)
        self.text = font.render(text, True, (255, 255, 255))


    def update(self, all_sprites):
        
        keys_pressed = pygame.key.get_pressed()


        # X AXIS
        modifier = 0
        if keys_pressed[pygame.K_LEFT]:
            modifier -= self.speed
        if keys_pressed[pygame.K_RIGHT]:
            modifier += self.speed
        
        self.rect.x += modifier

        collided = pygame.sprite.spritecollide(self, all_sprites, dokill=False)
        if modifier == 0:
            for sprite in collided:
                modifier += -sprite.speed 
            
        while len(collided) != 0:
            self.rect.x -= int(copysign(1, modifier))
            collided = pygame.sprite.spritecollide(self, all_sprites, dokill=False)

        gravity = -9.81

        # Y AXIS
        modifier = 0    

        # how to check if touching a platform:
        # a) platform tells player
        # b) player does own collision checking
        # c) ???

        if keys_pressed[pygame.K_UP] and self.collision:
            self.verticalVelocity = -20
        elif self.collision:
            self.verticalVelocity = 0

        self.collision = False
        #if keys_pressed[pygame.K_DOWN]:
        #    modifier += self.speed

        self.verticalVelocity += 0.5
        print(self.verticalVelocity)

        if self.rect.y > 800:
            self.verticalVelocity = -30



        modifier = self.verticalVelocity
        self.rect.y += modifier

        

        collided = pygame.sprite.spritecollide(self, all_sprites, dokill=False)
        while len(collided) != 0:
            self.rect.y -= int(copysign(1, modifier))
            collided = pygame.sprite.spritecollide(self, all_sprites, dokill=False)
        
        # print coordinates
        self.setText(f"({self.rect.x}, {self.rect.y})")


        
    def draw(self, screen):
        # draw player
        screen.blit(self.image, self.rect)

        # draw x/y of player sprite
        pygame.draw.rect(screen, (255,0,0), (self.rect.x, self.rect.y, 5, 5))

        # print player coordinates
        screen.blit(self.text, self.textRect)


        
