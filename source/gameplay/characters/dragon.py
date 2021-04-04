import pygame
from .character_class import Character
from ...graphics.images_loader import DRAGON, BASE
from ..utils.constants import *


class Dragon(Character):

    def __init__(self, y, vel):
        super().__init__(y, vel, DRAGON, 0, DRAG_GRAV, DRAG_ROTATION_VEL)
        self.flip = False

    def up(self):
        self.vel += - 2 * self.grav
        self.y += self.vel

    def move(self):
        # DRAGON PHYSICS
        self.vel += self.grav
        self.y += self.vel
        
        # MAX VEL
        if self.vel > DRAG_MAX_VEL:
            self.vel = DRAG_MAX_VEL
        if self.vel < - DRAG_MAX_VEL:
            self.vel = - DRAG_MAX_VEL

        # DRAGON AND BASES INTERACTION
        if self.y > WIN_HEIGHT - BASE.get_height() - self.height:
            self.y = WIN_HEIGHT - BASE.get_height() - self.height
            self.vel = 0
            self.rot = 0
        elif self.y < - BASE.get_height() / 2 + self.height * 3 / 4:
            self.y = - BASE.get_height() / 2 + self.height * 3 / 4
            self.vel = 0
            self.rot = 0

        # DRAGON ROTATION
        self.rot = - self.rot_vel * self.vel

    def draw(self, win):
        if self.grav > 0:
            self.flip = False
        else:
            self.flip = True

        flipped_image = pygame.transform.flip(self.img, False, self.flip)
        rotated_image = pygame.transform.rotate(flipped_image, self.rot)
        new_rect = rotated_image.get_rect(center=self.img.get_rect(topleft=(self.x, self.y)).center)
        win.blit(rotated_image, new_rect.topleft)
