# This will serve as the main game loop for our multiplication operation problems
# Much of this will be placeholder

import random as rand

playing = 'y'
while playing == 'y':
    user_input = 0
    var_1 = rand.randint(10, 99)
    var_2 = rand.randint(10, 99)
    answer = 0

    true_answer = (var_1 * var_2)
    try_left = 3  # Arbitrary
    while answer != true_answer and try_left != 0:
        if try_left == 3:
            print("The problem:")
            print(var_1, "*", var_2, "= ?")
            answer = int(input("Please give your answer \n"))

        elif try_left == 2:
            print("This is a hint, it means you have two tries left.")
            print(var_1, "*", var_2, "= ?")
            answer = int(input("Please give your answer \n"))

        elif try_left == 1:
            print("This is the answer,", true_answer, "it means that you only have one try left")
            print(var_1, "*", var_2, "= ?")
            answer = int(input("Please give your answer \n"))

        else:
            print("This shouldn't happen")

        try_left -= 1

    if answer == true_answer:
        print("Congrats you go it")
    else:
        print("Nope, not even")

    playing = input("Do you want to play again? y/n \n")
