import pygame
from ..utils.constants import *
from ...graphics.images_loader import PLAYER_EXPLOSION
from time import sleep


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
        self.gamemode = ""

        self.i = 0
        self.player_x = 0
        self.player_y = 0

    def blocks_interaction(self, blocks):
        for block in blocks:
            if self.x + self.width > block.x and self.x < block.x + block.img.get_width():
                if self.y + self.height > block.y:
                    self.y = block.y - self.height
                    self.vel = 0

    def death_effect(self, win):
        if self.i == 0:
            self.player_x = self.x
            self.player_y = self.y
        img_death = pygame.transform.scale(PLAYER_EXPLOSION[self.i], (250, 250))
        new_rect = img_death.get_rect(center=img_death.get_rect(topleft=(self.player_x - 75/2, self.player_y - 3*75/4)).center)
        win.blit(img_death, new_rect.topleft)
        sleep(0.06)
        self.i += 1

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
