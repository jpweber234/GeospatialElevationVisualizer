from line import Line

default_line = Line()  # Creates default line
line_stack = [default_line]  # Stores lines that have been created. Default line added as placeholder

default_plotted_line = Line()  # Creates default plotted line
plotted_line_stack = [
    default_plotted_line]  # Stores lines that have been plotted. Default plotted line added as placeholder


# Peeks at top item in stack
def peek_stack(stack):
    if stack:
        return stack[-1]  # this will get the last element of stack
    else:
        return None


# Retrieves X Coordinates of line at the top of the line stack
def get_previous_x(stack):
    return peek_stack(stack).get_x_coordinates()


# Retrieves X Coordinates of line at the top of the line stack
def get_previous_y(stack):
    return peek_stack(stack).get_y_coordinates()


def get_previous_min_height(stack):
    return peek_stack(stack).get_extreme_heights()[0]


def get_previous_max_height(stack):
    return peek_stack(stack).get_extreme_heights()[1]


def get_previous_latitude(stack):
    return peek_stack(stack).get_latitude()


def get_previous_longitude(stack):
    return peek_stack(stack).get_longitude()
