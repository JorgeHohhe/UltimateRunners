import pygame
from ..utils.constants import *


class Character:

    def __init__(self, y, vel, img, rot, g, rot_vel):
        self.x = INITIAL_X
        self.y = y
        self.vel = vel
        self.img = img
        self.rot = rot
        self.grav = g
        self.rot_vel = rot_vel
        self.height = self.img.get_height()
        self.width = self.img.get_width()

    def blocks_interaction(self, blocks):
        for block in blocks:
            if self.x + self.width > block.x and self.x < block.x + block.img.get_width():
                if self.y + self.height > block.y:
                    self.y = block.y - self.height
                    self.vel = 0

    def get_mask(self):
        return pygame.mask.from_surface(self.img)
        
    def get_gravity(self):
        return self.grav
    
    def change_gravity(self, val):
        self.grav = val
     
    def get_velocity(self):
        return self.vel
            
    def change_velocity(self, val):
        self.vel = val

    def set_height(self, h):
        self.y = h
