# This will serve as the main game loop for our multiplication operation problems
# Much of this will be placeholder

import pygame as pyg
from random import randint as rin
import Verification
from SpinPutBox import *

pyg.init()
pyg.display.init()
width = 1280
height = 695
screen = pyg.display.set_mode((width, height))

number_font = pyg.font.Font(None, 24)
instance = 0

r2 = rin(10, 99)
r1 = rin(10, 99)

true_ans = r1 * r2

print(r1, "*", r2, "=", true_ans)
user_input = true_ans
while instance == 0:
    screen.fill(0)
    main_problem_string = "Main problem: {} * {} = ".format(r1, r2)

    render_main_problem = number_font.render(main_problem_string, True, (255, 255, 255))
    main_problem_Rect = screen.get_rect()
    main_problem_Rect.centerx = main_problem_Rect.centerx + 50
    main_problem_Rect.centery = main_problem_Rect.centery + 50

    screen.blit(render_main_problem, main_problem_Rect)

    if true_ans >= 1000:
        print("Now spawning 4 boxes")

        input_box1 = InputBox(main_problem_Rect.centerx - 450, main_problem_Rect.centery - 360, 140, 32, 0)
        input_box2 = InputBox(main_problem_Rect.centerx - 425, main_problem_Rect.centery - 360, 140, 32, 1)
        input_box3 = InputBox(main_problem_Rect.centerx - 400, main_problem_Rect.centery - 360, 140, 32, 2)
        input_box4 = InputBox(main_problem_Rect.centerx - 375, main_problem_Rect.centery - 360, 140, 32, 3)
        input_boxes = [input_box1, input_box2, input_box3, input_box4]
        done = False

        while not done:
            screen.fill(0)
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

            pyg.display.flip()

            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    done = True

                for box in input_boxes:
                    box.handle_event(event)

    else:
        print("Now spawning 3 boxes")

        input_box1 = InputBox(main_problem_Rect.centerx - 450, main_problem_Rect.centery - 360, 140, 32)
        input_box2 = InputBox(main_problem_Rect.centerx - 425, main_problem_Rect.centery - 360, 140, 32)
        input_box3 = InputBox(main_problem_Rect.centerx - 400, main_problem_Rect.centery - 360, 140, 32)
        input_boxes = [input_box1, input_box2, input_box3]
        done = False

        while not done:
            screen.fill(0)
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

            pyg.display.flip()

            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    done = True

                for box in input_boxes:
                    box.handle_event(event)

    user_input = true_ans

    progress = Verification.verification(user_input, true_ans)

    if progress:
        instance = 0
    else:
        instance = 1


# Begin the LOIF part of the script

# L
def begin_l(integer_1, integer_2):
    while 1:
        last_digit_1 = integer_1 % 10
        last_digit_2 = integer_2 % 10
        ans = last_digit_1 * last_digit_2

        l_string = number_font.render("L problem: {} * {} = {} ".format(last_digit_1, last_digit_2, ans),
                                      True, (255, 192, 203))

        if ans >= 10:
            print("Now spawning 2 boxes")
        else:
            print("Now spawning one box")

        u_input = ans

        correctness = Verification.verification(u_input, ans)

        if correctness:
            return l_string


# O
def begin_2(integer_1, integer_2):
    while 1:
        first_digit_1 = int(integer_1/10)
        last_digit_2 = integer_2 % 10
        ans = first_digit_1 * last_digit_2

        o_string = number_font.render("O problem: {} * {} = {} ".format(first_digit_1, last_digit_2, ans),
                                      True, (255, 0, 0))

        if ans >= 10:
            print("Now spawning 2 boxes")
        else:
            print("Now spawning one box")

        u_input = ans

        correctness = Verification.verification(u_input, ans)

        if correctness:
            return o_string


# I
def begin_3(integer_1, integer_2):
    while 1:
        last_digit_1 = integer_1 % 10
        first_digit_2 = int(integer_2 / 10)
        ans = last_digit_1 * first_digit_2

        i_string = number_font.render("I problem: {} * {} = {} ".format(last_digit_1, first_digit_2, ans),
                                      True, (135, 206, 250))

        if ans >= 10:
            print("Now spawning 2 boxes")
        else:
            print("Now spawning one box")

        u_input = ans

        correctness = Verification.verification(u_input, ans)

        if correctness:
            return i_string


# F
def begin_4(integer_1, integer_2):
    while 1:
        first_digit_1 = int(integer_1 / 10)
        first_digit_2 = int(integer_2 / 10)
        ans = first_digit_1 * first_digit_2

        f_string = number_font.render("F problem: {} * {} = {} ".format(first_digit_1, first_digit_2, ans),
                                      True, (255, 255, 0))

        if ans >= 10:
            print("Now spawning 2 boxes")
        else:
            print("Now spawning one box")

        u_input = ans

        correctness = Verification.verification(u_input, ans)

        if correctness:
            return f_string


while instance == 1:

    screen.fill(0)

    main_problem_string = "Main problem: {} * {} = {} ".format(r1, r2, true_ans)

    render_main_problem = number_font.render(main_problem_string, True, (255, 255, 255))
    main_problem_Rect = screen.get_rect()
    L_problem_Rect = screen.get_rect()
    L_problem_Rect.centery = screen.get_rect().centery + 24
    O_problem_Rect = screen.get_rect()
    O_problem_Rect.centery = screen.get_rect().centery + 48
    I_problem_Rect = screen.get_rect()
    I_problem_Rect.centery = screen.get_rect().centery + 72
    F_problem_Rect = screen.get_rect()
    F_problem_Rect.centery = screen.get_rect().centery + 96

    screen.blit(render_main_problem, main_problem_Rect)

    screen.blit(begin_l(r1, r2), L_problem_Rect)
    screen.blit(begin_2(r1, r2), O_problem_Rect)
    screen.blit(begin_3(r1, r2), I_problem_Rect)
    screen.blit(begin_4(r1, r2), F_problem_Rect)
    pyg.display.flip()

    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            instance += 1
