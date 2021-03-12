import pygame
from .....graphics.images_loader import GRAV_SPRING
from ...component_class import component

class Grav_Spring(component):

    def __init__(self, x, y, angle):
        super().__init__(x, y, angle, GRAV_SPRING)

    def collision(self, cube):
        cube_mask = cube.get_mask()
        gspring_mask = pygame.mask.from_surface(self.img)
        offset = (round(self.x - cube.x), round(self.y - cube.y))
        point = cube_mask.overlap(gspring_mask, offset)

        if point:
            if cube.get_velocity() is not 0:
                cube.change_velocity(-cube.get_velocity())
                cube.change_gravity(-cube.get_gravity())
