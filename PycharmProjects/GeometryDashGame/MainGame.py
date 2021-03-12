import pygame
import os

# pygame.font.init()

VEL = 8
INITIAL_X = 150

CUBE = pygame.transform.scale(pygame.image.load(os.path.join("images", "cube.png")), (75, 75))
CUBE_PORTAL = pygame.transform.scale(pygame.image.load(os.path.join("images", "CubePortal.png")), (81, 150))
LASER = pygame.transform.scale(pygame.image.load(os.path.join("images", "Laser.png")), (47, 75))
LASER_BACK = pygame.transform.scale(pygame.image.load(os.path.join("images", "LaserBack.png")), (10, 10))
LASER_PORTAL = pygame.transform.scale(pygame.image.load(os.path.join("images", "LaserPortal.png")), (81, 150))
ORB = pygame.transform.scale(pygame.image.load(os.path.join("images", "Orb.png")), (75, 75))
ORB_PORTAL = pygame.transform.scale(pygame.image.load(os.path.join("images", "OrbPortal.png")), (81, 150))
DRAGON = pygame.transform.scale(pygame.image.load(os.path.join("images", "Dragon.png")), (125, 72))
DRAGON_PORTAL = pygame.transform.scale(pygame.image.load(os.path.join("images", "DragonPortal.png")), (81, 150))
CYCLOPS_FRAME_0 = pygame.transform.scale(pygame.image.load(os.path.join("images", "CyclopsFrame0.png")), (120, 75))
CYCLOPS_FRAME_1 = pygame.transform.scale(pygame.image.load(os.path.join("images", "CyclopsFrame1.png")), (120, 75))
CYCLOPS_FRAME_2 = pygame.transform.scale(pygame.image.load(os.path.join("images", "CyclopsFrame2.png")), (120, 75))
CYCLOPS_FRAME_3 = pygame.transform.scale(pygame.image.load(os.path.join("images", "CyclopsFrame3.png")), (120, 75))
CYCLOPS_FRAME_4 = pygame.transform.scale(pygame.image.load(os.path.join("images", "CyclopsFrame4.png")), (120, 75))
CYCLOPS_FRAME_5 = pygame.transform.scale(pygame.image.load(os.path.join("images", "CyclopsFrame5.png")), (120, 75))
CYCLOPS_FRAME_6 = pygame.transform.scale(pygame.image.load(os.path.join("images", "CyclopsFrame6.png")), (120, 75))
CYCLOPS_PORTAL = pygame.transform.scale(pygame.image.load(os.path.join("images", "CyclopsPortal.png")), (81, 150))

BG = pygame.image.load(os.path.join("images", "bg1.jpg"))
BASE = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "base.png")))
SIDE = pygame.transform.scale(pygame.image.load(os.path.join("images", "SideBlock.png")), (436, 20))
# FONT = pygame.font.SysFont("freesansbold.ttf", 50)

WIN_WIDTH = 800
WIN_HEIGHT = 680
PORTAL_HEIGHT = CUBE_PORTAL.get_height()


class Cube:
    ROTATION_VEL = 3
    HEIGHT = CUBE.get_height()

    def __init__(self, y):
        self.x = INITIAL_X
        self.y = y
        self.tilt = 0
        self.vel = 0
        self.img = CUBE
        self.rot = 0

    def could_jump(self, blocks):

        if self.y == WIN_HEIGHT - BASE.get_height() - self.HEIGHT + 5:
            return True
        else:
            for block in blocks:
                if self.y == block.y - self.HEIGHT + 5:
                    return True

            return False

    def jump(self):

        self.vel = -15
        self.y += self.vel

        self.rot += 1
        if self.rot == 5:
            self.rot = 1
            self.tilt = 0

    def move(self, blocks):
        # CUBE PHYSICS
        self.vel += 0.8
        self.y += self.vel

        # CUBE AND BASE INTERACTION
        if self.y > WIN_HEIGHT - BASE.get_height() - self.HEIGHT + 5:
            self.y = WIN_HEIGHT - BASE.get_height() - self.HEIGHT + 5
            self.vel = 0

        # CUBE AND BLOCKS INTERACTION
        for block in blocks:
            if self.x + CUBE.get_width() > block.x and self.x < block.x + block.img.get_width():
                if self.y > block.y - self.HEIGHT + 5:
                    self.y = block.y - self.HEIGHT + 5
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


