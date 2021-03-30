import pygame
from .character_class import Character
from ...graphics.images_loader import CYCLOPS, BASE
from ..utils.constants import *


class Cyclops(Character):

    def __init__(self, y, vel):
        super().__init__(y, vel, CYCLOPS[0], 0, CYCL_GRAV, 0)
        self.flip = False
        self.img = CYCLOPS

    def could_switch(self, blocks):
        if self.y == WIN_HEIGHT - BASE.get_height() - self.height:
            return True
        elif self.y == - BASE.get_height() / 2 + self.height * 3 / 4:
            return True
        else:
            for block in blocks:
                if self.y == block.y - self.height:
                    return True
                elif self.y == block.y + block.img.get_height() - 8:
                    return True

            return False

    def switch(self):
        self.grav *= -1

    def move(self):
        # CYCLOPS PHYSICS
        self.vel += self.grav
        self.y += self.vel

        # CYCLOPS AND BASE INTERACTION
        if self.y > WIN_HEIGHT - BASE.get_height() - self.height:
            self.y = WIN_HEIGHT - BASE.get_height() - self.height
            self.vel = 0
        
        # CYCLOPS AND TOP INTERACTION
        if self.y < - BASE.get_height() / 2 + self.height * 3 / 4:
            self.y = - BASE.get_height() / 2 + self.height * 3 / 4
            self.vel = 0    
            
        # CYCLOPS ANIMATION
        self.rot += 0.5
        if self.rot == 7:
            self.rot = 0

    def draw(self, win):
        if self.grav > 0:
            self.flip = False
        else:
            self.flip = True

        flipped_image = pygame.transform.flip(self.img[int(self.rot)], False, self.flip)
        new_rect = flipped_image.get_rect(center=self.img[int(self.rot)].get_rect(topleft=(self.x, self.y)).center)
        win.blit(flipped_image, new_rect.topleft)
        
    def get_mask(self):
        return pygame.mask.from_surface(self.img[0])
