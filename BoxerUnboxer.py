"""
This script takes the integer in the box and the place for the box (10th, 100th etc.)
and then adds the actual integer to the final result. The final result can then be called as a script
variable. The second function of this script is to clean the value of the final result, for future use.
"""

# return holder, global as to be a property of the script (class property)
final_input = 0


# This function takes the integer in the box and the place of the box then evaluates what to return
def boxer(packaged_integer, box_power):
    # Initialization
    integer = int(packaged_integer)
    place = box_power
    power = 0

    # Analyze place to give power
    if place == 0:
        power = 1000
    elif place == 1:
        power = 100
    elif place == 2:
        power = 10
    elif place == 3:
        power = 1

    # Compute for result using integer and power
    result = integer * power

    # Take global variable final_input
    global final_input
    # Add computed value to global result
    final_input += result


# Clean global value final_input
def clean_box():
    global final_input
    final_input = 0
