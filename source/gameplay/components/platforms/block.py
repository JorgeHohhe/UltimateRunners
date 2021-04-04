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

class MobileBlock(Block):

    def __init__(self, x, y, angle, pixels_x, pixels_y, y_velocity = 10):
        super().__init__(x, y, angle, pixels_x, pixels_y)
        self.img = pygame.transform.scale(self.img, (pixels_x, pixels_y))
        self.side_img1 = pygame.transform.rotate(SIDE, 90)
        self.side_img1 = pygame.transform.scale(self.side_img1, (20, pixels_y))
        self.upper_img = pygame.transform.rotate(SIDE, 0)
        self.lower_img = pygame.transform.rotate(SIDE, 180)
        self.upper_img = pygame.transform.scale(self.upper_img, (pixels_x, 20))
        self.lower_img = pygame.transform.scale(self.lower_img, (pixels_x, 20))
        self.y_velocity = y_velocity
        self.pixels_y = pixels_y

    def draw(self, win):
        _, max_y = win.get_size()
        if ((self.y + self.y_velocity + self.pixels_y >= max_y - 30) or (self.y + self.y_velocity <= 30)):
            self.y_velocity *= -1
        self.y += self.y_velocity
        win.blit(self.img, (self.x, self.y))
        win.blit(self.upper_img, (self.x, self.y - self.upper_img.get_height()))
        win.blit(self.lower_img, (self.x, self.y+ self.pixels_y))
        win.blit(self.side_img1, (self.x - self.side_img1.get_width(), self.y))

    def collision(self, player):
        player_mask = player.get_mask()
        lower_mask = pygame.mask.from_surface(self.lower_img)
        lower_offset = (round(self.x - player.x), round(self.y - player.y + self.pixels_y))
        lower_point = player_mask.overlap(lower_mask, lower_offset)
        upper_mask = pygame.mask.from_surface(self.upper_img)
        upper_offset = (round(self.x - player.x), round(self.y - player.y - self.upper_img.get_height()))
        upper_point = player_mask.overlap(upper_mask, upper_offset)
        side_mask = pygame.mask.from_surface(self.side_img1)
        offset = (round(self.x - player.x - self.side_img1.get_width()), round(self.y - player.y))
        point = player_mask.overlap(side_mask, offset)

        if lower_point or upper_point or point:
            return True

        return False

class MobilePortal(Block):

    def __init__(self, x, y, angle, pixels_x, pixels_y, y_velocity = 10):
        super().__init__(x, y, angle, pixels_x, pixels_y)
        self.img = pygame.transform.scale(self.img, (pixels_x, pixels_y))
        self.side_img1 = pygame.transform.rotate(SIDE, 90)
        self.side_img1 = pygame.transform.scale(self.side_img1, (20, pixels_y))
        self.upper_img = pygame.transform.rotate(SIDE, 0)
        self.lower_img = pygame.transform.rotate(SIDE, 180)
        self.upper_img = pygame.transform.scale(self.upper_img, (pixels_x, 20))
        self.lower_img = pygame.transform.scale(self.lower_img, (pixels_x, 20))
        self.y_velocity = y_velocity
        self.pixels_y = pixels_y

    def draw(self, win):
        _, max_y = win.get_size()
        if ((self.y + self.y_velocity + self.pixels_y >= max_y - 30) or (self.y + self.y_velocity <= 30)):
            self.y_velocity *= -1
        self.y += self.y_velocity
        win.blit(self.img, (self.x, self.y))
        win.blit(self.upper_img, (self.x, self.y - self.upper_img.get_height()))
        win.blit(self.lower_img, (self.x, self.y+ self.pixels_y))
        win.blit(self.side_img1, (self.x - self.side_img1.get_width(), self.y))
        win.blit(self.img, (self.x, self.y))
        win.blit(self.upper_img, (self.x, self.y - self.upper_img.get_height()))
        win.blit(self.lower_img, (self.x, self.y+ self.pixels_y))
        win.blit(self.side_img1, (self.x - self.side_img1.get_width(), self.y))

    def collision(self, player):
        player_mask = player.get_mask()
        lower_mask = pygame.mask.from_surface(self.lower_img)
        lower_offset = (round(self.x - player.x), round(self.y - player.y + self.pixels_y))
        lower_point = player_mask.overlap(lower_mask, lower_offset)
        upper_mask = pygame.mask.from_surface(self.upper_img)
        upper_offset = (round(self.x - player.x), round(self.y - player.y - self.upper_img.get_height()))
        upper_point = player_mask.overlap(upper_mask, upper_offset)
        side_mask = pygame.mask.from_surface(self.side_img1)
        offset = (round(self.x - player.x - self.side_img1.get_width()), round(self.y - player.y))
        point = player_mask.overlap(side_mask, offset)

        if lower_point or upper_point or point:
            return True

        return False
