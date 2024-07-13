import pygame
from config import config
from screenmanager.menuscreen.menu_screen import Menu_screen
from screenmanager.gamescreen.game_screen import Game_screen

class Screen_manager:
    def __init__(self):
        self.menu_screen = Menu_screen()
        self.game_screen = Game_screen()
        
    def render(self, window):
        if config["active_screen"] == self.menu_screen.name:
            self.menu_screen.render(window)
        if config["active_screen"] == self.game_screen.name:
            self.game_screen.render(window)
screen_manager = Screen_manager()