class Laser:
    HEIGHT = LASER.get_height()

    def __init__(self, y):
        self.x = INITIAL_X
        self.y = y
        self.vel = 0
        self.img = LASER
        self.img_back = LASER_BACK
        self.rot = 0
        self.locals = list()

    def up(self):

        self.vel = -10
        self.rot = -45

    def down(self):

        self.vel = 10
        self.rot = -135

    def move(self):
        # LASER PHYSICS
        self.y += self.vel

        # LASER AND BASE INTERACTION
        if self.y > WIN_HEIGHT - BASE.get_height() - self.HEIGHT * 3 / 4:
            self.y = WIN_HEIGHT - BASE.get_height() - self.HEIGHT * 3 / 4
            self.vel = 0
            self.rot = -90
        elif self.y < BASE.get_height() - self.HEIGHT * 3 / 4:
            self.y = BASE.get_height() - self.HEIGHT * 3 / 4
            self.vel = 0
            self.rot = -90

    def draw(self, win):
        rotated_image = pygame.transform.rotate(self.img, self.rot)
        new_rect = rotated_image.get_rect(center=self.img.get_rect(topleft=(self.x, self.y)).center)
        win.blit(rotated_image, new_rect.topleft)

        self.locals.append([self.x + 12, self.y + self.HEIGHT / 2 - self.img_back.get_height() / 2])
        for local in self.locals:
            local[0] -= VEL
            win.blit(self.img_back, local)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)


class Orb:
    ROTATION_VEL = 6
    HEIGHT = ORB.get_height()

    def __init__(self, y):
        self.x = INITIAL_X
        self.y = y
        self.gravity = 1
        self.vel = 0
        self.img = pygame.transform.flip(ORB, True, False)
        self.rot = 0

    def could_switch(self):

        if self.y == WIN_HEIGHT - BASE.get_height() - self.HEIGHT:
            return True
        elif self.y == - BASE.get_height() / 2 + self.HEIGHT * 3 / 4:
            return True

        return False

    def switch(self):
        self.gravity *= -1

    def move(self):
        # ORB PHYSICS
        self.vel += 0.6 * self.gravity
        self.y += self.vel

        # ORB AND BASES INTERACTIONS
        if self.y > WIN_HEIGHT - BASE.get_height() - self.HEIGHT:
            self.y = WIN_HEIGHT - BASE.get_height() - self.HEIGHT
            self.vel = 0
        elif self.y < - BASE.get_height() / 2 + self.HEIGHT * 3 / 4:
            self.y = - BASE.get_height() / 2 + self.HEIGHT * 3 / 4
            self.vel = 0

        # ORB ROTATION
        self.rot -= self.ROTATION_VEL * self.gravity

    def draw(self, win):
        rotated_image = pygame.transform.rotate(self.img, self.rot)
        new_rect = rotated_image.get_rect(center=self.img.get_rect(topleft=(self.x, self.y)).center)
        win.blit(rotated_image, new_rect.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)


class Dragon:
    ROTATION_VEL = 3
    MAX_VEL = 6
    HEIGHT = DRAGON.get_height()

    def __init__(self, y):
        self.x = INITIAL_X
        self.y = y
        self.vel = 0
        self.img = DRAGON
        self.rot = 0

    def up(self):
        self.vel += -0.4
        self.y += self.vel

    def move(self):
        # DRAGON PHYSICS
        self.vel += 0.2
        self.y += self.vel

        # MAX VEL
        if self.vel > self.MAX_VEL:
            self.vel = self.MAX_VEL

        # DRAGON AND BASE INTERACTION
        if self.y > WIN_HEIGHT - BASE.get_height() - self.HEIGHT:
            self.y = WIN_HEIGHT - BASE.get_height() - self.HEIGHT
            self.vel = 0
            self.rot = 0
        elif self.y < - BASE.get_height() / 2 + self.HEIGHT * 3 / 4:
            self.y = - BASE.get_height() / 2 + self.HEIGHT * 3 / 4
            self.vel = 0
            self.rot = 0

        # DRAGON ROTATION
        self.rot = - self.ROTATION_VEL * self.vel

    def draw(self, win):
        rotated_image = pygame.transform.rotate(self.img, self.rot)
        new_rect = rotated_image.get_rect(center=self.img.get_rect(topleft=(self.x, self.y)).center)
        win.blit(rotated_image, new_rect.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)


