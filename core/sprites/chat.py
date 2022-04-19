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

class chatBox(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 

        self.messages = []
        self.typing = False
        self.chatBuffer = ""
        self.chatboxfont = pygame.font.SysFont('Comic Sans MS', 30)
    
    def parse(self, user):
        if user.equipment[0] not in self.messages and len(str(user.equipment[0])) > 0:
            self.messages.append(user.equipment[0])


    
    def update(self):
        pass

    def draw(self, screen):
        w, h = pygame.display.get_surface().get_size()

        self.messages.append(self.chatBuffer)

        textHeight = 60
        maxHeight = 60*len(self.messages)


        for line in self.messages:
            chatbox = self.chatboxfont.render(str(line), False, (255, 255, 255))
            screen.blit(chatbox, (0,h - maxHeight))
            maxHeight -= textHeight
        
        self.messages.pop(-1)

        