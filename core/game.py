import pygame
import sys
from core.controller import Controller
from core.sprites.level import Level
from meta.user import User

class Game:
    def __init__(self):
        pygame.init()

        # Global constants
        SCREEN_WIDTH = 1000
        SCREEN_HEIGHT = 800
        FRAME_RATE = 60

        # Creating the screen and the clock
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
        self.screen.set_alpha(0)  # Make alpha bits transparent
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

            #self.level.draw(self.screen)
            self.players.draw(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # When user clicks the 'x' on the window, close our game
                    # TODO: close socket
                    pygame.quit()
                    sys.exit()

            #keys_pressed = pygame.key.get_pressed()
            #if keys_pressed[pygame.K_x]:
            #    print("Adding Player")


            # USER CONTROL
            await self.controller.update()
            self.controller.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)
            self.screen.fill((0,0,0))

            