class Cyclops:
    HEIGHT = CYCLOPS_FRAME_0.get_height()

    def __init__(self, y):
        self.x = INITIAL_X
        self.y = y
        self.gravity = 30
        self.vel = 0
        self.img = [CYCLOPS_FRAME_0, CYCLOPS_FRAME_1, CYCLOPS_FRAME_2, CYCLOPS_FRAME_3, CYCLOPS_FRAME_4, CYCLOPS_FRAME_5, CYCLOPS_FRAME_6]
        self.rot = 0
        self.flip = False

    def could_switch(self):

        if self.y == WIN_HEIGHT - BASE.get_height() - self.HEIGHT:
            return True
        elif self.y == - BASE.get_height() / 2 + self.HEIGHT * 3 / 4:
            return True

        return False

    def switch(self):
        self.gravity *= -1
        self.flip = not self.flip

    def move(self):
        # CYCLOPS PHYSICS
        self.vel += 0.6 * self.gravity
        self.y += self.vel

        # CYCLOPS AND BASES INTERACTIONS
        if self.y > WIN_HEIGHT - BASE.get_height() - self.HEIGHT:
            self.y = WIN_HEIGHT - BASE.get_height() - self.HEIGHT
            self.vel = 0
        elif self.y < - BASE.get_height() / 2 + self.HEIGHT * 3 / 4:
            self.y = - BASE.get_height() / 2 + self.HEIGHT * 3 / 4
            self.vel = 0

        # CYCLOPS ANIMATION WHILE WALK
        self.rot += 0.5
        if self.rot == 7:
            self.rot = 0

    def draw(self, win):
        rotated_image = pygame.transform.flip(self.img[int(self.rot)], False, self.flip)
        new_rect = rotated_image.get_rect(center=self.img[int(self.rot)].get_rect(topleft=(self.x, self.y)).center)
        win.blit(rotated_image, new_rect.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.img[0])


class LaserPortal:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = LASER_PORTAL
        self.passed = False

    def move(self):
        self.x -= VEL

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))


class CubePortal:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = CUBE_PORTAL
        self.passed = False

    def move(self):
        self.x -= VEL

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))


class OrbPortal:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = ORB_PORTAL
        self.passed = False

    def move(self):
        self.x -= VEL

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))


class DragonPortal:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = DRAGON_PORTAL
        self.passed = False

    def move(self):
        self.x -= VEL

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))


class CyclopsPortal:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = CYCLOPS_PORTAL
        self.passed = False

    def move(self):
        self.x -= VEL

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))


class Base:
    WIDTH = BASE.get_width()
    HEIGHT = BASE.get_height()

    def __init__(self):
        self.y_bottom = WIN_HEIGHT - self.HEIGHT
        self.y_top = - self.HEIGHT / 2
        self.x1 = 0
        self.x2 = self.WIDTH
        self.img_bottom = BASE
        self.img_top = pygame.transform.flip(BASE, False, True)

    def move(self):
        self.x1 -= VEL
        self.x2 -= VEL

        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH

        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

    def draw(self, win):
        win.blit(self.img_bottom, (self.x1, self.y_bottom))
        win.blit(self.img_bottom, (self.x2, self.y_bottom))
        win.blit(self.img_top, (self.x1, self.y_top))
        win.blit(self.img_top, (self.x2, self.y_top))


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

    def __init__(self, x, y, pixels_x, pixels_y):
        self.x = x
        self.y = y
        self.img = pygame.transform.scale(pygame.image.load(os.path.join("images", "spike.png")), (pixels_x, pixels_y))

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

    def __init__(self, x, y, pixels_x, pixels_y):
        self.x = x
        self.y = y
        self.img = pygame.transform.scale(pygame.image.load(os.path.join("images", "block.png")), (pixels_x, pixels_y))
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


