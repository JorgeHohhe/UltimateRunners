import pygame
from source.graphics.misc.font import *
from source.gameplay.utils.constants import *
from source.gameplay.components.platforms.block import *
from source.gameplay.essentials.checkinputs import *
from source.gameplay.essentials.menu import MainMenu
from source.gameplay.essentials.environment import Environment
import source.audio.audio_loader as al
from time import sleep

# SET PROGRESS BAR PARAMS
    
barPos      = (200, 50)
barSize     = (600, 20)
borderColor = (255, 255, 255)
barColor    = (0, 128, 0)
# COUNT DEATHS

NUMBER_OF_DEATHS = [0]

def draw_progress_bar(screen, pos, size, borderC, barC, progress):

    pygame.draw.rect(screen, borderC, (*pos, *size), 1)
    innerPos  = (pos[0]+3, pos[1]+3)
    innerSize = ((size[0]-6) * progress, size[1]-6)
    pygame.draw.rect(screen, barC, (*innerPos, *innerSize))


def draw_game(win, player, portals, background, components, base, dead, progress, death_count, NUMBER_OF_DEATHS):

    background.draw(win)

    if dead == 0:
        player.draw(win)

    for comp in components.values():
        for i in range(0, len(comp)):
            if comp[i].x < WIN_WIDTH:
                comp[i].draw(win)

    base.draw(win)

    for portal in portals.values():
        for i in range(0, len(portal)):
            portal[i].draw(win)

    if dead != 0:
        player.death_effect(win)
        NUMBER_OF_DEATHS[0] += 1
    draw_progress_bar(win, barPos, barSize, borderColor, barColor, progress)

    win.blit(death_count,(20,50)) # (x, y)
    pygame.display.update()



def main():
    """ =-=-=-=-=-=-= Main Menu =-=-=-=-=-=-= """
    ######
    inputs = Inputs()
    ######

    """ =-=-=-=-=-=-= MAP SETUP =-=-=-=-=-=-= """

    # SET WINDOW
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    # PREPARATION
    timer = pygame.time.Clock()
    death_loop = 0
    game_paused = False

    # MENU MUSIC
    level_selected = 4
    al.play_music_map(level_selected)
    
    # Font
    pygame.font.init() # you have to call this at the start, 
                       # if you want to use this module.
    myfont = pygame.font.SysFont('Roboto', 35)
    """ =-=-=-=-=-=-= GAME START =-=-=-=-=-=-= """
    flag = True
    while inputs.running:
      inputs.curr_menu.display_menu()
      level_selected = inputs.curr_menu.chooselvl
      env = Environment(level_selected)
      # LEVEL MUSIC
      al.play_music_map(level_selected)
      while flag & inputs.playing:
        #env = Environment(level_selected)
        timer.tick(60)
        ######
        inputs.check_events()
        if inputs.ESCAPE:
            inputs.playing = False
        ######
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_paused = not game_paused


        if not game_paused:
            # END OF LEVEL
            if env.FIM < env.player.x:
                inputs.curr_menu = inputs.endscreen
                inputs.curr_menu.display_menu()
                main()
                # do something

            # TEST SPACE-BAR FOR THE DIFFERENT GAMEMODES
            state = pygame.key.get_pressed()
            if state[pygame.K_SPACE]:
                if env.player.gamemode == "cube":
                    if env.player.could_jump(env.blocks):
                        env.player.jump()
                elif env.player.gamemode == "dragon":
                    env.player.up()
                elif env.player.gamemode == "laser":
                    env.player.up()
                elif env.player.gamemode == "orb":
                    if env.player.could_switch(env.blocks):
                        env.player.switch()

                if not env.player.pressed_space:
                    env.player.pressed_space = True
                    if env.player.gamemode == "cyclops":
                        if env.player.could_switch(env.blocks):
                            env.player.switch()
            else:
                env.player.pressed_space = False
                if env.player.gamemode == "laser":
                    env.player.down()

            # MOVE THE PLAYER
            env.player.move()
            env.FIM -= VEL

            # MOVE THE MAP
            env.background.move()
            env.base.move()
            for portal in env.portals.values():
                for i in range(0, len(portal)):
                    portal[i].move()

            remove_spikes = list()  # LOOK IF IS NECESSARY
            remove_blocks = list()  # LOOK IF IS NECESSARY

            # SPIKES
            for spike in env.components["all_comp"]:
                if spike.x < WIN_WIDTH:
                    # SPIKE COLLISION TEST
                    if spike.collision(env.player):
                        # restart the game
                        death_loop += 1
                        game_paused = True
                        pass

                    if spike.x + spike.img.get_width() < 0:
                        remove_spikes.append(spike)

                spike.move()

            # BLOCKS
            for block in env.components["blocks"]:
                if block.x < WIN_WIDTH:
                    # BLOCK COLLISION TEST
                    block.interaction(env.player)
                    if block.collision(env.player):
                        # restart the game
                        death_loop += 1
                        game_paused = True
                        pass

                    if block.x + block.img.get_width() < 0:
                        remove_blocks.append(block)

                block.move()

            # PORTALS TEST
            env.portals_test()

            # REMOVE OBJECTS THAT ALREADY PASSED
            for r in remove_spikes:
                env.components["all_comp"].remove(r)
            for r in remove_blocks:
                env.components["blocks"].remove(r)

            # DRAW THE GAME WINDOW
            progress =  1-env.FIM/env.MAP_LENGTH
            death_count = myfont.render('DEATHS : {0}'.format(int(NUMBER_OF_DEATHS[0]/7)), False, (255, 255, 255))
            draw_game(win, env.player, env.portals, env.background, env.components, env.base, death_loop, progress, death_count, NUMBER_OF_DEATHS)
            flag = True
        else:
            if death_loop == 0:
                al.pause_menu()
                game_paused = not game_paused
            else:
                draw_game(win, env.player, env.portals, env.background, env.components, env.base, death_loop, progress, death_count, NUMBER_OF_DEATHS)
                if death_loop == 1:
                    al.death_sound()
                death_loop += 1
                if death_loop > 6:
                    # sleep(0.5)
                    main()

#########
        pygame.display.update()
        inputs.reset_keys()
#########
      


if __name__ == '__main__':
    main()
