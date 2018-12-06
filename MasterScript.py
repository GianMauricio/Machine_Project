# This will serve as the main game loop for our multiplication operation problems

# Import all needed modules
import pygame as pyg
from random import randint as rin
from SpinPutBox import *
from LOIF import *
import BoxerUnboxer
import Verification
import os
import Button
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 0)


# Initialize PyGame and the Screen/Main Surface
pyg.init()
pyg.display.init()
width = 1280
height = 695
screen = pyg.display.set_mode((width, height))

# Take screen Rect for future use because let's be honest we're gonna need it
screen_Rect = screen.get_rect()

# Initialize the sets of input boxes as given by the initialization function in InputBox
# Main 4
input_box1 = InputBox(screen_Rect.centerx - 400, screen_Rect.centery - 310, 140, 32, 0)
input_box2 = InputBox(screen_Rect.centerx - 375, screen_Rect.centery - 310, 140, 32, 1)
input_box3 = InputBox(screen_Rect.centerx - 350, screen_Rect.centery - 310, 140, 32, 2)
input_box4 = InputBox(screen_Rect.centerx - 325, screen_Rect.centery - 310, 140, 32, 3)

# LOIF boxes
input_box5 = InputBox(screen_Rect.centerx - 430, screen_Rect.centery - 240, 140, 32, 3)
input_box6 = InputBox(screen_Rect.centerx - 455, screen_Rect.centery - 240, 140, 32, 2)

input_box7 = InputBox(screen_Rect.centerx - 430, screen_Rect.centery - 170, 190, 32, 3)
input_box8 = InputBox(screen_Rect.centerx - 455, screen_Rect.centery - 170, 190, 32, 2)

input_box9 = InputBox(screen_Rect.centerx - 430, screen_Rect.centery - 100, 195, 32, 3)
input_box10 = InputBox(screen_Rect.centerx - 455, screen_Rect.centery - 100, 195, 32, 2)

input_box11 = InputBox(screen_Rect.centerx - 430, screen_Rect.centery - 30, 200, 32, 3)
input_box12 = InputBox(screen_Rect.centerx - 455, screen_Rect.centery - 30, 200, 32, 2)

# Defining the default font for everything
number_font = pyg.font.Font(None, 24)

# Importing images
title_screen = pyg.image.load("Resources/Assets/Title_screen.png")
start_button_active = pyg.image.load("Resources/Assets/Start_Active.png")
start_button_inactive = pyg.image.load("Resources/Assets/Start_Inactive.png")

title_screen_Rect = screen_Rect


# Set origin instance
instance = 0
# Create two random numbers
r2 = rin(10, 99)
r1 = rin(10, 99)

# Calculate the true answer
true_ans = r1 * r2


start_button = Button.Button(title_screen.get_rect().centerx, title_screen.get_rect().centery, 300, 100,
                             screen, start_button_active, start_button_inactive)


def next_instance():
    print("Forcing instance change")
    global instance
    instance = instance + 1


# Debug code
print(r1, "*", r2, "=", true_ans)
while instance == 0:
    print("Begin game")
    screen.blit(title_screen, title_screen_Rect)

    for event in pyg.event.get():
        start_button.handle_event(event)

    start_button.draw_button()

    if start_button.return_value:
        instance = instance + 1

    pyg.display.flip()
