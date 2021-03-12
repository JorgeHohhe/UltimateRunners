import pygame
from ...graphics.images_loader import BASE
from ..utils.constants import VEL

class Base:
    WIDTH = BASE.get_width()

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH
        self.img = BASE

    def move(self):
        self.x1 -= VEL
        self.x2 -= VEL

        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH

        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

    def draw(self, win):
        win.blit(self.img, (self.x1, self.y))
        win.blit(self.img, (self.x2, self.y))
