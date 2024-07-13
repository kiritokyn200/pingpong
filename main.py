from config import config
import pygame
from screenmanager.screen__manager import screen_manager


window = pygame.display.set_mode((config["width"], config["hight"]))
pygame.display.set_caption("pingpong")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    window.fill((100,0,100))
    screen_manager.render(window)
    pygame.display.update()