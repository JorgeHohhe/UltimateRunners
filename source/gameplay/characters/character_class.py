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
