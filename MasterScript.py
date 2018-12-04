# This will serve as the main game loop for our multiplication operation problems


import pygame as pyg
from random import randint as rin
import Verification
from SpinPutBox import *
import BoxerUnboxer

pyg.init()
pyg.display.init()
width = 1280
height = 695
screen = pyg.display.set_mode((width, height))
screen_Rect = screen.get_rect()

input_box1 = InputBox(screen_Rect.centerx - 400, screen_Rect.centery - 310, 140, 32, 0)
input_box2 = InputBox(screen_Rect.centerx - 375, screen_Rect.centery - 310, 140, 32, 1)
input_box3 = InputBox(screen_Rect.centerx - 350, screen_Rect.centery - 310, 140, 32, 2)
input_box4 = InputBox(screen_Rect.centerx - 325, screen_Rect.centery - 310, 140, 32, 3)

input_box5 = InputBox(screen_Rect.centerx - 480, screen_Rect.centery - 290, 140, 32, 2)
input_box6 = InputBox(screen_Rect.centerx - 505, screen_Rect.centery - 290, 140, 32, 3)
input_box7 = InputBox(screen_Rect.centerx - 480, screen_Rect.centery - 215, 190, 32, 2)
input_box8 = InputBox(screen_Rect.centerx - 505, screen_Rect.centery - 215, 190, 32, 3)
input_box9 = InputBox(screen_Rect.centerx - 480, screen_Rect.centery - 145, 195, 32, 2)
input_box10 = InputBox(screen_Rect.centerx - 505, screen_Rect.centery - 145, 195, 32, 3)
input_box11 = InputBox(screen_Rect.centerx - 480, screen_Rect.centery - 75, 200, 32, 2)
input_box12 = InputBox(screen_Rect.centerx - 505, screen_Rect.centery - 75, 200, 32, 3)
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
        input_boxes = [input_box1, input_box2, input_box3, input_box4]

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
            for box in input_boxes:
                box.handle_event(event)
                user_input = BoxerUnboxer.final_input

                progress = Verification.verification(user_input, true_ans)

                if not progress:
                    instance = 0
                else:
                    instance = 1

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

        pyg.display.flip()

        for event in pyg.event.get():
            for box in input_boxes:
                box.handle_event(event)

                user_input = BoxerUnboxer.final_input

                progress = Verification.verification(user_input, true_ans)

                if not progress:
                    instance = 0
                else:
                    instance = 1


# Begin the LOIF part of the script

# L
def begin_l(integer_1, integer_2):
    while 1:
        last_digit_1 = integer_1 % 10
        last_digit_2 = integer_2 % 10

        l_string = number_font.render("L problem: {} * {} = ".format(last_digit_1, last_digit_2),
                                      True, (255, 192, 203))

        return l_string


# O
def begin_2(integer_1, integer_2):
    while 1:
        first_digit_1 = int(integer_1/10)
        last_digit_2 = integer_2 % 10
        ans = first_digit_1 * last_digit_2

        o_string = number_font.render("O problem: {} * {} = ".format(first_digit_1, last_digit_2, ans),
                                      True, (255, 0, 0))

        return o_string


# I
def begin_3(integer_1, integer_2):
    while 1:
        last_digit_1 = integer_1 % 10
        first_digit_2 = int(integer_2 / 10)
        ans = last_digit_1 * first_digit_2

        i_string = number_font.render("I problem: {} * {} = ".format(last_digit_1, first_digit_2, ans),
                                      True, (135, 206, 250))

        return i_string


# F
def begin_4(integer_1, integer_2):
    while 1:
        first_digit_1 = int(integer_1 / 10)
        first_digit_2 = int(integer_2 / 10)
        ans = first_digit_1 * first_digit_2

        f_string = number_font.render("F problem: {} * {} = ".format(first_digit_1, first_digit_2, ans),
                                      True, (255, 255, 0))

        return f_string


# L
def step_1(integer_1, integer_2):
    while 1:
        last_digit_1 = integer_1 % 10
        last_digit_2 = integer_2 % 10
        ans = last_digit_1 * last_digit_2

        return ans


# O
def step_2(integer_1, integer_2):
    while 1:
        first_digit_1 = int(integer_1/10)
        last_digit_2 = integer_2 % 10
        ans = first_digit_1 * last_digit_2

        return ans


