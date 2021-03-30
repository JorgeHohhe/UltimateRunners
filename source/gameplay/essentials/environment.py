from ..components.transporters.springs.gravity_spring import GravSpring
from ..components.transporters.springs.yellow_spring import YellowSpring
from ..components.transporters.globes.yellow_globe import YellowGlobe
from ..components.platforms.block import Block
from ..components.hazards.spike import Spike
from ..components.hazards.lava import Lava
from ..components.portals.portal import Portal
from ..characters.cube import Cube
from ..characters.laser import Laser
from ..characters.orb import Orb
from ..characters.dragon import Dragon
from ..characters.cyclops import Cyclops
from .base import Base
from .background import Bg
from ..utils.constants import *
from ...graphics.images_loader import BASE, GRAV_SPRING, YELLOW_SPRING, YELLOW_GLOBE


class Environment:
    
    def __init__(self):
        """ =-=-=-=-=-=-= MAP SETUP =-=-=-=-=-=-= """
        # PREPARATION
        all_comp = []
        self.blocks = []
        laser_portal = []
        cube_portal = []
        orb_portal = []
        dragon_portal = []
        cyclops_portal = []

        # READING THE LEVEL SETUP IN A TXT FILE
        input_file = open(r"Map3.txt", "r")
        f = input_file.readline().split()
        gamemode = f[0]

        f = input_file.readline().split()
        while f[0] != "end":
            if f[0] == "spike":
                f[2] = WIN_HEIGHT - BASE.get_height() - int(f[4]) - int(f[2])
                all_comp.append(Spike(int(f[1]), f[2], int(f[5]), int(f[3]), int(f[4])))
            elif f[0] == "block":
                f[2] = WIN_HEIGHT - BASE.get_height() - int(f[4]) - int(f[2])
                self.blocks.append(Block(int(f[1]), f[2], 0, int(f[3]), int(f[4])))
            elif f[0] == "yellowspring":
                f[2] = WIN_HEIGHT - BASE.get_height() - YELLOW_SPRING.get_height() - int(f[2])
                all_comp.append(YellowSpring(int(f[1]), f[2], int(f[3])))
            elif f[0] == "yellowglobe":
                f[2] = WIN_HEIGHT - BASE.get_height() - YELLOW_GLOBE.get_height() - int(f[2])
                all_comp.append(YellowGlobe(int(f[1]), f[2], 0))
            elif f[0] == "gravspring":
                f[2] = WIN_HEIGHT - BASE.get_height() - GRAV_SPRING.get_height() - int(f[2])
                all_comp.append(GravSpring(int(f[1]), f[2], int(f[3])))
            elif f[0] == "lava":
                f[2] = WIN_HEIGHT - BASE.get_height() - int(f[4]) - int(f[2])
                all_comp.append(Lava(int(f[1]), f[2], int(f[5]), int(f[3]), int(f[4])))
            elif f[0] == "laserportal":
                f[2] = WIN_HEIGHT - BASE.get_height() - PORTAL_HEIGHT - int(f[2])
                laser_portal.append(Portal(int(f[1]), f[2], 0, 1))
            elif f[0] == "cubeportal":
                f[2] = WIN_HEIGHT - BASE.get_height() - PORTAL_HEIGHT - int(f[2])
                cube_portal.append(Portal(int(f[1]), f[2], 0, 0))
            elif f[0] == "orbportal":
                f[2] = WIN_HEIGHT - BASE.get_height() - PORTAL_HEIGHT - int(f[2])
                orb_portal.append(Portal(int(f[1]), f[2], 0, 2))
            elif f[0] == "dragonportal":
                f[2] = WIN_HEIGHT - BASE.get_height() - PORTAL_HEIGHT - int(f[2])
                dragon_portal.append(Portal(int(f[1]), f[2], 0, 3))
            elif f[0] == "cyclopsportal":
                f[2] = WIN_HEIGHT - BASE.get_height() - PORTAL_HEIGHT - int(f[2])
                cyclops_portal.append(Portal(int(f[1]), f[2], 0, 4))

            f = input_file.readline().split()

        self.FIM = int(f[1])
        input_file.close()

        '''self.base = Base(WIN_HEIGHT - BASE.get_height())
        self.top = Base(BASE.get_height())
        self.background = Bg(0)
        self.spikes = [Spike(800, WIN_HEIGHT - BASE.get_height() - SPIKE.get_height(), 0, 50, 50)]
        self.blocks = [Block(1200, WIN_HEIGHT - BASE.get_height() - BLOCK.get_height(), 0, 75, 75)]
        self.spikes = [Grav_Spring(800, WIN_HEIGHT - BASE.get_height() - GRAV_SPRING.get_height(), 0)]
        self.cube = Cyclops(200, 0)'''

        # SET BASE AND BACKGROUND
        self.base = Base()
        self.background = Bg(0)

        # SET COMPONENTS
        self.components = {
            "all_comp": all_comp,  # Spikes, GravSpring
            "blocks": self.blocks,
        }

        # SET PORTALS
        self.portals = {
            "laser_portal": laser_portal,
            "cube_portal": cube_portal,
            "orb_portal": orb_portal,
            "dragon_portal": dragon_portal,
            "cyclops_portal": cyclops_portal
        }

        # SET GAMEMODES
        if gamemode == "cube":
            self.player = Cube(500, 0)
            self.player.gamemode = "cube"
        elif gamemode == "laser":
            self.player = Laser(500)
            self.player.gamemode = "laser"
        elif gamemode == "orb":
            self.player = Orb(500, 0)
            self.player.gamemode = "orb"
        elif gamemode == "dragon":
            self.player = Dragon(500, 0)
            self.player.gamemode = "dragon"
        elif gamemode == "cyclops":
            self.player = Cyclops(500, 0)
            self.player.gamemode = "cyclops"

    def portals_test(self):
        for key, portal in self.portals.items():
            for i in range(0, len(portal)):
                if portal[i].x < INITIAL_X and not portal[i].passed:
                    portal[i].passed = True
                    if key == "laser_portal":
                        self.player = Laser(self.player.y)
                        self.player.gamemode = "laser"
                    elif key == "cube_portal":
                        self.player = Cube(self.player.y, 0)
                        self.player.gamemode = "cube"
                    elif key == "orb_portal":
                        self.player = Orb(self.player.y, 0)
                        self.player.gamemode = "orb"
                    elif key == "dragon_portal":
                        self.player = Dragon(self.player.y, 0)
                        self.player.gamemode = "dragon"
                    elif key == "cyclops_portal":
                        self.player = Cyclops(self.player.y, 0)
                        self.player.gamemode = "cyclops"