def draw_game(win, cube, laser, orb, dragon, cyclops, portals, background, components, base, gamemode):
    background.draw(win)

    if gamemode == "cube":
        cube.draw(win)
    elif gamemode == "laser":
        laser.draw(win)
    elif gamemode == "orb":
        orb.draw(win)
    elif gamemode == "dragon":
        dragon.draw(win)
    elif gamemode == "cyclops":
        cyclops.draw(win)

    for comp in components.values():
        for i in range(0, len(comp)):
            comp[i].draw(win)

    base.draw(win)

    for portal in portals.values():
        for i in range(0, len(portal)):
            portal[i].draw(win)

    pygame.display.update()


def main():
    """ =-=-=-=-=-=-= MAP SETUP =-=-=-=-=-=-= """
    # PREPARATION
    spikes = []
    blocks = []
    laser_portal = []
    cube_portal = []
    orb_portal = []
    dragon_portal = []
    cyclops_portal = []

    # READING THE LEVEL SETUP IN A TXT FILE
    input_file = open(r"Map1.txt", "r")
    f = input_file.readline().split()
    gamemode = f[0]

    f = input_file.readline().split()
    while f[0] != "end":
        if f[0] == "spike":
            f[2] = WIN_HEIGHT - BASE.get_height() - int(f[4]) - int(f[2])
            spikes.append(Spike(int(f[1]), f[2], int(f[3]), int(f[4])))
        elif f[0] == "block":
            f[2] = WIN_HEIGHT - BASE.get_height() - int(f[4]) - int(f[2])
            blocks.append(Block(int(f[1]), f[2], int(f[3]), int(f[4])))
        elif f[0] == "laserportal":
            f[2] = WIN_HEIGHT - BASE.get_height() - PORTAL_HEIGHT - int(f[2])
            laser_portal.append(LaserPortal(int(f[1]), f[2]))
        elif f[0] == "cubeportal":
            f[2] = WIN_HEIGHT - BASE.get_height() - PORTAL_HEIGHT - int(f[2])
            cube_portal.append(CubePortal(int(f[1]), f[2]))
        elif f[0] == "orbportal":
            f[2] = WIN_HEIGHT - BASE.get_height() - PORTAL_HEIGHT - int(f[2])
            orb_portal.append(OrbPortal(int(f[1]), f[2]))
        elif f[0] == "dragonportal":
            f[2] = WIN_HEIGHT - BASE.get_height() - PORTAL_HEIGHT - int(f[2])
            dragon_portal.append(DragonPortal(int(f[1]), f[2]))
        elif f[0] == "cyclopsportal":
            f[2] = WIN_HEIGHT - BASE.get_height() - PORTAL_HEIGHT - int(f[2])
            cyclops_portal.append(CyclopsPortal(int(f[1]), f[2]))

        f = input_file.readline().split()

    input_file.close()
    # SET WINDOW, BASE AND BACKGROUND
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    base = Base()
    background = Bg(0)

    # SET COMPONENTS
    components = {
        "spikes": spikes,
        "blocks": blocks
    }

    # SET PORTALS
    portals = {
        "laser_portal": laser_portal,
        "cube_portal": cube_portal,
        "orb_portal": orb_portal,
        "dragon_portal": dragon_portal,
        "cyclops_portal": cyclops_portal
    }

    # SET GAMEMODES
    cube = Cube(0)
    laser = Laser(0)
    orb = Orb(0)
    dragon = Dragon(0)
    cyclops = Cyclops(0)
    if gamemode == "cube":
        cube = Cube(500)
    elif gamemode == "laser":
        laser = Laser(500)
    elif gamemode == "orb":
        orb = Orb(500)
    elif gamemode == "dragon":
        dragon = Dragon(500)
    elif gamemode == "cyclops":
        cyclops = Cyclops(500)

    player_height = 0
    pressed = False

    """ =-=-=-=-=-=-= GAME START =-=-=-=-=-=-= """
    timer = pygame.time.Clock()
    flag = True
    while flag:
        timer.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False
                pygame.quit()
                quit()

        # TEST SPACE-BAR FOR THE DIFFERENT GAMEMODES
        state = pygame.key.get_pressed()
        if state[pygame.K_SPACE]:
            if gamemode == "cube":
                if cube.could_jump(blocks):
                    cube.jump()
            elif gamemode == "dragon":
                dragon.up()

            if not pressed:
                pressed = True
                if gamemode == "laser":
                    laser.up()
                elif gamemode == "orb":
                    if orb.could_switch():
                        orb.switch()
                elif gamemode == "cyclops":
                    if cyclops.could_switch():
                        cyclops.switch()
        else:
            pressed = False
            if gamemode == "laser":
                laser.down()

        # TEST GAMEMODE AND MOVE
        if gamemode == "cube":
            cube.move(blocks)
            player_height = cube.y
        elif gamemode == "laser":
            laser.move()
            player_height = laser.y
        elif gamemode == "orb":
            orb.move()
            player_height = orb.y
        elif gamemode == "dragon":
            dragon.move()
            player_height = dragon.y
        elif gamemode == "cyclops":
            cyclops.move()
            player_height = cyclops.y

        # MOVE THE MAP
        background.move()
        base.move()
        for portal in portals.values():
            for i in range(0, len(portal)):
                portal[i].move()

        remove_spikes = list()  # LOOK IF IS NECESSARY
        remove_blocks = list()  # LOOK IF IS NECESSARY
        # SPIKES
        for spike in components["spikes"]:
            # SPIKE COLLISION TEST
            if spike.collision(cube):
                # restart the game
                main()

            if spike.x + spike.img.get_width() < 0:
                remove_spikes.append(spike)

            spike.move()
        # BLOCKS
        for block in components["blocks"]:
            # BLOCK COLLISION TEST
            if block.collision(cube):
                # restart the game
                main()
            # BLOCK COLLISION TEST

            if block.x + block.img.get_width() < 0:
                remove_blocks.append(block)

            block.move()

        # PORTALS TEST
        for key, portal in portals.items():
            for i in range(0, len(portal)):
                if portal[i].x < INITIAL_X and not portal[i].passed:
                    portal[i].passed = True
                    if key == "laser_portal":
                        cube = Cube(0)
                        laser = Laser(player_height)
                        orb = Orb(0)
                        dragon = Dragon(0)
                        cyclops = Cyclops(0)
                        gamemode = "laser"
                    elif key == "cube_portal":
                        cube = Cube(player_height)
                        laser = Laser(0)
                        orb = Orb(0)
                        dragon = Dragon(0)
                        cyclops = Cyclops(0)
                        gamemode = "cube"
                    elif key == "orb_portal":
                        cube = Cube(0)
                        laser = Laser(0)
                        orb = Orb(player_height)
                        dragon = Dragon(0)
                        cyclops = Cyclops(0)
                        gamemode = "orb"
                    elif key == "dragon_portal":
                        cube = Cube(0)
                        laser = Laser(0)
                        orb = Orb(0)
                        dragon = Dragon(player_height)
                        cyclops = Cyclops(0)
                        gamemode = "dragon"
                    elif key == "cyclops_portal":
                        cube = Cube(0)
                        laser = Laser(0)
                        orb = Orb(0)
                        dragon = Dragon(0)
                        cyclops = Cyclops(player_height)
                        gamemode = "cyclops"

        # REMOVE OBJECTS THAT ALREADY PASSED
        for r in remove_spikes:
            components["spikes"].remove(r)
        for r in remove_blocks:
            components["blocks"].remove(r)

        draw_game(win, cube, laser, orb, dragon, cyclops, portals, background, components, base, gamemode)


if __name__ == '__main__':
    main()
