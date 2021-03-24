import pygame
from .character_class import Character
from ...graphics.images_loader import LASER, LASER_BACK, BASE
from ..utils.constants import *


class Laser(Character):

    def __init__(self, y):
        super().__init__(y, 10, LASER, -135, 1, 0)
        self.img_back = LASER_BACK
        self.locals = list()

    def up(self):

        self.vel = -10*self.grav
        self.rot = 45*self.grav - 90

    def down(self):

        self.vel = 10*self.grav
        self.rot = -45*self.grav - 90

    def move(self):
        # LASER PHYSICS
        self.y += self.vel

        # LASER AND BASE INTERACTION
        if self.y > WIN_HEIGHT - BASE.get_height() - self.height * 3 / 4:
            self.y = WIN_HEIGHT - BASE.get_height() - self.height * 3 / 4
            self.vel = 0
            self.rot = -90
        elif self.y < BASE.get_height() - self.height * 3 / 4:
            self.y = BASE.get_height() - self.height * 3 / 4
            self.vel = 0
            self.rot = -90

    def draw(self, win):
        rotated_image = pygame.transform.rotate(self.img, self.rot)
        new_rect = rotated_image.get_rect(center=self.img.get_rect(topleft=(self.x, self.y)).center)
        win.blit(rotated_image, new_rect.topleft)

        self.locals.append([self.x + 12, self.y + self.height / 2 - self.img_back.get_height() / 2])
        for local in self.locals:
            local[0] -= VEL
            win.blit(self.img_back, local)
