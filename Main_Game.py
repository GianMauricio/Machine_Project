# This will serve as the main script, holding the over all structure of the game itself

# Section 0 :: Import necessary modules
import pygame as pyg
import math


background_1 = pygame.image.load("Background 1.png")
background_2 = pygame.image.load("Background 2.png")
building_1 = pygame.image.load("Building 1.png")
building_2 = pygame.image.load("Bulding 2.png")
building_3 = pygame.image.load("Building 3.png")
player_sprt = pygame.image.load("Player Sprite00.png")
npc_sprt01 = pygame.image.load("IECMPTK NPC 100.png")
npc_sprt02 = pygame.image.load("IECMPTK NPC 200.png")
npc_sprt03 = pygame.image.load("IECMPTK NPC 300.png")


# Section 1 :: Initialize literally everything
pyg.init()
pyg.display.init()
width = 1280
height = 695
screen = pyg.display.set_mode((width, height))

# These are the backgrounds
bg_1 = pyg.image.load("Resources/Assets/Background_1.png")
bg_2 = pyg.image.load("Resources/Assets/Background_2.png")
build_1 = pyg.image.load("Resources/Assets/Building_1.png")
build_2 = pyg.image.load("Resources/Assets/Building_2.png")
build_3 = pyg.image.load("Resources/Assets/Building_3.png")

# These are the character sprites
player_front_idle = pyg.image.load("Resources/Player/Player_Sprite00.png")
player_left_idle = pyg.image.load("Resources/Player/Player_Sprite12.png")
player_right_idle = pyg.image.load("Resources/Player/Player_Sprite04.png")
player = player_front_idle

'''
# These are the NPC's
npc_1 = pyg.image.load("Resources/NPC_1/1")
npc_2 = pyg.image.load("Resources/NPC_2/1")
npc_3 = pyg.image.load("Resources/NPC_3/1")
'''

# Basic control array for later
keys = [False, False, False, False]
player_pos = [100, 100]

# Section 2 :: Create the screen and the world in which the player will traverse
running = True
while running:
    # Screen Clear
    screen.fill(0)
    # Section 3 :: Display background
    for x_point in range(math.floor((width / bg_1.get_width())) + 1):
        for y_point in range(math.floor((height / bg_1.get_height())) + 1):
            screen.blit(bg_1, (x_point * 100, y_point * 100))

    # Shifts the rotation and position of the player:
    # Takes the current location of the mouse
    position = pyg.mouse.get_pos()
    # Sets the angle of rotation (In radians)
    angle = math.atan2(position[1] - (player_pos[1] + 32), position[0] - (player_pos[0] + 26))
    # Sets the actual rotation of the player (In degrees)
    player_rot = pyg.transform.rotate(player, 360 - angle * 57.29)
    # Calculate new position to compensate for rotation
    player_pos1 = (player_pos[0] - player_rot.get_rect().width / 2, player_pos[1] - player_rot.get_rect().height / 2)
    # Draw player
    screen.blit(player_rot, player_pos1)

    pyg.display.flip()

    # Section 4 :: Create game loop for beginning and ending
    # Loops through the current list of events (Event Handling)
    for event in pyg.event.get():

        # Control structure for movement:
        # If player presses a key
        # Section 5 :: Design control structure for player
        if event.type == pyg.KEYDOWN:
            # Key W
            if event.key == pyg.K_w:
                keys[0] = True
            # Key A
            elif event.key == pyg.K_a:
                keys[1] = True
            # Key S
            elif event.key == pyg.K_s:
                keys[2] = True
            # Key D
            elif event.key == pyg.K_d:
                keys[3] = True

        # If player releases a key
        if event.type == pyg.KEYUP:
            # Key W
            if event.key == pyg.K_w:
                keys[0] = False
            # Key A
            elif event.key == pyg.K_a:
                keys[1] = False
            # Key S
            elif event.key == pyg.K_s:
                keys[2] = False
            # Key D
            elif event.key == pyg.K_d:
                keys[3] = False

    # Change player location according to movements made:
    if keys[0]:
        # Move player up
        player_pos[1] -= 5
    if keys[2]:
        player_pos[1] += 5
    if keys[1]:
        player_pos[0] -= 5
    if keys[3]:
        player_pos[0] += 5

for event in pyg.event.get():
    if event.type == pyg.QUIT:
        running = False
    # Section 6 :: Design update structure for screen
