# This will serve as the main script, holding the over all structure of the game itself

# Section 0 :: Import necessary modules
import pygame as pyg
import math
import random

background_1 = pygame.image.load("Background 1.png")
background_2 = pygame.image.load("Background 2.png")
building_1 = pygame.image.load("Building 1.png")
building_2 = pygame.image.load("Bulding 2.png")
building_3 = pygame.image.load("Building 3.png")




# Section 1 :: Initialize literally everything
pyg.init()
pyg.display.init()
width = 1280
height = 720
screen = pyg.display.set_mode((width, height))

keys = [False, False, False, False]
player_pos = [100, 100]

running = True
while running:
    pyg.display.flip()
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False
# Section 2 :: Create the screen and the world in which the player will traverse

# Section 3 :: Spawn essentials (Player, NPC's, etc.)
# Section 4 :: Create game loop for beginning and ending
# Section 5 :: Design control structure for player
# Section 6 :: Design update structure for screen
