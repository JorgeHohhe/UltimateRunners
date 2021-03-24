import pygame
from ....graphics.images_loader import SPIKE
from ..component_class import Component


class Spike(Component):

    def __init__(self, x, y, angle, pixels_x, pixels_y):
        super().__init__(x, y, angle, SPIKE)
        self.img = pygame.transform.scale(self.img, (pixels_x, pixels_y))

    def collision(self, cube):
        cube_mask = cube.get_mask()
        spike_mask = pygame.mask.from_surface(self.img)
        offset = (round(self.x - cube.x), round(self.y - cube.y))
        point = cube_mask.overlap(spike_mask, offset)

        if point:
            return True

        return False
