from plot_ops import *
from coordinates import *


# Adds line to plot
def add():
    line = create_line()  # Creates line
    if line:  # If line is created successfully
        plot(line)  # Plot line
    plt.show()


def calculate():
    create_coordinate_list()  # Create list of coordinates to plot
    for index, point in enumerate(coordinate_list[1:]):  # For each coordinate (except for the first)
        line = create_coordinate_line(point[0], point[1])  # Create a coordinate line
        plot(line)  # Plot the line
    plt.show()  # Display the plot


# Removes line from both stacks, and returns line so it can be removed
def pop_line():
    line_stack.pop()  # pop line from line_stack
    line_to_remove = plotted_line_stack.pop()  # pop line from plotted_line_stack and assign to Line variable
    return line_to_remove


# Removes line from plot
def remove_line(input_line):
    line = input_line.pop(0)
    line.remove()  # Removes line from plot


# Removes legend from plot
def remove_legend():
    plt.legend().remove()  # removes legend (will remove legends of all lines)
    plt.legend()  # re-adds legend of displayed lines


# Removes line and legend from plot and displays updated plot
def remove():
    # First line in stack is a place holder
    if len(plotted_line_stack) >= 3:  # If 2 or more lines in stack
        line_to_remove = pop_line()  # Pop line from both stacks
        remove_line(line_to_remove)  # Remove line
        remove_legend()  # Remove most recent legend text
    elif len(plotted_line_stack) == 2:  # If only one line in stack
        pop_line()  # Pop line from both stacks
        plt.clf()  # Clear plot
    else:  # If no lines in stack
        status_text["text"] = "Plot is empty!"  # Update status text
        status_text_2["text"] = "Plot is empty!"  # Update status text

    plt.show()  # Display plot


# Recalculates most recently plotted line
def recalculate():
    if len(plotted_line_stack) >= 2:  # If there is at least one line in stack
        remove()  # Remove most recent line
    add()  # Add line using current values in Entry boxes


def reset():
    # Remove all lines from plotted_line_stack, except default
    while len(plotted_line_stack) > 1:
        remove()

    # Remove all lines from line_stack, except default
    while len(line_stack) > 1:
        line_stack.pop()

    # Clear coordinate_list
    while len(coordinate_list) != 0:
        coordinate_list.pop()

    line_stack[0] = default_line  # Reset default line values

    # Update status text on both tabs
    status_text["text"] = "Enter a valid input:\n1. Both inputs must be numeric\n2. Elevation change must not exceed " \
                          "Distance "
    status_text_2["text"] = "Enter 2 valid coordinates and\nnumber of increments to plot"