# Begin main instance 1 (Original problem)
while instance == 1:
    # Clear the screen
    screen.fill(0)
    # Create string of main problem
    main_problem_string = "Main problem: {} * {} = ".format(r1, r2)

    # Create render for main problem
    render_main_problem = number_font.render(main_problem_string, True, (255, 255, 255))
    main_problem_Rect = screen.get_rect()
    main_problem_Rect.centerx = main_problem_Rect.centerx + 50
    main_problem_Rect.centery = main_problem_Rect.centery + 50

    # Display render
    screen.blit(render_main_problem, main_problem_Rect)

    # Display four boxes if needed
    if true_ans >= 1000:
        # Create array to store boxes
        input_boxes = [input_box1, input_box2, input_box3, input_box4]
        main_problem_string = "Main problem: {} * {} = ".format(r1, r2)

        # For every box, update the box
        for box in input_boxes:
            box.update()
            box.draw(screen)

        for event in pyg.event.get():
            for box in input_boxes:
                box.handle_event(event)
                user_input = BoxerUnboxer.un_boxer()

        if Verification.verification(Verification.final_value, true_ans):
            BoxerUnboxer.clear_field()
            Verification.reset()
            instance = 2

    else:
        input_boxes = [input_box2, input_box3, input_box4]

        main_problem_string = "Main problem: {} * {} = ".format(r1, r2)

        render_main_problem = number_font.render(main_problem_string, True, (255, 255, 255))
        main_problem_Rect = screen.get_rect()
        main_problem_Rect.centerx = main_problem_Rect.centerx + 50
        main_problem_Rect.centery = main_problem_Rect.centery + 50

        screen.blit(render_main_problem, main_problem_Rect)

        for box in input_boxes:
            box.update()

        for box in input_boxes:
            box.draw(screen)

        for event in pyg.event.get():
            for box in input_boxes:
                box.handle_event(event)
                user_input = BoxerUnboxer.un_boxer()

        if Verification.verification(Verification.final_value, true_ans):
            BoxerUnboxer.clear_field()
            Verification.reset()
            instance = 2

    pyg.display.flip()

# Begin the LOIF
while instance == 2:
    # Clear the screen
    screen.fill(0)
    # Create string of main problem
    main_problem_string = "Main problem: {} * {} = ".format(r1, r2)

    # Create render for main problem
    render_main_problem = number_font.render(main_problem_string, True, (255, 255, 255))
    main_problem_Rect = screen.get_rect()
    main_problem_Rect.centerx = main_problem_Rect.centerx + 50
    main_problem_Rect.centery = main_problem_Rect.centery + 50

    # Display render
    screen.blit(render_main_problem, main_problem_Rect)

    L_problem_Rect = main_problem_Rect
    L_problem_Rect.centery = main_problem_Rect.centery + 72

    screen.blit(begin_l(r1, r2), L_problem_Rect)
    answer = step_1(r1, r2)

    if answer >= 10:
        input_boxes = [input_box5, input_box6]

        for box in input_boxes:
            box.update()

        for box in input_boxes:
            box.draw(screen)

        for event in pyg.event.get():
            for box in input_boxes:
                box.handle_event(event)

        for event in pyg.event.get():
            for box in input_boxes:
                box.handle_event(event)
                user_input = BoxerUnboxer.un_boxer()

        if Verification.verification(Verification.final_value, answer):
            BoxerUnboxer.clear_field()
            Verification.reset()
            instance = 3

    else:
        input_boxes = [input_box5]

        for box in input_boxes:
            box.update()

        for box in input_boxes:
            box.draw(screen)

        for event in pyg.event.get():
            for box in input_boxes:
                box.handle_event(event)

        for event in pyg.event.get():
            for box in input_boxes:
                box.handle_event(event)
                user_input = BoxerUnboxer.un_boxer()

        if Verification.verification(Verification.final_value, answer):
            BoxerUnboxer.clear_field()
            Verification.reset()
            instance = 3

    pyg.display.flip()

while instance == 3:
    # Clear the screen
    screen.fill(0)
    # Create string of main problem
    main_problem_string = "Main problem: {} * {} = ".format(r1, r2)

    # Create render for main problem
    render_main_problem = number_font.render(main_problem_string, True, (255, 255, 255))
    main_problem_Rect = screen.get_rect()
    main_problem_Rect.centerx = main_problem_Rect.centerx + 50
    main_problem_Rect.centery = main_problem_Rect.centery + 50

    # Display render
    screen.blit(render_main_problem, main_problem_Rect)

    O_problem_Rect = main_problem_Rect
    O_problem_Rect.centery = main_problem_Rect.centery + 144

    screen.blit(begin_2(r1, r2), O_problem_Rect)
    answer = step_2(r1, r2)

    if answer >= 10:
        input_boxes = [input_box7, input_box8]

        for box in input_boxes:
            box.update()

        for box in input_boxes:
            box.draw(screen)

        for event in pyg.event.get():
            for box in input_boxes:
                box.handle_event(event)

        for event in pyg.event.get():
            for box in input_boxes:
                box.handle_event(event)
                user_input = BoxerUnboxer.un_boxer()

        if Verification.verification(Verification.final_value, answer):
            BoxerUnboxer.clear_field()
            Verification.reset()
            instance = 4

    else:
        input_boxes = [input_box7]

        for box in input_boxes:
            box.update()

        for box in input_boxes:
            box.draw(screen)

        for event in pyg.event.get():
            for box in input_boxes:
                box.handle_event(event)

        for event in pyg.event.get():
            for box in input_boxes:
                box.handle_event(event)
                user_input = BoxerUnboxer.un_boxer()

        if Verification.verification(Verification.final_value, answer):
            BoxerUnboxer.clear_field()
            Verification.reset()
            instance = 4

    pyg.display.flip()

