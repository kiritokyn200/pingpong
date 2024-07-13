import socket
from config import config
from threading import Thread



def start_client():
    client = Client((config["localhost"], config["port"]))

class Client:
    def __init__(self, addr):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(addr)
        Thread(target=self.request).start()
    def request(self):
        while True:
            data = self.sock.recv(4096).decode()

            if data == 'start_game':
                config["active_screen"] = "game_screen"
                print("START GAME")
#            if 'data_players' in data:
 #               for player in data['data_players']:
  #                  if player.pos == "left":
   #                     elem_screen["racket"]["left"] = player
    #                if player.pos == "right":
     #                   elem_screen["racket"]["right"] = player

            self.sock.send(bytes('client -> server', encoding = 'UTF-8'))
            
   
            
    
            