# This is to ease my confusion, may or may not be included in the documentation
# This is a demo of the game done purely in python without and external aid from Pygame

import random
playing = "y"
while playing == "y":
    instance = 0
    r1 = random.randint(10, 99)
    r2 = random.randint(10, 99)
    true_ans = r1 * r2
    while instance == 0:
        print("{} * {} = {}".format(r1, r2, true_ans))
        user_input = int(input("What is the answer to the problem?"))

        if user_input == true_ans:
            playing = False
        else:
            print("Not correct, let's try a different method called L.O.I.F.")
            instance = instance + 1

    while instance == 1:
        print("The first thing we need to do is isolate the last integer of both integers")
        last_first = int(r1/10)
        last_second = int(r2/10)

        print("The last digit of the first integer is {} and the first digit of the second integer is {}"
              .format(last_first, last_second))

        print("Next we multiply these two numbers together")
        ans = last_first * last_second

        print("{} * {} = {}".format(last_first, last_second, ans))

        l_user_input = input("So what is the answer to this problem")
        answering = True
        while answering:
            if l_user_input == ans:
                print("Good moving on to the next one")
                answering = False
            elif l_user_input != ans:
                print()


print("Correct")
playing = input("Would you like to play again? (y/n)")