while instance == 4:
    # Clear the screen
    screen.fill(0)
    # Create string of main problem
    main_problem_string = "Main problem: {} * {} = ".format(r1, r2)

    # Create render for main problem
    render_main_problem = number_font.render(main_problem_string, True, (255, 255, 255))
    main_problem_Rect = screen.get_rect()
    main_problem_Rect.centerx = main_problem_Rect.centerx + 50
    main_problem_Rect.centery = main_problem_Rect.centery + 50

    # Display render
    screen.blit(render_main_problem, main_problem_Rect)

    I_problem_Rect = main_problem_Rect
    I_problem_Rect.centery = main_problem_Rect.centery + 216

    screen.blit(begin_3(r1, r2), I_problem_Rect)
    answer = step_3(r1, r2)

    if answer >= 10:
        input_boxes = [input_box9, input_box10]

        for box in input_boxes:
            box.update()

        for box in input_boxes:
            box.draw(screen)

        for event in pyg.event.get():
            for box in input_boxes:
                box.handle_event(event)

        for event in pyg.event.get():
            for box in input_boxes:
                box.handle_event(event)
                user_input = BoxerUnboxer.un_boxer()

        if Verification.verification(Verification.final_value, answer):
            BoxerUnboxer.clear_field()
            Verification.reset()
            instance = 5

    else:
        input_boxes = [input_box9]

        for box in input_boxes:
            box.update()

        for box in input_boxes:
            box.draw(screen)

        for event in pyg.event.get():
            for box in input_boxes:
                box.handle_event(event)

        for event in pyg.event.get():
            for box in input_boxes:
                box.handle_event(event)
                user_input = BoxerUnboxer.un_boxer()

        if Verification.verification(Verification.final_value, answer):
            BoxerUnboxer.clear_field()
            Verification.reset()
            instance = 5

    pyg.display.flip()

while instance == 5:
    # Clear the screen
    screen.fill(0)
    # Create string of main problem
    main_problem_string = "Main problem: {} * {} = ".format(r1, r2)

    # Create render for main problem
    render_main_problem = number_font.render(main_problem_string, True, (255, 255, 255))
    main_problem_Rect = screen.get_rect()
    main_problem_Rect.centerx = main_problem_Rect.centerx + 50
    main_problem_Rect.centery = main_problem_Rect.centery + 50

    # Display render
    screen.blit(render_main_problem, main_problem_Rect)

    F_problem_Rect = main_problem_Rect
    F_problem_Rect.centery = main_problem_Rect.centery + 288

    screen.blit(begin_4(r1, r2), F_problem_Rect)
    answer = step_4(r1, r2)

    if answer >= 10:
        input_boxes = [input_box11, input_box12]

        for box in input_boxes:
            box.update()

        for box in input_boxes:
            box.draw(screen)

        for event in pyg.event.get():
            for box in input_boxes:
                box.handle_event(event)

        for event in pyg.event.get():
            for box in input_boxes:
                box.handle_event(event)
                user_input = BoxerUnboxer.un_boxer()

        if Verification.verification(Verification.final_value, answer):
            BoxerUnboxer.clear_field()
            Verification.reset()
            instance = 6

    else:
        input_boxes = [input_box11]

        for box in input_boxes:
            box.update()

        for box in input_boxes:
            box.draw(screen)

        for event in pyg.event.get():
            for box in input_boxes:
                box.handle_event(event)

        for event in pyg.event.get():
            for box in input_boxes:
                box.handle_event(event)
                user_input = BoxerUnboxer.un_boxer()

        if Verification.verification(Verification.final_value, answer):
            BoxerUnboxer.clear_field()
            Verification.reset()
            instance = 6

    pyg.display.flip()
