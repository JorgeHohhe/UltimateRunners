import pygame
from ....graphics.images_loader import SPIKE
from ..component_class import Component


class Spike(Component):

    def __init__(self, x, y, angle, pixels_x, pixels_y):
        super().__init__(x, y, angle, SPIKE)
        self.img = pygame.transform.scale(self.img, (pixels_x, pixels_y))
        self.img = pygame.transform.rotate(self.img, self.angle)

    def collision(self, player):
        cube_mask = player.get_mask()
        spike_mask = pygame.mask.from_surface(self.img)
        offset = (round(self.x - player.x), round(self.y - player.y))
        point = cube_mask.overlap(spike_mask, offset)

        if point:
            return True

        return False

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))
