'''
map specifications

2d

there are locations where if you're within a range you can do something

stretch goals:
several floors


intakes:
a png file that starts at 0,0 
bounding box
list of POI's

'''
import pygame

class Level(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 

        self.worldName = "World 1"
        self.worldDescription = "The First World"
        self.file = "map2.png"
        self.points = {
            "tree": [[10, 10], [15, 15]],
            "berries": [[5, 5], [20, 20]]
        }
        self.spawn = (-600, 846)

        self.image = pygame.image.load(f"assets/maps/{self.file}").convert()
        self.rect = self.image.get_rect()

    
    def update(self):
        pass

    def draw(self, screen, x, y):
        self.rect.center = (x, y)
        screen.blit(self.image, self.rect)

        