import pygame
from .....graphics.images_loader import YELLOW_GLOBE
from ...component_class import Component


class YellowGlobe(Component):

    def __init__(self, x, y, angle):
        super().__init__(x, y, angle, YELLOW_GLOBE)
        self.activated = False

    def collision(self, player):
        state = pygame.key.get_pressed()
        cube_mask = player.get_mask()
        spike_mask = pygame.mask.from_surface(self.img)
        offset = (round(self.x - player.x), round(self.y - player.y))
        point = cube_mask.overlap(spike_mask, offset)

        if point and state[pygame.K_SPACE]:
            player.change_velocity(-15)

            if player.gamemode == "cube":
                player.rot += 1
                if player.rot == 5:
                    player.rot = 1
                    player.tilt = 0
