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

class Map(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 

        self.mapName = "World 1"
        self.mapDescription = "The First World"
        self.file = "map1.py"
        self.points = {
            "tree": [[10, 10], [15, 15]],
            "berries": [[5, 5], [20, 20]]
        }
    
    def update(self):
        pass