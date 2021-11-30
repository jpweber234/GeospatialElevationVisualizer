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


# Converts degrees to radians
def convert_to_radians(degrees):
    return math.radians(degrees)


# Calculates distance between 2 geographic coordinates using Haversine formula
def calculate_distance(lat1, lon1, lat2, lon2):
    delta_lat = convert_to_radians((lat2 - lat1) / 2)
    delta_lon = convert_to_radians((lon2 - lon1) / 2)

    a1 = math.sin(delta_lat) * math.sin(delta_lat)
    a2 = math.cos(lat2) * math.cos(lat1) * math.sin(delta_lon) * math.sin(delta_lon)
    a = a1 + a2

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return 3958.8 * c  # Returns distance in miles as a float


# Used to convert Entry box inputs in the Coordinate Tab to floats
def convert_coordinate_inputs(num1, num2, num3, num4, num5):
    return float(num1), float(num2), float(num3), float(num4), float(num5)


# Calculates increment in degrees
def calculate_increment(start, end, increment):
    return (end - start) / increment


# Calculates increment distance in miles
def calculate_increment_distance(coordinate):
    return calculate_distance(coordinate[0], coordinate[1], 0, 0)


# Calculates trail length given horizontal and vertical components (Pythagorean theorem)
def calculate_trail_length(a, b):
    return math.sqrt(pow(a, 2) + pow(b, 2))
