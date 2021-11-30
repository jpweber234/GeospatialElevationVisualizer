from gui_init import *
import requests


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


# Retrieves coordinate inputs from entry boxes
def get_coordinates():
    return latitude_1.get(), longitude_1.get(), latitude_2.get(), longitude_2.get()


# Formats coordinates for input into Open Elevation API
def format_coordinates(lat, lon):  # inputs are strings
    return lat + ", " + lon  # outputs is a string


# Utilizes Open Elevation API to retrieve elevation for a given geographic coordinate
def get_elevation(payload):
    r = requests.get('https://api.open-elevation.com/api/v1/lookup?', params={"locations": payload})
    return r.json()["results"][0]["elevation"]  # returns elevation in meters as a string


# Returns elevation in feet as a float rounded to 2 decimal places
def calculate_elevation(coordinate):
    return round(float(get_elevation(coordinate) * 3.28084), 2)


# Verifies that coordinates are numeric, and updates status text if not
def verify_numeric_coordinates(coordinates):
    for coordinate in coordinates:
        if not isNumber(coordinate):
            status_text_2["text"] = "Latitude and Longitude coordinates\nmust be numeric values"
            return False
    return True


# Verifies that increment is numeric, and updates status text if not
def verify_numeric_increment(increment):
    if not isNumber(increment):
        status_text_2["text"] = "Increment must be numeric value"
        return False
    return True


# Verifies latitude is between -90 and 90 degrees, and updates status text if not
def verify_latitude(latitude):
    if abs(latitude) > 90:
        status_text_2["text"] = "Latitude must be between -90 and 90 degrees"
        return False
    return True


# Verifies latitude is between -180 and 180 degrees, and updates status text if not
def verify_longitude(longitude):
    if abs(longitude) > 180:
        status_text_2["text"] = "Longitude must be between -180 and 180 degrees"
        return False
    return True


# Limits size of increment to between 1 and 16, and updates status text if outside this range
def verify_increment(increment):
    if increment > 16:
        status_text_2["text"] = "Increment must be less than 16"
        return False
    elif increment <= 0:
        status_text_2["text"] = "Increment must be at least 1"
        return False
    return True
