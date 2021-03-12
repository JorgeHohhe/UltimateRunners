import pygame
from ....graphics.images_loader import SPIKE
from ..component_class import component

class Spike(component):

    def __init__(self, x, y, angle):
        super().__init__(x, y, angle, SPIKE)

    def collision(self, cube):
        cube_mask = cube.get_mask()
        spike_mask = pygame.mask.from_surface(self.img)
        offset = (round(self.x - cube.x), round(self.y - cube.y))
        point = cube_mask.overlap(spike_mask, offset)

        if point:
            return True

        return False
