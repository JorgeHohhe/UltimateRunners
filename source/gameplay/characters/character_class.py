import pygame
from ..utils.constants import *

class Character:

    def __init__(self, x, y, img, g, rot_vel):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick = 0
        self.vel = 0
        self.img = img
        self.rot = 0
        self.grav = g
        self.rot_vel = rot_vel

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
