final_input = 0


def boxer(packaged_integer, box_power):
    integer = int(packaged_integer)
    place = box_power
    power = 0

    if place == 0:
        power = 1000
    elif place == 1:
        power = 100
    elif place == 2:
        power = 10
    elif place == 3:
        power = 1

    result = integer * power

    global final_input
    final_input += result


def clean_box():
    global final_input
    final_input = 0
