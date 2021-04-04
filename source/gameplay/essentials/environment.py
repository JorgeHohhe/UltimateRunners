from ..components.transporters.springs.gravity_spring import GravSpring
from ..components.transporters.springs.yellow_spring import YellowSpring
from ..components.transporters.globes.yellow_globe import YellowGlobe
from ..components.transporters.globes.gravity_globe import GravityGlobe
from ..components.platforms.block import Block, MobileBlock
from ..components.hazards.spike import Spike
from ..characters.cube import Cube
from .base import Base
from .background import Bg
from ..utils.constants import *
from ...graphics.images_loader import BASE, BLOCK, GRAV_SPRING, MOBILE_RECTANGLE, SPIKE

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
            elif f[0] == "mobile_block":
                f[2] = WIN_HEIGHT - BASE.get_height() - int(f[4]) - int(f[2])
                self.blocks.append(MobileBlock(int(f[1]), f[2], 0, int(f[3]), int(f[4])))
            elif f[0] == "yellowspring":
                f[2] = WIN_HEIGHT - BASE.get_height() - YELLOW_SPRING.get_height() - int(f[2])
                all_comp.append(YellowSpring(int(f[1]), f[2], int(f[3])))
            elif f[0] == "yellowglobe":
                f[2] = WIN_HEIGHT - BASE.get_height() - YELLOW_GLOBE.get_height() - int(f[2])
                all_comp.append(YellowGlobe(int(f[1]), f[2], 0))
            elif f[0] == "gravityglobe":
                f[2] = WIN_HEIGHT - BASE.get_height() - GRAVITY_GLOBE.get_height() - int(f[2])
                all_comp.append(GravityGlobe(int(f[1]), f[2], 0))             
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
        self.spikes = [Spike(800, WIN_HEIGHT - BASE.get_height() - SPIKE.get_height(), 0)]
        self.blocks = [Block(1200, WIN_HEIGHT - BASE.get_height() - BLOCK.get_height(), 0)]
        self.mobiles = [Mobile(1550, WIN_HEIGHT - BASE.get_height() - MOBILE_RECTANGLE.get_height(), 0)]
        self.spikes = [Grav_Spring(800, WIN_HEIGHT - BASE.get_height() - GRAV_SPRING.get_height(), 0)]
        self.cube = Cube(200, 200)


    def map_setup(self):
        self.blocks.append(Block(800, WIN_HEIGHT - BASE.get_height() - BLOCK.get_height(), 0))
        self.blocks.append(Block(1050, WIN_HEIGHT - BASE.get_height() - BLOCK.get_height(), 0))
        self.blocks.append(Block(1050, WIN_HEIGHT - BASE.get_height() - BLOCK.get_height() - 75, 0))
        self.mobiles.append(Mobile(3900, WIN_HEIGHT - BASE.get_height() - MOBILE_RECTANGLE.get_height(), 0))
        self.spikes.append(Grav_Spring(1200, BASE.get_height()- GRAV_SPRING.get_height()-15, 180))
