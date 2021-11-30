from line_creation import *

coordinate_list = []
increment_coordinate = []


# Creates increment coordinate, which is the increment in both directions
def create_increment_coordinate(start_lat, start_lon, end_lat, end_lon, increment):
    lat_increment = calculate_increment(start_lat, end_lat, increment)  # Calculates latitude increment
    lon_increment = calculate_increment(start_lon, end_lon, increment)  # Calculates longitude increment

    increment_coordinate.append(lat_increment)
    increment_coordinate.append(lon_increment)


# Removes the last coordinate if it is within 0.00001 degrees of 2nd to last coordinate
def trim(end_lat, end_lon):
    if end_lat - coordinate_list[len(coordinate_list) - 1][0] >= 0.00001 or end_lon - \
            coordinate_list[len(coordinate_list) - 1][0] >= 0.00001:
        coordinate_list.pop()


# Sets list of coordinates to plot
def set_coordinate_list(start_lat, start_lon, end_lat, end_lon):
    new_coordinate = [start_lat, start_lon]

    while True:
        coordinate_list.append(new_coordinate)  # Append new coordinate
        new_coordinate = [a + b for a, b in
                          zip(new_coordinate, increment_coordinate)]  # Add increment coordinate to current coordinate

        if not isPositive(increment_coordinate[0]):  # If latitude increment is negative
            if new_coordinate[0] <= end_lat:
                break  # break if new latitude is less than the end latitude
        else:  # If latitude increment is positive
            if new_coordinate[0] >= end_lat:
                break  # break if new latitude is greater than end latitude

        if not isPositive(increment_coordinate[1]):  # If longitude increment is negative
            if new_coordinate[1] <= end_lon:  # break if new longitude is less than the end longitude
                break
        else:  # If longitude increment is positive
            if new_coordinate[1] >= end_lon:
                break  # break if new longitude is greater than end longitude

    coordinate_list.append([end_lat, end_lon])  # Append end coordinate to coordinate list
    trim(end_lat, end_lon)  # remove if coordinate list already has end coordinate


def create_coordinate_list():
    start_lat, start_lon, end_lat, end_lon = get_coordinates()  # Get coordinate inputs
    increment = increment_box.get()  # Get increment input

    if verify_numeric_coordinates([start_lat, start_lon, end_lat, end_lon]) and verify_numeric_increment(
            increment):  # if inputs are numeric

        start_lat, start_lon, end_lat, end_lon, increment = convert_coordinate_inputs(start_lat, start_lon, end_lat,
                                                                                      end_lon,
                                                                                      increment)  # Convert to floats

        if verify_latitude(start_lat) and verify_latitude(end_lat) and verify_longitude(start_lon) and verify_longitude(
                end_lon) and verify_increment(increment):  # If inputs are within range

            set_initial_height(calculate_elevation(
                format_coordinates(str(start_lat), str(start_lon))))  # initializes height as elevation in feet from API

            create_increment_coordinate(start_lat, start_lon, end_lat, end_lon,
                                        increment)  # Creates increment coordinate

            set_coordinate_list(start_lat, start_lon, end_lat, end_lon)  # Creates list
        else:
            return  # exit function if inputs are out of range
    else:
        return  # exit function if inputs are non numeric


def create_coordinate_line(lat, lon):
    elevation = calculate_elevation(format_coordinates(str(lat), str(lon)))  # Calculate elevation with API

    elevation_change = elevation - get_previous_y(line_stack)[1]  # Calculate change in elevation from previous line
    # in feet
    horizontal_change = 5280 * calculate_increment_distance(
        increment_coordinate)  # Calculates horizontal change in feet

    trail_length_ft = calculate_trail_length(horizontal_change,
                                             elevation_change)  # Calculates trail length (hypotenuse)
    incline_rad, incline_deg, grade = calculate_angle(elevation_change,
                                                      trail_length_ft)  # Calculates angle in different forms

    new_line = Line()  # Line instance

    new_line.create_x_coordinates(get_previous_x(line_stack)[1], horizontal_change)  # Determines new lines
    # X-coordinates.
    new_line.create_y_coordinates(get_previous_y(line_stack)[1], elevation_change)  # Determines new lines
    # Y-coordinates.
    new_line.create_legend(round(elevation_change, 2), round(trail_length_ft / 5280, 2), incline_deg,
                           grade)  # Creates legend given calculated data

    new_line.create_extremes(new_line.get_y_coordinates()[1], get_previous_min_height(line_stack),
                             get_previous_max_height(line_stack))  # Creates extreme heights

    line_stack.append(new_line)  # Pushes new_line to line_stack

    status_text_2["text"] = "Plot displayed in new window"

    return new_line
