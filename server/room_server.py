from server.classes.player import Player
class Room_server:
    def __init__(self):
        self.player = {}
    
    def add_player(self, number, addr):
        if number == 1:
            self.player[addr] = Player("left")
        if number == 2:
            self.player[addr] = Player("right")
        print(self.player)

room_server = Room_server()
