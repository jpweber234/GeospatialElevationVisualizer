# InclineCalculator

The idea for this project came from my love of hiking, but frustration over how trail steepness is described. Many people will say "This trail gains 3000 feet over 2 miles", which I find difficult to understand. This visualizer attempts to solve this problem. 

The user inputs an Elevation Change (in feet, can be negative), and a Trail Length (in miles, should not be negative). When a user adds the line to the plot by clicking the "Add" button, the program calculates the horizontal ("birds eye") distance, and plots a line from the current starting point to the new coordinate given by (horizontal distance, elevation change). The program also calculates the incline angle (degrees) and grade of the incline, both of which are displayed on the plot. The user has the ability to add multiple lines to the plot by continuing to click the "Add" button, but can also remove lines from the plot via the "Remove" button, or recalculate the most recently plotted line via the "Recalculate" button.

The GUI was made using the Tkinter framework, and consists of two entry boxes for Elevation Change and Trail Distance, three buttons for adding, removing, and recalculating lines, and a Status Text box, which provides error messages and other instructions. The plot was made using matplotlib. 
