class Player():
    def __init__(self, pos):
        self.pos = pos
        self.width = 10
        self.hight = 70
        self.y = 300
        if pos == "left":
            self.color = (255, 0, 0)
            self.x = 15
        if pos == "right":
            self.color = (0, 0, 255)
            self.x = 800 - 85

        


