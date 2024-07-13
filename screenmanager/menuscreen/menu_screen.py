import pygame
from screenmanager.menuscreen.elem_screen import elem_screen

class Menu_screen:
    def __init__(self):
        self.name = "menu_screen"
        self.color = (50,100,0)

    def render(self, window):
        window.fill(self.color)
        for elem in elem_screen:
            elem_screen[elem].render(window)
        
    