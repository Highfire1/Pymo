class User:
    def __init__(self, id=0, username="bob", data=""):
        self.id = id
        self.username = username
        self.data = data

        self.camerax = 0
        self.cameray = 0

        self.x = 0
        self.y = 0

        self.speed = 10

        self.visible = True
    
