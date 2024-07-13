from exemplesurfaces.exemle_button.button import Button #Класс для создание кнопок
from client.client import start_client
from server.server import start_server

def click_button_start_server():
    start_server()
def click_button_start_client():
    start_client()


elem_screen = {
    "button_start_server": Button(200, 100, 300, 300, (100, 140, 160), (140, 160, 180), click_button_start_server, "Start server"),
    "button_start_client": Button(200, 100, 300, 150, (100, 140, 160), (140, 160, 180), click_button_start_client, "Connect to the server"),
}
