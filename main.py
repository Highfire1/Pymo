# Session 2 Exercise 1
# Main file
#
# There are some bare tree trunks in the DRAW section and a class called Leaves inside the file leaves.py
# Add some leaves objects to decorate the tree trunks
# Don't worry about getting your coordinates exactly right

import sys
import pygame
import random

from platform import Platform
from player import Player
from game import Game
from map import Map
# ------------------------------ Exercise 1 Comments ------------------------------
# Added the line above to import the Leaves class from leaves.py
# To create a leaves object, type the following inside the SETUP section:
#   leaves = Leaves()
# ---------------------------------------------------------------------------------

"""
SETUP section - preparing everything before the main loop runs
"""
pygame.init()

# Global constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
FRAME_RATE = 60

# Useful colors 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (168, 119, 50)

# Creating the screen and the clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
screen.set_alpha(0)  # Make alpha bits transparent
clock = pygame.time.Clock()


"""
CREATE THINGS

    
players = pygame.sprite.Group()
platforms = pygame.sprite.Group()

player = Player()

players.add(player)

for i in range(5):
    rx = random.randint(0, SCREEN_WIDTH+300)
    ry = i/5*SCREEN_HEIGHT
    pl = Platform(x=rx, y=ry)

    print()

    platforms.add(pl)

all_sprites = pygame.sprite.Group()
all_sprites.add(players)
all_sprites.add(platforms)
"""

game = Game()


'''
1) create server    
2) host to web
3) establish connection to client
4) sync data

'''



"""
MAIN LOOP


def display_loop():
    screen.fill(BLACK)

    players.update(platforms)
    platforms.update(players)
    

    for sprite in all_sprites:
        sprite.draw(screen)

    pygame.display.flip()  
    clock.tick(FRAME_RATE)      

"""
"""
PYGAME SHENANIGANS
"""
def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # When user clicks the 'x' on the window, close our game
            pygame.quit()
            sys.exit()


while True:
    handle_events()
    display_loop()