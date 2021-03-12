import pygame
from ....graphics.images_loader import BLOCK, SIDE
from ..component_class import component

class Block(component):

    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.img = BLOCK
        self.side_img1 = pygame.transform.rotate(SIDE, 90)

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))
        win.blit(self.side_img1, (self.x - self.side_img1.get_width(), self.y))

    def collision(self, cube):
        cube_mask = cube.get_mask()
        side_mask = pygame.mask.from_surface(self.side_img1)
        offset = (round(self.x - cube.x - self.side_img1.get_width()), round(self.y - cube.y))
        point = cube_mask.overlap(side_mask, offset)

        if point:
            return True

        return False
