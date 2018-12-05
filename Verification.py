# Calculation fo the actual value given by the user and giving of the integer
final_value = 0


# Takes an array
# Used the compile the value of the array given to it into on integer defined globally
def calculation(user_input):
    global final_value
    # Check if they are equal and returns a bool
    for i in user_input:
        final_value = final_value + i

    print(final_value)


# Takes two integers, compares the first to the second and returns the evaluation
def verification(actual, expected):
    # print("Verifying")
    if actual == expected:
        return True
    else:
        return False


# Resets the value of the global final_value
def reset():
    global final_value
    final_value = 0
    # print("Reset complete")
