# IMPORTATIONS


import math


# CALCUlATE THE NUMBER RECEIVED


def equation(eq_x):
    return (eq_x ** 3) + (5 * math.sin(eq_x)) + (2 * eq_x) + 4


# VERIFY IF THE SIGNS OF THE NUMBERS ARE DIFFERENT


def opposite_signs(vs_x, vs_y):
    if equation(vs_x) * equation(vs_y) < 0:
        return True
    else:
        return False


# DECLARATIONS OF SOME SIMPLE VARIABLES TO MAKE CODE WORK

selection, sub_selection, x, y = 0, True, 0, 0

# LOOP TO MAKE THE USER MAY CALCULATE HOW MANY VALUES THAT HE WANT

while selection == 0:

    # RECEIVE THE VALUES OF USER INPUT WITH A SIMPLE LOOP

    while sub_selection:
        x = float(input("\033[1;34m\nType X Value: "))
        y = float(input("\033[1;34mType Y Value: "))
        if x == y:  # VERIFY IF THE POINTS ARE EQUAL
            print("\033[1;31m\nThe values must be different, please type new values!")
        elif not opposite_signs(x, y):  # VERIFY IF THE POINTS RECEIVED HAVE OPPOSITE SIGNS
            print("\033[1;31m\nThis interval don't have valid points, please type new values!")
        else:
            break

    # STORES THE ORIGINAL VALUES FOR LATER USE

    original_x, original_y = x, y

    # IF THE VALUES ARE TYPED IN WRONG ORDER SWITCH THEM

    if x > y:
        x, y = y, x

    # LOOP TO CALCULATE INTERVAL MULTIPLE TIMES UNTIL REACH THE INTERVAL OF 0.1 BETWEEN THE POINTS

    while y - x >= 0.1:

        # DEFINE A MEAN BETWEEN THE TWO POINTS

        mean = (x + y) / 2

        if opposite_signs(mean, x):  # IF THE POINT IS ON THE INTERVAL OF X AND MEAN
            y = mean
        else:  # IF THE POINT IS ON THE INTERVAL OF MEAN AND Y
            x = mean

    # PRINT THE CALCULATED DATA

    print(f"\033[1;32m\nF({original_x}) = {equation(original_x):.3f}\nF({original_y}) = {equation(original_y):.3f}\n\n"
          f"The Interval Of This Functions Is: [{x:.5f}, {y:.5f}]\n")

    selection = int(input("\033[1;34mType 0 To Calculate Another Interval Or Anything To Exit The Program: "))
