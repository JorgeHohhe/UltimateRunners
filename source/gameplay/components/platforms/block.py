import pygame
from ....graphics.images_loader import BLOCK, SIDE
from ..component_class import Component


class Block(Component):

    def __init__(self, x, y, angle, pixels_x, pixels_y):
        super().__init__(x, y, angle, BLOCK)
        self.img = pygame.transform.scale(self.img, (pixels_x, pixels_y))
        self.side_img1 = pygame.transform.rotate(SIDE, 90)
        self.side_img1 = pygame.transform.scale(self.side_img1, (20, pixels_y))

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))
        win.blit(self.side_img1, (self.x - self.side_img1.get_width(), self.y))

    def collision(self, player):
        player_mask = player.get_mask()
        side_mask = pygame.mask.from_surface(self.side_img1)
        offset = (round(self.x - player.x - self.side_img1.get_width()), round(self.y - player.y))
        point = player_mask.overlap(side_mask, offset)

        if point:
            return True

        return False

    def interaction(self, player):
        player_mask = player.get_mask()
        block_mask = pygame.mask.from_surface(self.img)
        offset = (round(self.x - player.x), round(self.y - player.y))
        point = player_mask.overlap(block_mask, offset)

        if point:
            player.vel = 0
            if player.gamemode == 'laser':
                player.rot = -90
                if player.y < self.y:
                    player.y = self.y - player.height * 3 / 4
                else:
                    player.y = self.y + self.img.get_height() * 3 / 4
            else:
                if player.y < self.y:
                    player.y = self.y - player.height
                else:
                    player.y = self.y + self.img.get_height()
                    if player.gamemode == "cyclops":
                        player.y -= 8
            return True

        return False
