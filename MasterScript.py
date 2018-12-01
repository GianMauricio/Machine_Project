# This will serve as the main game loop for our multiplication operation problems
# Much of this will be placeholder

# Import literally everything
import pygame as pyg
from random import randint as rin
import Verification
from SpinPutBox import *
import BoxerUnboxer

# Initialize stuff for pygame
pyg.init()
pyg.display.init()
width = 1280
height = 695
screen = pyg.display.set_mode((width, height))
screen_Rect = screen.get_rect()

# Initialize stuff for SpinPutBox
input_box1 = InputBox(screen_Rect.centerx - 400, screen_Rect.centery - 310, 140, 32, 0)
input_box2 = InputBox(screen_Rect.centerx - 375, screen_Rect.centery - 310, 140, 32, 1)
input_box3 = InputBox(screen_Rect.centerx - 350, screen_Rect.centery - 310, 140, 32, 2)
input_box4 = InputBox(screen_Rect.centerx - 325, screen_Rect.centery - 310, 140, 32, 3)

input_box5 = InputBox(screen_Rect.centerx - 480, screen_Rect.centery - 290, 140, 32, 2)
input_box6 = InputBox(screen_Rect.centerx - 505, screen_Rect.centery - 290, 140, 32, 3)
number_font = pyg.font.Font(None, 24)
instance = 0

# Initialize the actual problem
r2 = rin(10, 99)
r1 = rin(10, 99)

true_ans = r1 * r2

# Debug display for the actual problem (gives the answer)
print(r1, "*", r2, "=", true_ans)
user_input = true_ans

# Begin main game loop stage 1
while instance == 0:
    # Reset screen
    screen.fill(0)
    # Set string main_problem_string as the actual problem as generated above
    main_problem_string = "Main problem: {} * {} = ".format(r1, r2)

    # Using string, make a render to be displayed
    render_main_problem = number_font.render(main_problem_string, True, (255, 255, 255))
    # Generate new Rect main_problem_Rect using the Rect of the screen
    main_problem_Rect = screen.get_rect()
    # Adjust values of the main_problem_Rect
    main_problem_Rect.centerx = main_problem_Rect.centerx + 50
    main_problem_Rect.centery = main_problem_Rect.centery + 50

    # Display the actual problem using the previously generated Rect
    screen.blit(render_main_problem, main_problem_Rect)

    # Begin check for box display
    # If 4 boxes...
    if true_ans >= 1000:
        # Generate array to hold all boxes
        input_boxes = [input_box1, input_box2, input_box3, input_box4]

        # Everything below this is the same as above, rewritten to sustain the display of the main problem throughout
        # the use of this conditional
        screen.fill(0)
        main_problem_string = "Main problem: {} * {} = ".format(r1, r2)

        render_main_problem = number_font.render(main_problem_string, True, (255, 255, 255))
        main_problem_Rect = screen.get_rect()
        main_problem_Rect.centerx = main_problem_Rect.centerx + 50
        main_problem_Rect.centery = main_problem_Rect.centery + 50

        screen.blit(render_main_problem, main_problem_Rect)

        # Update all boxes using the function in SpinPutBox
        for box in input_boxes:
            box.update()

        # Display updated boxes using another function in SpinPutBox
        for box in input_boxes:
            box.draw(screen)

        # Update display
        pyg.display.flip()

        # Event handling
        for event in pyg.event.get():
            # For each box in the array...
            for box in input_boxes:
                # Use event handler in SpinPutBox
                box.handle_event(event)
                # Set value of the user_input to the global variable in BoxerUnboxer
                user_input = BoxerUnboxer.final_input

                # Generate boolean according to verification function in Verification
                progress = Verification.verification(user_input, true_ans)

                # Conditional to progress (Flip this to make it correct)
                if not progress:
                    instance = 0
                else:
                    instance = 1

    # If 3 boxes...
    else:
        # Generate array to hold all boxes
        input_boxes = [input_box2, input_box3, input_box4]

        # Again this is here to keep the main problem displaying throughout this conditional
        main_problem_string = "Main problem: {} * {} = ".format(r1, r2)

        render_main_problem = number_font.render(main_problem_string, True, (255, 255, 255))
        main_problem_Rect = screen.get_rect()
        main_problem_Rect.centerx = main_problem_Rect.centerx + 50
        main_problem_Rect.centery = main_problem_Rect.centery + 50

        screen.blit(render_main_problem, main_problem_Rect)

        # Update all boxes using the function in SpinPutBox
        for box in input_boxes:
            box.update()

        # Display updated boxes using another function in SpinPutBox
        for box in input_boxes:
            box.draw(screen)

        # Update display
        pyg.display.flip()

        # Event handling
        for event in pyg.event.get():
            # For each box in the array...
            for box in input_boxes:
                # Use event handler in SpinPutBox
                box.handle_event(event)
                # Set value of the user_input to the global variable in BoxerUnboxer
                user_input = BoxerUnboxer.final_input

                # Generate boolean according to verification function in Verification
                progress = Verification.verification(user_input, true_ans)

                # Conditional to progress (Flip this to make it correct)
                if not progress:
                    instance = 0
                else:
                    instance = 1


# Begin the LOIF part of the script
# This group wil display the problems
# L takes two integers
def begin_l(integer_1, integer_2):
    # Always check (Might be useless)
    while 1:
        # Take the last digit of both integers
        last_digit_1 = integer_1 % 10
        last_digit_2 = integer_2 % 10

        # Generate a render based on the digits calculated
        l_string = number_font.render("L problem: {} * {} = ".format(last_digit_1, last_digit_2),
                                      True, (255, 192, 203))

        # Return the render
        return l_string


