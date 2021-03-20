import pygame
from .character_class import Character
from ...graphics.images_loader import DRAGON, BASE, BLOCK
from ..utils.constants import *

class Dragon(Character):

    def __init__(self, y, vel):
        super().__init__(y, vel, DRAGON, 0, DRAG_GRAV, DRAG_ROTATION_VEL)
        self.height = img.get_height()

    def up(self):
        self.vel += -6*self.grav
        #self.y += self.vel

    def move(self):
        # LASER PHYSICS
        self.vel += self.grav
        self.y += self.vel
        
        # MAX VEL
        if self.vel > DRAG_MAX_VEL:
            self.vel = DRAG_MAX_VEL

        # DRAGON AND BASE INTERACTION
        if self.y > WIN_HEIGHT - BASE.get_height() - self.height * 3 / 4:
            self.y = WIN_HEIGHT - BASE.get_height() - self.height * 3 / 4
            self.vel = 0
            self.rot = 0
        elif self.y < BASE.get_height() - self.height * 3 / 4:
            self.y = BASE.get_height() - self.height * 3 / 4
            self.vel = 0
            self.rot = 0
            
        self.rot = - DRAG_ROTATION_VEL * self.vel

    def draw(self, win):
        rotated_image = pygame.transform.rotate(self.img, self.rot)
        new_rect = rotated_image.get_rect(center=self.img.get_rect(topleft=(self.x, self.y)).center)
        win.blit(rotated_image, new_rect.topleft)
