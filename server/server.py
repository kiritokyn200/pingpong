import socket
from config import config
from threading import Thread
from server.room_server import room_server

def start_server():
    server = Server((config["localhost"], config["port"]))

class Server:
    def __init__(self, addr):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(addr)
        self.max_accepts = 2
        self.connect_client = []
        self.is_start_game = False
        Thread(target=self.lisen_connection).start()

    def lisen_connection(self):
        self.sock.listen(self.max_accepts)
        while True:
            if len(self.connect_client) < 1:
                print("Server worked and wait new connection")
                client_sock, client_adress = self.sock.accept()
                Thread(target= self.lisen_client, args=(client_sock, client_adress)).start()
# Если комната наполнена то передать на клиенты сообщение об старте игры положение игроков 
            if len(self.connect_client) == 2 and self.is_start_game == False:
                for client_sock in self.connect_client:
                    client_sock.sendall(bytes('start_game', encoding = 'utf-8'))
#                    client_sock.sendall(bytes({'data_players': room_server.player}, encoding = 'utf-8'))
                    exit()

    def lisen_client(self, client_sock, client_adress):
        print("lisen new connection: ", client_adress)
        self.connect_client.append(client_sock)
        room_server.add_player(len(self.connect_client), client_adress)

        while True:
            data = client_sock.recv(4096).decode()
           
            client_sock.send(bytes('serve -> client', encoding = 'utf-8'))
            