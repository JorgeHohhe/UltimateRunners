import pygame
from ....graphics.images_loader import MOBILE_RECTANGLE, SIDE
from ..component_class import component

class Mobile(component):

    def __init__(self, x, y, angle, omega = 1/60):
        self.x = x
        self.y = y
        self.angle = angle
        self.omega = omega
        self.img = MOBILE_RECTANGLE
        self.img_rect = self.img.get_rect()
        self.time = 0
        self.side_img1 = SIDE
        self.side_img1_rect = self.side_img1.get_rect()

    def rot_center(self, img, original_img, rect, angle):
        img = pygame.transform.rotate(original_img, angle)
        x, y = rect.center  # Save its current center.
        rect = img.get_rect()  # Replace old rect with new rect.
        rect.center = (x, y) 
        return None
    def draw(self, win):
        self.time += 1
        self.angle += self.time * self.omega

        self.img = pygame.transform.rotate(MOBILE_RECTANGLE, self.angle)
        x, y = self.img_rect.center  # Save its current center.
        self.img_rect = self.img.get_rect()  # Replace old rect with new rect.
        self.img_rect.center = (x, y) 

        self.side_img1 = pygame.transform.rotate(SIDE, 90 + self.angle)        
        self.side_img1_rect = self.side_img1.get_rect()  # Replace old rect with new rect.
        self.side_img1_rect.center = (x, y) 

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