# I
def step_3(integer_1, integer_2):
    while 1:
        last_digit_1 = integer_1 % 10
        first_digit_2 = int(integer_2 / 10)
        ans = last_digit_1 * first_digit_2

        return ans


# F
def step_4(integer_1, integer_2):
    while 1:
        first_digit_1 = int(integer_1 / 10)
        first_digit_2 = int(integer_2 / 10)
        ans = first_digit_1 * first_digit_2

        return ans


while instance == 1:
    screen.fill(0)

    main_problem_string = "Main problem: {} * {} = ".format(r1, r2)

    render_main_problem = number_font.render(main_problem_string, True, (255, 255, 255))
    main_problem_Rect = screen.get_rect()

    screen.blit(render_main_problem, main_problem_Rect)

    L_problem_Rect = screen.get_rect()
    L_problem_Rect.centery = screen.get_rect().centery + 72

    screen.blit(begin_l(r1, r2), L_problem_Rect)
    answer = step_1(r1, r2)
    user_input = answer

    if answer >= 10:
        input_boxes = [input_box5, input_box6]
        
        
        for box in input_boxes:
            box.update()

        for box in input_boxes:
            box.draw(screen)

        
        

        for event in pyg.event.get():
            for box in input_boxes:
                box.handle_event(event)
                user_input = BoxerUnboxer.final_input

                progress = Verification.verification(user_input, answer)

                if progress:
                    instance = 0
                else:
                    instance = 1
                    BU.clean_box()
        
    else:
        input_boxes = [input_box6]

        for box in input_boxes:
            box.update()

        for box in input_boxes:
            box.draw(screen)

           
        

        for event in pyg.event.get():
            for box in input_boxes:
                box.handle_event(event)
                user_input = BoxerUnboxer.final_input

                progress = Verification.verification(user_input, answer)

                if progress:
                    instance = 1
                else:
                    instance = 2
                    BU.clean_box()
    
    O_problem_Rect = screen.get_rect()
    O_problem_Rect.centery = screen.get_rect().centery + 144

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
                user_input = BoxerUnboxer.final_input

                progress = Verification.verification(user_input, answer)

                if progress:
                    instance = 0
                else:
                    instance = 1
                    BU.clean_box()
        

    else:
        input_boxes = [input_box8]

        for box in input_boxes:
            box.update()

        for box in input_boxes:
            box.draw(screen)

        

        for event in pyg.event.get():
            for box in input_boxes:
                box.handle_event(event)
                user_input = BoxerUnboxer.final_input

                progress = Verification.verification(user_input, answer)

                if progress:
                    instance = 1
                else:
                    instance = 2
                    BU.clean_box
        
    I_problem_Rect = screen.get_rect()
    I_problem_Rect.centery = screen.get_rect().centery + 216

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
                user_input = BoxerUnboxer.final_input

                progress = Verification.verification(user_input, answer)

                if progress:
                    instance = 0
                else:
                    instance = 1
                    BU.clean_box()
        
    else:
        input_boxes = [input_box10]

        for box in input_boxes:
            box.update()

        for box in input_boxes:
            box.draw(screen)
            
        

        for event in pyg.event.get():
            for box in input_boxes:
                box.handle_event(event)
                user_input = BoxerUnboxer.final_input

                progress = Verification.verification(user_input, answer)

                if progress:
                    instance = 1
                else:
                    instance = 2
                    BU.clean_box()
    
    

    F_problem_Rect = screen.get_rect()
    F_problem_Rect.centery = screen.get_rect().centery + 288

    
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
                user_input = BoxerUnboxer.final_input

                progress = Verification.verification(user_input, answer)

                if progress:
                    instance = 0
                else:
                    instance = 1
                    BU.clean_box()
        
    else:
        input_boxes = [input_box12]

        for box in input_boxes:
            box.update()

        for box in input_boxes:
            box.draw(screen)

        

        for event in pyg.event.get():
            for box in input_boxes:
                box.handle_event(event)
                user_input = BoxerUnboxer.final_input

                progress = Verification.verification(user_input, answer)

                if progress:
                    instance = 1
                else:
                    instance = 2
                    BU.clean_box()
                    
    pyg.display.flip()

for event in pyg.event.get():
    if event.type == pyg.QUIT:
        instance += 1
