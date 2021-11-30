from calculations import *
from gui_data import *
from stacks import *


# Formats inputs into floats and converts trail length to feet
def format_inputs():
    elevation_change, trail_length = convert_inputs()  # Converts string inputs of Entry boxes to floats
    trail_length_ft = mile_to_feet(trail_length)  # Converts trail length to feet
    return elevation_change, trail_length_ft


# Initializes height by setting the second y coordinate of the default line in line_stack
def set_initial_height(height):
    line_stack[0].y_coordinates = [0, height]  # sets new y coordinate for default line
    if height > 0:
        line_stack[0].extreme_heights = [0, height]  # sets new extreme max height if greater than 0
    if height < 0:
        line_stack[0].extreme_heights = [height, 0]  # sets new extreme min height if less than 0


# Creates/returns Line object and pushes Line object to line_stack
def create_line():
    elevation_change, trail_length = get_inputs()  # Retrieves string inputs of Entry boxes

    if not verify_isNumber(elevation_change, trail_length):
        return  # Exit function

    elevation_change, trail_length_ft = format_inputs()

    if verify_values(elevation_change, trail_length_ft):  # If inputs are valid
        status_text["text"] = "Plot displayed in new window"  # Change status text

        incline_rad, incline_deg, grade = calculate_angle(elevation_change, trail_length_ft)
        horizontal_distance = calculate_horizontal_distance(elevation_change, incline_rad)

        new_line = Line()

        new_line.create_x_coordinates(get_previous_x(line_stack)[1], horizontal_distance)  # Determines new lines
        # X-coordinates.
        new_line.create_y_coordinates(get_previous_y(line_stack)[1], elevation_change)  # Determines new lines
        # Y-coordinates.
        new_line.create_legend(elevation_change, trail_length, incline_deg,
                               grade)  # Creates legend given calculated data

        new_line.create_extremes(new_line.get_y_coordinates()[1], get_previous_min_height(line_stack),
                                 get_previous_max_height(line_stack))

        line_stack.append(new_line)  # Pushes new_line to line_stack

        return new_line


