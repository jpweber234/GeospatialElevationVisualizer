import math
from gui_init import *


# Verifies that elevation change does not exceed trail length (ft) and updates status text if so
def verify_values(elevation_change, trail_length_ft):
    if trail_length_ft < abs(elevation_change):  # If elevation change exceeds trail length
        status_text["text"] = "Elevation Change must not exceed Distance"  # Change status text
        return False
    else:
        return True


# Determines if input is positive or negative (positive is greater or equal to 0)
def isPositive(num):
    if num >= 0:
        return True
    else:
        return False


# Converts miles to feet
def mile_to_feet(length):
    return length * 5280


# Calculates incline angle and grade given elevation change and trail length
def calculate_angle(elevation_change, trail_length_ft):
    incline_rad = math.asin(elevation_change / trail_length_ft)  # Calculates incline in radians
    incline_deg = round(math.degrees(incline_rad), 2)  # Converts incline angle to degrees
    incline_grade = round(((elevation_change / trail_length_ft) * 100), 2)  # Calculates incline grade
    return incline_rad, incline_deg, incline_grade


# Calculates horizontal "bird's eye" distance given elevation change and incline
def calculate_horizontal_distance(elevation_change, incline_rad):
    return round(elevation_change / math.tan(incline_rad), 2)  # Calculates horizontal distance
