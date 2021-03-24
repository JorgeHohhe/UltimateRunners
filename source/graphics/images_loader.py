import pygame
import os

BLOCK = pygame.transform.scale(pygame.image.load(os.path.join("source/graphics/images", "block.png")), (75, 75))
SPIKE = pygame.transform.scale(pygame.image.load(os.path.join("source/graphics/images", "spike.png")), (50, 50))
BG = pygame.image.load(os.path.join("source/graphics/images", "bg1.jpg"))
BASE = pygame.transform.scale2x(pygame.image.load(os.path.join("source/graphics/images", "base.png")))
SIDE = pygame.transform.scale(pygame.image.load(os.path.join("source/graphics/images", "SideBlock.png")), (436, 20))
GRAV_SPRING = pygame.transform.scale(pygame.image.load(os.path.join("source/graphics/images", "GravitySpring.png")), (50, 12))

#GAMEMODES
CUBE = pygame.transform.scale(pygame.image.load(os.path.join("source/graphics/images", "cube.png")), (75, 75))
CUBE_PORTAL = pygame.transform.scale(pygame.image.load(os.path.join("source/graphics/images", "CubePortal.png")), (81, 150))
LASER = pygame.transform.scale(pygame.image.load(os.path.join("source/graphics/images", "Laser.png")), (47, 75))
LASER_BACK = pygame.transform.scale(pygame.image.load(os.path.join("source/graphics/images", "LaserBack.png")), (10, 10))
LASER_PORTAL = pygame.transform.scale(pygame.image.load(os.path.join("source/graphics/images", "LaserPortal.png")), (81, 150))
ORB = pygame.transform.scale(pygame.image.load(os.path.join("source/graphics/images", "Orb.png")), (75, 75))
ORB_PORTAL = pygame.transform.scale(pygame.image.load(os.path.join("source/graphics/images", "OrbPortal.png")), (81, 150))
DRAGON = pygame.transform.scale(pygame.image.load(os.path.join("source/graphics/images", "Dragon.png")), (125, 72))
DRAGON_PORTAL = pygame.transform.scale(pygame.image.load(os.path.join("source/graphics/images", "DragonPortal.png")), (81, 150))
CYCLOPS_FRAME_0 = pygame.transform.scale(pygame.image.load(os.path.join("source/graphics/images", "CyclopsFrame0.png")), (120, 75))
CYCLOPS_FRAME_1 = pygame.transform.scale(pygame.image.load(os.path.join("source/graphics/images", "CyclopsFrame1.png")), (120, 75))
CYCLOPS_FRAME_2 = pygame.transform.scale(pygame.image.load(os.path.join("source/graphics/images", "CyclopsFrame2.png")), (120, 75))
CYCLOPS_FRAME_3 = pygame.transform.scale(pygame.image.load(os.path.join("source/graphics/images", "CyclopsFrame3.png")), (120, 75))
CYCLOPS_FRAME_4 = pygame.transform.scale(pygame.image.load(os.path.join("source/graphics/images", "CyclopsFrame4.png")), (120, 75))
CYCLOPS_FRAME_5 = pygame.transform.scale(pygame.image.load(os.path.join("source/graphics/images", "CyclopsFrame5.png")), (120, 75))
CYCLOPS_FRAME_6 = pygame.transform.scale(pygame.image.load(os.path.join("source/graphics/images", "CyclopsFrame6.png")), (120, 75))
CYCLOPS_PORTAL = pygame.transform.scale(pygame.image.load(os.path.join("source/graphics/images", "CyclopsPortal.png")), (81, 150))

CYCLOPS = [CYCLOPS_FRAME_0, CYCLOPS_FRAME_1, CYCLOPS_FRAME_2, CYCLOPS_FRAME_3, CYCLOPS_FRAME_4, CYCLOPS_FRAME_5, CYCLOPS_FRAME_6]
PORTALS = [CUBE_PORTAL, LASER_PORTAL, ORB_PORTAL, DRAGON_PORTAL, CYCLOPS_PORTAL]
