import pygame
from screenmanager.menuscreen.elem_screen import elem_screen

class Game_screen:
    def __init__(self, window):
        self.window = window
        self.name = "name_screen"
        self.color = (100,0,50)

    def render(self):
        self.window.fill(self.color)
        for elem in elem_screen:
            elem_screen[elem].render(self.window)