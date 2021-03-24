import pygame
from .....graphics.images_loader import GRAV_SPRING
from ...component_class import Component


class GravSpring(Component):

    def __init__(self, x, y, angle):
        super().__init__(x, y, angle, GRAV_SPRING)
        self.activated = False

    def collision(self, cube):
        cube_mask = cube.get_mask()
        gspring_mask = pygame.mask.from_surface(self.img)
        offset = (round(self.x - cube.x), round(self.y - cube.y))
        point = cube_mask.overlap(gspring_mask, offset)

        if point and not self.activated:        
            cube.change_velocity(-cube.get_velocity())
            cube.change_gravity(-cube.get_gravity())
            self.activated = True
