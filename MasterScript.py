# This will serve as the main game loop for our multiplication operation problems
# Much of this will be placeholder

import pygame as pyg
from random import randint as rin

r2 = rin(10, 99)
r1 = rin(10, 99)

true_ans = r1 * r2

print(r1, "*", r2, "=", true_ans)

if true_ans >= 1000:
    print("Now spawning 4 boxes")

else:
    print("Now spawning 3 boxes")

"Begin the LOIF part of the script"
