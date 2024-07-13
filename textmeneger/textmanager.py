import pygame
pygame.init()

class Text():
    def __init__(self, message, pos):
        self.f_sys = pygame.font.SysFont('verdana', 15, True)
        self.surf_text = self.f_sys.render(message, 0, (0, 0, 0))
        self.pos = self.surf_text.get_rect(center= pos)
    def render_text(self, window):
        window.blit(self.surf_text, self.pos)
    