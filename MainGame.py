import pygame
import os

pygame.font.init()

VEL = 8

WIN_WIDTH = 800
WIN_HEIGHT = 680
YSPRING = pygame.transform.scale(pygame.image.load(os.path.join("images", "YellowSpring.png")), (75, 5))
CUBE = pygame.transform.scale(pygame.image.load(os.path.join("images", "cube.png")), (75, 75))
BLOCK = pygame.transform.scale(pygame.image.load(os.path.join("images", "block.png")), (75, 75))
SPIKE = pygame.transform.scale(pygame.image.load(os.path.join("images", "spike.png")), (50, 50))
BG = pygame.image.load(os.path.join("images", "bg1.jpg"))
BASE = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "base.png")))
SIDE = pygame.transform.scale(pygame.image.load(os.path.join("images", "SideBlock.png")), (436, 20))
FONT = pygame.font.SysFont("freesansbold.ttf", 50)

# TEST = pygame.transform.scale(pygame.image.load(os.path.join("images", "Wave34.png")), (47, 75))  # Change Scale


class Cube:
    ROTATION_VEL = 3

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick = 0
        self.vel = 0
        self.img = CUBE
        self.rot = 0

    def could_jump(self, blocks):

        if self.y == WIN_HEIGHT - BASE.get_height() - self.img.get_height() + 5:
            return True
        else:
            for block in blocks:
                if self.y == block.y - self.img.get_height():
                    return True

            return False

    def jump(self):

        self.vel = -15
        self.tick = 0

        self.rot += 1
        if self.rot == 5:
            self.rot = 1
            self.tilt = 0

    def jumpYS(self):

        self.vel = -20
        self.tick = 0

        self.rot += 1
        if self.rot == 5:
            self.rot = 1
            self.tilt = 0

    def move(self, blocks):
        # CUBE PHYSICS
        self.vel += 0.8
        self.y += self.vel
        self.tick += 1

        # CUBE AND BASE INTERACTION
        if self.y > WIN_HEIGHT - BASE.get_height() - self.img.get_height() + 5:
            self.y = WIN_HEIGHT - BASE.get_height() - self.img.get_height() + 5
            self.vel = 0

        # CUBE AND BLOCKS INTERACTION
        for block in blocks:
            if self.x + CUBE.get_width() > block.x and self.x < block.x + BLOCK.get_width():
                if self.y + CUBE.get_height() > block.y:
                    self.y = block.y - self.img.get_height()
                    self.vel = 0

        # CUBE ROTATION AFTER JUMP
        if self.tilt > -90 * self.rot:
            self.tilt -= self.ROTATION_VEL

    def draw(self, win):
        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_image.get_rect(center=self.img.get_rect(topleft=(self.x, self.y)).center)
        win.blit(rotated_image, new_rect.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)


class Base:
    WIDTH = BASE.get_width()

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH
        self.img = BASE

    def move(self):
        self.x1 -= VEL
        self.x2 -= VEL

        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH

        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

    def draw(self, win):
        win.blit(self.img, (self.x1, self.y))
        win.blit(self.img, (self.x2, self.y))


class Bg:
    WIDTH = BG.get_width()

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH
        self.img1 = BG
        self.img2 = pygame.transform.flip(BG, True, False)

    def move(self):
        self.x1 -= VEL - 7.5
        self.x2 -= VEL - 7.5

        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH

        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

    def draw(self, win):
        win.blit(self.img1, (self.x1, self.y))
        win.blit(self.img2, (self.x2, self.y))


class Spike:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = SPIKE

    def move(self):
        self.x -= VEL

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))

    def collision(self, cube):
        cube_mask = cube.get_mask()
        spike_mask = pygame.mask.from_surface(self.img)
        offset = (round(self.x - cube.x), round(self.y - cube.y))
        point = cube_mask.overlap(spike_mask, offset)

        if point:
            return True

        return False

class YellowSpring:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = YSPRING

    def move(self):
        self.x -= VEL

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))

    def collision(self, cube):
        cube_mask = cube.get_mask()
        spike_mask = pygame.mask.from_surface(self.img)
        offset = (round(self.x - cube.x), round(self.y - cube.y))
        point = cube_mask.overlap(spike_mask, offset)

        if point:
            return True

        return False


class Block:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = BLOCK
        self.side_img1 = pygame.transform.rotate(SIDE, 90)

    def move(self):
        self.x -= VEL

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


def draw_game(win, cube, background, spikes, blocks, ysprings, base):
    background.draw(win)
    cube.draw(win)
    for spike in spikes:
        spike.draw(win)
    for block in blocks:
        block.draw(win)
    for spring in ysprings:
        spring.draw(win)
    base.draw(win)

    # DRAW TEST
    # win.blit(TEST, (500, 200))

    pygame.display.update()


def main():
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    base = Base(WIN_HEIGHT - BASE.get_height())
    background = Bg(0)
    spikes = [Spike(800, WIN_HEIGHT - BASE.get_height() - SPIKE.get_height())]
    blocks = [Block(1200, WIN_HEIGHT - BASE.get_height() - BLOCK.get_height())]
    ysprings = [YellowSpring(700, WIN_HEIGHT - BASE.get_height() - YSPRING.get_height())]
    cube = Cube(200, 200)

    timer = pygame.time.Clock()
    flag = True
    while flag:
        timer.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False
                pygame.quit()
                quit()
            # JUMP TEST WITH SPACE-BAR
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and cube.could_jump(blocks):
                cube.jump()

        # TEST WHO IS THE NEXT BLOCK
        cube.move(blocks)
        background.move()
        base.move()
        remove_spikes = list()  # LOOK IF IS NECESSARY
        remove_blocks = list()  # LOOK IF IS NECESSARY
        remove_ysprings = list()  # LOOK IF IS NECESSARY

        # SPIKES
        for spike in spikes:
            # SPIKE COLLISION TEST
            if spike.collision(cube):
                # restart the game
                main()
            # SPIKE COLLISION TEST

            if spike.x + spike.img.get_width() < 0:
                remove_spikes.append(spike)

            spike.move()
        # BLOCKS
        for block in blocks:
            # BLOCK COLLISION TEST
            if block.collision(cube):
                # restart the game
                main()
            # BLOCK COLLISION TEST

            if block.x + block.img.get_width() < 0:
                remove_blocks.append(block)

            block.move()

        for spring in ysprings:
            # SPRING COLLISION TEST
            if spring.collision(cube):
                # restart the game
                cube.jumpYS()
            # BLOCK COLLISION TEST

            if block.x + block.img.get_width() < 0:
                remove_ysprings.append(ysprings)

            spring.move()

        # MAP SETUP
        while (len(spikes) + len(blocks)) <= 1:
            blocks.append(Block(900, WIN_HEIGHT - BASE.get_height() - BLOCK.get_height()))
            blocks.append(Block(1150, WIN_HEIGHT - BASE.get_height() - BLOCK.get_height()))
            blocks.append(Block(1150, WIN_HEIGHT - BASE.get_height() - BLOCK.get_height() - 75))
            ysprings.append(YellowSpring(800, WIN_HEIGHT - BASE.get_height() - YSPRING.get_height()))

        # REMOVE OBJECTS THAT ALREADY PASSED
        for r in remove_spikes:
            spikes.remove(r)
        for r in remove_blocks:
            blocks.remove(r)
        for r in remove_ysprings:
            ysprings.remove(r)

        draw_game(win, cube, background, spikes, blocks, ysprings, base)


if __name__ == '__main__':
    main()