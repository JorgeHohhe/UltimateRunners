import pygame
import os

BLOCK = pygame.image.load(os.path.join("source/graphics/images", "block.png"))
SPIKE = pygame.image.load(os.path.join("source/graphics/images", "spike.png"))
BG = pygame.image.load(os.path.join("source/graphics/images", "bg1.jpg"))
BASE = pygame.transform.scale2x(pygame.image.load(os.path.join("source/graphics/images", "base.png")))
SIDE = pygame.transform.scale(pygame.image.load(os.path.join("source/graphics/images", "SideBlock.png")), (436, 20))
GRAV_SPRING = pygame.transform.scale(pygame.image.load(os.path.join("source/graphics/images", "GravitySpring.png")), (50, 11))
LAVA = pygame.image.load(os.path.join("source/graphics/images", "lava.png"))
YELLOW_SPRING = pygame.transform.scale(pygame.image.load(os.path.join("source/graphics/images", "YellowSpring.png")), (50, 11))

PLAYER_EXPLOSION_FRAME_0 = pygame.image.load(os.path.join("source/graphics/images/PlayerExplosion", "PlayerExplosion0.png"))
PLAYER_EXPLOSION_FRAME_1 = pygame.image.load(os.path.join("source/graphics/images/PlayerExplosion", "PlayerExplosion1.png"))
PLAYER_EXPLOSION_FRAME_2 = pygame.image.load(os.path.join("source/graphics/images/PlayerExplosion", "PlayerExplosion2.png"))
PLAYER_EXPLOSION_FRAME_3 = pygame.image.load(os.path.join("source/graphics/images/PlayerExplosion", "PlayerExplosion3.png"))
PLAYER_EXPLOSION_FRAME_4 = pygame.image.load(os.path.join("source/graphics/images/PlayerExplosion", "PlayerExplosion4.png"))
PLAYER_EXPLOSION_FRAME_5 = pygame.image.load(os.path.join("source/graphics/images/PlayerExplosion", "PlayerExplosion5.png"))
PLAYER_EXPLOSION_FRAME_6 = pygame.image.load(os.path.join("source/graphics/images/PlayerExplosion", "PlayerExplosion6.png"))
PLAYER_EXPLOSION_FRAME_7 = pygame.image.load(os.path.join("source/graphics/images/PlayerExplosion", "PlayerExplosion7.png"))
PLAYER_EXPLOSION = [PLAYER_EXPLOSION_FRAME_1, PLAYER_EXPLOSION_FRAME_2, PLAYER_EXPLOSION_FRAME_3, PLAYER_EXPLOSION_FRAME_4, PLAYER_EXPLOSION_FRAME_5, PLAYER_EXPLOSION_FRAME_6, PLAYER_EXPLOSION_FRAME_7]


# GAMEMODES AND PORTALS
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
