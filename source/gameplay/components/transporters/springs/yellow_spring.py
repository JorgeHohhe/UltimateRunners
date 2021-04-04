import pygame
from .....graphics.images_loader import YELLOW_SPRING
from ...component_class import Component


class YellowSpring(Component):

    def __init__(self, x, y, angle):
        super().__init__(x, y, angle, YELLOW_SPRING)
        self.activated = False

    def collision(self, player):
        cube_mask = player.get_mask()
        spike_mask = pygame.mask.from_surface(self.img)
        offset = (round(self.x - player.x), round(self.y - player.y))
        point = cube_mask.overlap(spike_mask, offset)

        if point:
            player.change_velocity(-20)

            if player.gamemode == "cube":
                player.rot += 1
                if player.rot == 5:
                    player.rot = 1
                    player.tilt = 0
