from gui_init import *


# Gets direct inputs from Entry boxes
def get_inputs():
    height_change = change.get()  # Elevation change from user
    trail_distance = distance.get()  # Trail Length from user
    return height_change, trail_distance


# Verifies if input is numeric
def isNumber(number):
    no_decimal_string = str(number).replace(".", "",
                                            1)  # removes first decimal point, which would be considered not a digit

    if no_decimal_string[0] == '-':  # If first character is a negative sign
        check_string = no_decimal_string.replace('-', '', 1)  # Remove negative sign, assign to check string
    else:  # If first character is not negative sign
        check_string = no_decimal_string  # assign no_decimal_string to check_string

    if check_string.isdigit():  # If check_string is only numbers (no special chracters or letter)
        return True
    else:
        return False


# Checks condition of isNumber and updates status text if inputs are not numbers
def verify_isNumber(elevation_change, trail_length):
    if isNumber(elevation_change) is False or isNumber(trail_length) is False:  # If either input is non-numeric
        status_text["text"] = "Non numeric input.\nPlease enter a numeric input"  # Change status function
        return False
    else:
        return True


# Gets inputs from Entry boxes and converts them to floats
def convert_inputs():
    height_change = float(change.get())  # Elevation change from user
    trail_distance = float(distance.get())  # Trail Length from user
    return height_change, trail_distance
