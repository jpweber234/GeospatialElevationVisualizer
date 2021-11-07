from matplotlib import pyplot as plt
import numpy as np
from stacks import *


# Checks is minimum height is negative
def min_is_Negative(y_minimum):
    if y_minimum < 0:
        return True
    else:
        return False


# Sets plot limits
def plot_limits(x_limit, y_limits):
    plt.xlim(0, x_limit + 500)  # Sets X-axis limit
    if min_is_Negative(y_limits[0]):  # If lower y_limit is negative
        plt.ylim(y_limits[0] - 500, y_limits[1] + 500)  # PLot from 500 below min, to 500 above max
    else:
        plt.ylim(y_limits[0], y_limits[1] + 500)  # Plot from 0 to 500 above max


# Creates scalable axes, and places axis labels and tick marks
def set_axes(x_limit, y_limits):
    plt.gca().set_aspect('equal', adjustable='box')  # Boxes will adjust to remain to scale

    tick = np.arange(0, x_limit, 528).tolist()  # X-Axis tick mark locations
    x_label = np.arange(0, (x_limit / 5280), 0.1).tolist()  # X-axis tick labels

    label_string = ['%2f' % round(num, 2) for num in x_label]  # Rounds x_labels calculation above to 2 decimal places

    for i, v in enumerate(label_string):
        label_string[i] = v[0:3]  # Forces labels on X-Axis to display no more than 2 decimal places

    plt.xlabel('Horizontal Distance')  # X-axis Title
    plt.xticks(tick, label_string, fontsize=7, weight='bold')  # Plots X-axis

    plt.ylabel('Elevation change')  # Y-axis Title
    if min_is_Negative(y_limits[0]):
        plt.yticks(np.arange(y_limits[0] - 500, y_limits[1] + 500, 500).tolist(), fontsize=7,
                   weight='bold')  # Plots Y-axis ticks from 500 below min, to 500 above max
    else:
        plt.yticks(np.arange(y_limits[0], y_limits[1] + 500, 500).tolist(), fontsize=7,
                   weight='bold')  # Plots Y-axis from 0, to 500 above max


# Plots graph
def plot(line):
    plt.style.use('ggplot')  # Adds gridlines

    plt.title('Trail Steepness Visualization')  # Sets plot title

    x_limit = line.get_x_coordinates()[1]  # X-axis limit
    y_limits = line.get_extreme_heights()

    plot_limits(x_limit, y_limits)
    set_axes(x_limit, y_limits)

    plot_line = plt.plot(line.get_x_coordinates(), line.get_y_coordinates(),
                         label=line.get_plot_text())  # Creates line to plot with associated plot text
    plotted_line_stack.append(plot_line)  # add plotted line to plotted line stack

    plt.legend()  # Displays legend
    plt.show()  # Shows plot
