import pygame
from screenmanager.gamescreen.elem_screen import elem_screen

class Game_screen:
    def __init__(self):
        self.name = "game_screen"
        self.color = (0,100,50)

    def render(self, window):
        window.fill(self.color)
#        for elem in elem_screen:
 #           elem_screen[elem].render(window)