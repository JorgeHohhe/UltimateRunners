import pygame
from .....graphics.images_loader import GRAVITY_GLOBE
from ...component_class import Component


class GravityGlobe(Component):

    def __init__(self, x, y, angle):
        super().__init__(x, y, angle, GRAVITY_GLOBE)
        self.activated = False

    def collision(self, player):
        player_mask = player.get_mask()
        spike_mask = pygame.mask.from_surface(self.img)
        offset = (round(self.x - player.x), round(self.y - player.y))
        point = player_mask.overlap(spike_mask, offset)

        state = pygame.key.get_pressed()
        if point and state[pygame.K_SPACE] and not self.activated:
            if player.grav > 0:
                player.change_velocity(-15)
            else:
                player.change_velocity(15)
            player.change_gravity(-player.get_gravity())
            self.activated = True

            if player.gamemode == "cube":
                player.rot += 1
                if player.rot == 5:
                    player.rot = 1
                    player.tilt = 0
