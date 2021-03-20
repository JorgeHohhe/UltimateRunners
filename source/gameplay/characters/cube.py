import pygame
from .character_class import Character
from ...graphics.images_loader import CUBE, BASE, BLOCK
from ..utils.constants import *

class Cube(Character):

    def __init__(self, y, vel):
        super().__init__(y, vel, CUBE, CUBE_GRAV, CUBE_ROTATION_VEL)
        self.tilt = 0
        self.height = img.get_height()

    def could_jump(self, blocks):

        if self.grav >0 and self.y == WIN_HEIGHT - BASE.get_height() - self.img.get_height() + 5:
            return True
        elif self.grav <0 and self.y == BASE.get_height() - self.img.get_height()/2+5:
            return True
        else:
            for block in blocks:
                if self.y == block.y - self.img.get_height():
                    return True

            return False

    def jump(self):
        if self.grav > 0:
            self.vel = -15
        else:
            self.vel = 15

        self.rot += 1
        if self.rot == 5:
            self.rot = 1
            self.tilt = 0

    def move(self, blocks):
        # CUBE PHYSICS
        self.vel += self.grav
        self.y += self.vel

        # CUBE AND BASE INTERACTION
        if self.y > WIN_HEIGHT - BASE.get_height() - self.img.get_height() + 5:
            self.y = WIN_HEIGHT - BASE.get_height() - self.img.get_height() + 5
            self.vel = 0
        
        # CUBE AND TOP INTERACTION
        if self.y < BASE.get_height() - self.img.get_height()/2+5:
            self.y = BASE.get_height() - self.img.get_height()/2+5
            self.vel = 0    

        # CUBE AND BLOCKS INTERACTION
        for block in blocks:
            if self.x + CUBE.get_width() > block.x and self.x < block.x + BLOCK.get_width():
                if self.y + CUBE.get_height() > block.y:
                    self.y = block.y - self.img.get_height()
                    self.vel = 0

        # CUBE ROTATION AFTER JUMP
        if self.tilt > -90 * self.rot:
            self.tilt -= self.rot_vel

    def draw(self, win):
        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_image.get_rect(center=self.img.get_rect(topleft=(self.x, self.y)).center)
        win.blit(rotated_image, new_rect.topleft)
