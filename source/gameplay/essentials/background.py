import pygame
from ...graphics.images_loader import BG
from ..utils.constants import VEL

class Bg:
    WIDTH = BG.get_width()

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH
        self.img1 = BG
        self.img2 = pygame.transform.flip(BG, True, False)

    def move(self):
        self.x1 -= VEL - 7.5
        self.x2 -= VEL - 7.5

        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH

        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

    def draw(self, win):
        win.blit(self.img1, (self.x1, self.y))
        win.blit(self.img2, (self.x2, self.y))
