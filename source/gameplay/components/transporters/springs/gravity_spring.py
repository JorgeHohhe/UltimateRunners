import pygame
from .....graphics.images_loader import GRAV_SPRING
from ...component_class import Component


class GravSpring(Component):

    def __init__(self, x, y, angle):
        super().__init__(x, y, angle, GRAV_SPRING)
        self.activated = False

    def collision(self, player):
        cube_mask = player.get_mask()
        gspring_mask = pygame.mask.from_surface(self.img)
        offset = (round(self.x - player.x), round(self.y - player.y))
        point = cube_mask.overlap(gspring_mask, offset)

        if point and not self.activated:        
            player.change_velocity(-player.get_velocity())
            player.change_gravity(-player.get_gravity())
            self.activated = True
