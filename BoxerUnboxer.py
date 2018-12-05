"""
This script takes the integer in the box and the place for the box (10th, 100th etc.)
and then adds the actual integer to the final result. The final result can then be called as a script
variable. The second function of this script is to clean the value of the final result, for future use.
"""

import Verification
# Return holder, global as to be a property of the script
final_input = [0, 0, 0, 0]
final_value = 0


# This function takes the values from the input box and calculates the value, this is then stored in an array
# This function returns an array
def boxer(packaged_integer, box_power):
    # Initialization
    integer = int(packaged_integer)
    place = box_power

    # Analyze place to give power
    if place == 0:
        final_input[0] = (integer * 1000)
    elif place == 1:
        final_input[1] = (integer * 100)
    elif place == 2:
        final_input[2] = (integer * 10)
    elif place == 3:
        final_input[3] = integer
        Verification.calculation(final_input)
    print(final_input)


def un_boxer():
    return final_value


def clear_field():
    global final_input
    final_input = [0, 0, 0, 0]
