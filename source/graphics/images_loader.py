import pygame
import os

CUBE = pygame.transform.scale(pygame.image.load(os.path.join("source/graphics/images", "cube.png")), (75, 75))
BLOCK = pygame.transform.scale(pygame.image.load(os.path.join("source/graphics/images", "block.png")), (75, 75))
SPIKE = pygame.transform.scale(pygame.image.load(os.path.join("source/graphics/images", "spike.png")), (50, 50))
BG = pygame.image.load(os.path.join("source/graphics/images", "bg1.jpg"))
BASE = pygame.transform.scale2x(pygame.image.load(os.path.join("source/graphics/images", "base.png")))
SIDE = pygame.transform.scale(pygame.image.load(os.path.join("source/graphics/images", "SideBlock.png")), (436, 20))
GRAV_SPRING = pygame.transform.scale(pygame.image.load(os.path.join("source/graphics/images", "GravitySpring.png")), (50, 12))
MOBILE_RECTANGLE = pygame.transform.scale(pygame.image.load(os.path.join("source/graphics/images", "MobileRectangle.png")), (50,300))