# O takes two integers
def begin_2(integer_1, integer_2):
    # Always check (Might be useless)
    while 1:
        # Take the first digit of the first integer
        first_digit_1 = int(integer_1/10)
        # Take the last digit of the second integer
        last_digit_2 = integer_2 % 10
        # Calculate answer (delete this to remove answer from display)
        ans = first_digit_1 * last_digit_2

        # Generate a render based on the digits calculated and the answer calculated
        o_string = number_font.render("O problem: {} * {} = {} ".format(first_digit_1, last_digit_2, ans),
                                      True, (255, 0, 0))

        # Return the render
        return o_string


# I takes two integers
def begin_3(integer_1, integer_2):
    # Always Check (Might be useless)
    while 1:
        # Take the last digit of the first integer
        last_digit_1 = integer_1 % 10
        # Take the first digit of the second integer
        first_digit_2 = int(integer_2 / 10)
        # Calculate answer (delete this to remove answer from display)
        ans = last_digit_1 * first_digit_2

        # Generate a render based on the digits calculated and the answer calculated
        i_string = number_font.render("I problem: {} * {} = {} ".format(last_digit_1, first_digit_2, ans),
                                      True, (135, 206, 250))

        # Return the render
        return i_string


# F takes two  integers
def begin_4(integer_1, integer_2):
    # Always Check (Might be useless)
    while 1:
        # Yoinks the first digit of both integers
        first_digit_1 = int(integer_1 / 10)
        first_digit_2 = int(integer_2 / 10)
        # Thinks the answer using computer magic
        ans = first_digit_1 * first_digit_2

        # Pulls a render from the 6th dimension
        f_string = number_font.render("F problem: {} * {} = {} ".format(first_digit_1, first_digit_2, ans),
                                      True, (255, 255, 0))

        # YEETS the render
        return f_string


# This group will calculate the answers per step
# L takes two integers, does exactly what the previous function did but returns an integer not a render
def step_1(integer_1, integer_2):
    while 1:
        last_digit_1 = integer_1 % 10
        last_digit_2 = integer_2 % 10
        ans = last_digit_1 * last_digit_2

        return ans


# O takes two integers, does exactly what the previous function did but returns an integer not a render
def step_2(integer_1, integer_2):
    while 1:
        first_digit_1 = int(integer_1/10)
        last_digit_2 = integer_2 % 10
        ans = first_digit_1 * last_digit_2

        return ans


# I takes two integers, does exactly what the previous function did but returns an integer not a render
def step_3(integer_1, integer_2):
    while 1:
        last_digit_1 = integer_1 % 10
        first_digit_2 = int(integer_2 / 10)
        ans = last_digit_1 * first_digit_2

        return ans


# F takes two integers, does exactly what the previous function did but returns an integer not a render
def step_4(integer_1, integer_2):
    while 1:
        first_digit_1 = int(integer_1 / 10)
        first_digit_2 = int(integer_2 / 10)
        ans = first_digit_1 * first_digit_2

        return ans


# Begin main game loop stage 2
while instance == 1:
    # Clean the screen
    screen.fill(0)

    # Create a string of the main problem without the answer
    main_problem_string = "Main problem: {} * {} = ".format(r1, r2)

    # Generate a render and the Rect of the main_problem_string
    render_main_problem = number_font.render(main_problem_string, True, (255, 255, 255))
    main_problem_Rect = screen.get_rect()

    # Blit the f***er onto the screen
    screen.blit(render_main_problem, main_problem_Rect)

    # Generate a Rect for the L step of the LOIF
    L_problem_Rect = screen.get_rect()
    L_problem_Rect.centery = screen.get_rect().centery + 72

    # Blit the f***er
    screen.blit(begin_l(r1, r2), L_problem_Rect)
    # Calculate the answer of step one
    answer = step_1(r1, r2)

    # Check if step one was answered correctly
    # If two boxes are to be displayed
    if answer >= 10:
        # Generate array of two boxes
        input_boxes = [input_box5, input_box6]

        # Update each box
        for box in input_boxes:
            box.update()

        # Draw each box onto the screen
        for box in input_boxes:
            box.draw(screen)

        # Update screen
        pyg.display.flip()

        # Event handling
        for event in pyg.event.get():
            for box in input_boxes:
                box.handle_event(event)
                user_input = BoxerUnboxer.final_input

                progress = Verification.verification(user_input, answer)

                if progress:
                    instance = 0
                else:
                    instance = 1
                    # Cleans the final_input global variable of BoxerUnboxer
                    BU.clean_box()

    # If one box is to be displayed
    else:
        input_boxes = [input_box6]

        for box in input_boxes:
            box.update()

        for box in input_boxes:
            box.draw(screen)

        pyg.display.flip()

        for event in pyg.event.get():
            for box in input_boxes:
                box.handle_event(event)
                user_input = BoxerUnboxer.final_input

                progress = Verification.verification(user_input, answer)

                if progress:
                    instance = 1
                else:
                    instance = 2

    O_problem_Rect = screen.get_rect()
    O_problem_Rect.centery = screen.get_rect().centery + 144

    I_problem_Rect = screen.get_rect()
    I_problem_Rect.centery = screen.get_rect().centery + 216

    F_problem_Rect = screen.get_rect()
    F_problem_Rect.centery = screen.get_rect().centery + 288

    screen.blit(begin_2(r1, r2), O_problem_Rect)
    screen.blit(begin_3(r1, r2), I_problem_Rect)
    screen.blit(begin_4(r1, r2), F_problem_Rect)
    pyg.display.flip()

    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            instance += 1
