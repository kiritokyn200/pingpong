import pygame
from textmeneger.textmanager import Text #Класс для отрисовки заданного текста на заданной поверхности


class Button:
    def __init__(self, width, hight, x, y, unactive_color, active_color, function, message):
        self.width = width
        self.hight = hight
        self.x = x
        self.y = y
        self.unactive_color = unactive_color
        self.active_color = active_color
        self.function = function
        self.message = message
        self.font = Text(self.message, (((self.width // 2) + self.x), ((self.hight // 2) + self.y)))
    def render(self, window):
        pos_mouse = pygame.mouse.get_pos()
        
        if pos_mouse[0] > self.x and pos_mouse[1] > self.y and pos_mouse[0] < self.x + self.width and pos_mouse[1] < self.y + self.hight:
            pygame.draw.rect(window, self.active_color, (self.x, self.y, self.width, self.hight))
            for elem in pygame.event.get():
                if elem.type == pygame.MOUSEBUTTONUP:
                    if  elem.button == 1:
                        self.function()
            
        else :
            pygame.draw.rect(window, self.unactive_color, (self.x, self.y, self.width, self.hight))
        self.font.render_text(window)
