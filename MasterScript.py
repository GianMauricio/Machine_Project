# This will serve as the main game loop for our multiplication operation problems
# Much of this will be placeholder

import pygame as pyg
from random import randint as rin

pyg.init()
pyg.display.init()
width = 1280
height = 695
screen = pyg.display.set_mode((width, height))

number_font = pyg.font.Font(None, 24)
running = True

r2 = rin(10, 99)
r1 = rin(10, 99)

true_ans = r1 * r2

print(r1, "*", r2, "=", true_ans)

if true_ans >= 1000:
    print("Now spawning 4 boxes")

else:
    print("Now spawning 3 boxes")

"Begin the LOIF part of the script"


# L
def begin_l(integer_1, integer_2):
    last_digit_1 = integer_1 % 10
    last_digit_2 = integer_2 % 10
    ans = last_digit_1 * last_digit_2

    l_string = number_font.render("L problem: {} * {} = {} ".format(last_digit_1, last_digit_2, ans)
                                  , True, (255, 192, 203))

    return l_string


# O
def begin_2(integer_1, integer_2):
    first_digit_1 = int(integer_1/10)
    last_digit_2 = integer_2 % 10
    ans = first_digit_1 * last_digit_2

    o_string = number_font.render("O problem: {} * {} = {} ".format(first_digit_1, last_digit_2, ans)
                                  , True, (255, 0, 0))

    return o_string


# I
def begin_3(integer_1, integer_2):
    last_digit_1 = integer_1 % 10
    first_digit_2 = int(integer_2 / 10)
    ans = last_digit_1 * first_digit_2

    i_string = number_font.render("I problem: {} * {} = {} ".format(last_digit_1, first_digit_2, ans)
                                  , True, (135, 206, 250))

    return i_string


# F
def begin_4(integer_1, integer_2):
    first_digit_1 = int(integer_1 / 10)
    first_digit_2 = int(integer_2 / 10)
    ans = first_digit_1 * first_digit_2

    f_string = number_font.render("F problem: {} * {} = {} ".format(first_digit_1, first_digit_2, ans)
                                  , True, (255, 255, 0))

    return f_string


while running:

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
            running = False
