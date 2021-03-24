import pygame
from .character_class import Character
from ...graphics.images_loader import ORB, BASE, BLOCK
from ..utils.constants import *


class Orb(Character):

    def __init__(self, y, vel):
        super().__init__(y, vel, pygame.transform.flip(ORB, True, False), 0, ORB_GRAV, ORB_ROTATION_VEL)

    def could_switch(self, blocks):

        if self.y == WIN_HEIGHT - BASE.get_height() - self.height:
            return True
        elif self.y == - BASE.get_height() / 2 + self.height * 3 / 4:
            return True
        else:
            for block in blocks:
                if self.y == block.y - self.height:
                    return True

            return False

    def switch(self):
        self.grav *= -1

    def move(self):
        # ORB PHYSICS
        self.vel += self.grav
        self.y += self.vel

        # ORB AND BASE INTERACTION
        if self.y > WIN_HEIGHT - BASE.get_height() - self.height:
            self.y = WIN_HEIGHT - BASE.get_height() - self.height
            self.vel = 0
        
        # ORB AND TOP INTERACTION
        if self.y < - BASE.get_height() / 2 + self.height * 3 / 4:
            self.y = - BASE.get_height() / 2 + self.height * 3 / 4
            self.vel = 0    
            
        # CUBE ROTATION AFTER JUMP
        self.rot -= self.rot_vel * self.grav / ORB_GRAV

    def draw(self, win):
        rotated_image = pygame.transform.rotate(self.img, self.rot)
        new_rect = rotated_image.get_rect(center=self.img.get_rect(topleft=(self.x, self.y)).center)
        win.blit(rotated_image, new_rect.topleft)
