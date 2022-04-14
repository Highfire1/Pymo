import json
import random
import hashlib

class User:
    def __init__(self, id=0, username=None, data=""):
        self.id = id

        if username == None:
            username = str(random.randint(100000, 999999))
        self.username = username
        self.password = username 

        self.camerax = 0
        self.cameray = 0

        self.x = 0
        self.y = 0

        self.speed = 10

        self.visible = True

        self.hp = 100
        self.damage = 1
        self.mana = 100

        # 0 slot of inventory is CHATMESSAGE
        # everything else tbd
        '''
        slot 0: chat
        slot 1: skin (1 - 5)
        '''
        self.equipment = []

        for i in range(0, 5):
            self.equipment.append(0)
        
        self.equipment[1] = random.randint(1, 5)
        self.equipment[2] = 1
        self.equipment[3] = 10

        
        self.lastJSON = self.toJSON()
        

    '''
    Player attributes:
    all must know:
    1) HP
    3) Mana
    5) Items
    6) player position and vectors... ;-;

    calculated client side:
    2) Damage
    4) Speed

    TODO: set out items and their effects

    '''

    def addItem(self, id, add):
        # TODO error/sanity checks
        self.equipment[id] += add
    
    def toJSON(self):
        credentials = [self.id, self.password]
        attributes = [self.hp, self.mana, self.x, self.y]

        data = json.dumps([credentials, attributes, self.equipment])

        # remove message
        #self.equipment[0] = ""

        return data


    def fromJSON(self, payload):
        try:
            data = json.loads(payload)
        except:
            print("FAILED ON", payload)

        self.id = data[0][0]
        self.password = data[0][1]

        self.hp = data[1][0]
        self.mana = data[1][1]
        self.x = data[1][2]
        self.y = data[1][3]

        self.equipment = data[2]
    
    def hash(self):
        # very secure i know shush
        return self.password
