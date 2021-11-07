class Line:

    # Sets default line attributes. Line from (0, 0) to (0, 0) and no legend text
    def __init__(self, x=[0, 0], y=[0, 0], text=" ", extremes=[0, 0]):
        self.x_coordinates = x
        self.y_coordinates = y
        self.line_text = text
        self.extreme_heights = extremes

    # Retrieves X-Coordinates of Line object
    def get_x_coordinates(self):
        return self.x_coordinates

    # Retrieves Y-Coordinates of Line object
    def get_y_coordinates(self):
        return self.y_coordinates

    # Retrieves X-Coordinates of Line object
    def get_plot_text(self):
        return self.line_text

    def get_extreme_heights(self):
        return self.extreme_heights

    # Creates X coordinates
    def create_x_coordinates(self, previous_x, new_x):
        self.x_coordinates = [previous_x, new_x + previous_x]  # Adds new distance change to previous distance

    # Creates Y Coordinates
    def create_y_coordinates(self, previous_y, new_y):
        self.y_coordinates = [previous_y, new_y + previous_y]  # Adds new height change to previous height

    # Creates plot legend text
    def create_legend(self, height_change, length, angle, grade):
        self.line_text = ('Elevation change: ' + str(height_change) + ' Feet\n' +
                          'Trail Length: ' + str(length) + ' Miles\n' +
                          'Incline Angle: ' + str(angle) + ' Degrees\n' +
                          'Grade: ' + str(grade) + '%')

    # Creates extreme limits attribute
    def create_extremes(self, height, previous_min, previous_max):
        if height < previous_min:
            min_height = height
        else:
            min_height = previous_min

        if height > previous_max:
            max_height = height
        else:
            max_height = previous_max

        self.extreme_heights = [min_height, max_height]
