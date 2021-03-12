import pygame
from ..utils.constants import VEL

class component:

    def __init__(self, x, y, angle, img):
        self.x = x
        self.angle = angle
        self.y = y
        self.img = img

    def move(self):
        self.x -= VEL

    def draw(self, win):
        draw_img = pygame.transform.rotate(self.img, self.angle)
        win.blit(draw_img, (self.x, self.y))
