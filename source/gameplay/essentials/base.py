import pygame
from ...graphics.images_loader import BASE
from ..utils.constants import VEL, WIN_HEIGHT


class Base:
    WIDTH = BASE.get_width()
    HEIGHT = BASE.get_height()

    def __init__(self):
        self.y_bottom = WIN_HEIGHT - self.HEIGHT
        self.y_top = - self.HEIGHT / 2
        self.x1 = 0
        self.x2 = self.WIDTH
        self.img_bottom = BASE
        self.img_top = pygame.transform.flip(BASE, False, True)

    def move(self):
        self.x1 -= VEL
        self.x2 -= VEL

        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH

        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

    def draw(self, win):
        win.blit(self.img_bottom, (self.x1, self.y_bottom))
        win.blit(self.img_bottom, (self.x2, self.y_bottom))
        win.blit(self.img_top, (self.x1, self.y_top))
        win.blit(self.img_top, (self.x2, self.y_top))
