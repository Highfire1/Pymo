import pygame
import sys
from core.controller import Controller
from core.sprites.level import Level
from meta.user import User

class Game:
    def __init__(self):
        pygame.init()

        # Global constants
        SCREEN_WIDTH = 500
        SCREEN_HEIGHT = 400
        FRAME_RATE = 60

        # Creating the screen and the clock
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
        self.screen.set_alpha(0)  # Make alpha bits transparent
        pygame.display.set_caption("Pymo!")

        self.clock = pygame.time.Clock()
        self.players = pygame.sprite.Group()


        # TODO: get user from server
        user = User()
        level = Level()
        self.controller = Controller(user=user, level=level)


        # TODO: get game world data from server

        
        # begin the actual game

    
    
    async def mainLoop(self):
        while True:
            self.players.update()


            
                


            # USER CONTROL
            await self.controller.update()
            self.controller.draw(self.screen)

            # PYGAME THINGS
            pygame.display.flip()
            self.clock.tick(60)
            self.screen.fill((0,0,0))

            
