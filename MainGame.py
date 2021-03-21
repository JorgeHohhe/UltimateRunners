import pygame
import os
from source.graphics.images_loader import *
from source.graphics.misc.font import *
from source.gameplay.utils.constants import *
from source.gameplay.components.platforms import block
from source.gameplay.components.platforms import mobile
from source.gameplay.essentials.environment import Environment

# TEST = pygame.transform.scale(pygame.image.load(os.path.join("images", "Wave34.png")), (47, 75))  # Change Scale


def draw_game(win, cube, background, spikes, blocks, mobiles, base, top):
    background.draw(win)
    cube.draw(win)
    for spike in spikes:
        spike.draw(win)
    for block in blocks:
        block.draw(win)
    for mobile in mobiles:
        mobile.draw(win)
    base.draw(win)

    # DRAW TEST
    # win.blit(TEST, (500, 200))

    pygame.display.update()


def main():
    env = Environment()
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
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
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and env.cube.could_jump(env.blocks):
                env.cube.jump()

        # TEST WHO IS THE NEXT BLOCK
        env.cube.move(env.blocks)
        env.cube.move(env.mobiles)
        env.background.move()
        env.base.move()
        remove_spikes = list()  # LOOK IF IS NECESSARY
        remove_blocks = list()  # LOOK IF IS NECESSARY
        remove_mobiles = list()  # LOOK IF IS NECESSARY
        # SPIKES
        for spike in env.spikes:
            # SPIKE COLLISION TEST
            if spike.collision(env.cube):
                # restart the game
                main()
            # SPIKE COLLISION TEST

            if spike.x + spike.img.get_width() < 0:
                remove_spikes.append(spike)

            spike.move()
        # BLOCKS
        for block in env.blocks:
            # BLOCK COLLISION TEST
            if block.collision(env.cube):
                # restart the game
                main()
            # BLOCK COLLISION TEST

            if block.x + block.img.get_width() < 0:
                remove_blocks.append(block)

            block.move()
        
        # MOBILES 
        for mobile in env.mobiles:
            # MOBILE COLLISION TEST
            if mobile.collision(env.cube):
                # restart the game
                main()
            # MOBILE COLLISION TEST

            if (mobile.x + mobile.img.get_width() < 0):
                remove_mobiles.append(mobile)

            mobile.move()

        # MAP SETUP
        while (len(env.spikes) + len(env.blocks) + len(env.mobiles)) <= 1:
            env.map_setup()

        # REMOVE OBJECTS THAT ALREADY PASSED
        for r in remove_spikes:
            env.spikes.remove(r)
        for r in remove_blocks:
            env.blocks.remove(r)
        for r in remove_mobiles:
            env.mobiles.remove(r)

        draw_game(win, env.cube, env.background, env.spikes, env.blocks, env.mobiles, env.base, env.top)


if __name__ == '__main__':
    main()
