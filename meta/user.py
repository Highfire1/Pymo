import json

class User:
    def __init__(self, id=0, username="bob", data=""):
        self.id = id
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
        
        self.equipment = {
            0:1,
            1:1,
            2:10
        }

        
        self.needSync = True # set this to true whenever we modify ANYTHING about user
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
    
    def toJSON(self):
        attributes = [self.hp, self.mana, self.x, self.y]
        credentials = [self.id, self.password]

        data = json.dumps([credentials, attributes, self.equipment])

        return data


    def fromJSON(self, json):
        data = json.loads(json)

        self.hp = data[1][0]
        self.mana = data[1][1]
        self.x = data[1][2]
        self.y = data[1][3]

        self.equipment = data[1]