# Initialization of all functions
# L
import pygame as pyg
pyg.init()
number_font = pyg.font.Font(None, 24)


# Render L
def begin_l(integer_1, integer_2):
    last_digit_1 = integer_1 % 10
    last_digit_2 = integer_2 % 10

    l_string = number_font.render("L problem: {} * {} = ".format(last_digit_1, last_digit_2),
                                  True, (255, 192, 203))

    return l_string


# Render O
def begin_2(integer_1, integer_2):
    first_digit_1 = int(integer_1/10)
    last_digit_2 = integer_2 % 10
    ans = first_digit_1 * last_digit_2

    o_string = number_font.render("O problem: {} * {} = ".format(first_digit_1, last_digit_2, ans),
                                  True, (255, 0, 0))

    return o_string


# Render I
def begin_3(integer_1, integer_2):
    last_digit_1 = integer_1 % 10
    first_digit_2 = int(integer_2 / 10)
    ans = last_digit_1 * first_digit_2

    i_string = number_font.render("I problem: {} * {} = ".format(last_digit_1, first_digit_2, ans),
                                  True, (135, 206, 250))

    return i_string


# Render F
def begin_4(integer_1, integer_2):
    first_digit_1 = int(integer_1 / 10)
    first_digit_2 = int(integer_2 / 10)
    ans = first_digit_1 * first_digit_2

    f_string = number_font.render("F problem: {} * {} = ".format(first_digit_1, first_digit_2, ans),
                                  True, (255, 255, 0))

    return f_string


# Compute L
def step_1(integer_1, integer_2):
    last_digit_1 = integer_1 % 10
    last_digit_2 = integer_2 % 10
    ans = last_digit_1 * last_digit_2

    return ans


# Compute O
def step_2(integer_1, integer_2):
    first_digit_1 = int(integer_1/10)
    last_digit_2 = integer_2 % 10
    ans = first_digit_1 * last_digit_2

    return ans


# Compute I
def step_3(integer_1, integer_2):
    last_digit_1 = integer_1 % 10
    first_digit_2 = int(integer_2 / 10)
    ans = last_digit_1 * first_digit_2

    return ans


# Compute F
def step_4(integer_1, integer_2):
    first_digit_1 = int(integer_1 / 10)
    first_digit_2 = int(integer_2 / 10)
    ans = first_digit_1 * first_digit_2

    return ans

