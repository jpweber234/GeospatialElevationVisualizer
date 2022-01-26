# InclineCalculator

**\*\*UPDATE 1/25/2022: The Open Elevation API has lost its SSL Certificate, which prevents the Coordinates tab from functioning properly. To get around the verification of the SSL license, you can add "verify=False" inside the request.get() function in line 56 of gui_data.py. However, connect to the API at your own risk, since the connection may not be private\*\***

The idea for this project came from my love of hiking, but frustration over how trail steepness is described. Many people will say "This trail gains 3000 feet over 2 miles", which I find difficult to understand. This visualizer attempts to solve this problem. 

On the "Elevation and Distance" tab, the user inputs an Elevation Change (in feet, can be negative), and a Trail Length (in miles, should not be negative). When a user adds the line to the plot by clicking the "Add" button, the program calculates the horizontal ("birds eye") distance, and plots a line from the current starting point to the new coordinate given by (horizontal distance, elevation change). The program also calculates the incline angle (degrees) and grade of the incline, both of which are displayed on the plot. The user has the ability to add multiple lines to the plot by continuing to click the "Add" button, but can also remove lines from the plot via the "Remove" button, or recalculate the most recently plotted line via the "Recalculate" button.

On the "Coordinates" tab, the user inputs two geographical coordinates, and an increment number. When the user clicks the "Calculate" button, the program will use the Open Elevation API to fetch the elevations of the given coordinates, as well as at points in between the given coordinates and plot the incline angles between them. The user can also remove the most recently plotted line, and add their own lines to the plot from the first tab. 

Both tabs also have a reset button that resets the plot and all calculated data so that new values can be entered without interfering with old data.

The GUI was made using the Tkinter framework, and consists of two entry boxes for Elevation Change and Trail Distance, three buttons for adding, removing, and recalculating lines, and a Status Text box, which provides error messages and other instructions. The plot was made using matplotlib. Elevation Data from the coordinate tab was collected using the Open Elevation API.

Inital Tab 1 View:

![image](https://user-images.githubusercontent.com/92554209/144135877-60eefe0e-683c-4ade-b5d5-48f04c8bbc5b.png)


Plot of 2000 feet on a 1 mile trail from Tab 1:

![image](https://user-images.githubusercontent.com/92554209/144136094-115f543d-420e-459d-a347-19a15e96a8af.png)


Various lines added to Plot:
![image](https://user-images.githubusercontent.com/92554209/144136573-31b9e284-c656-4c15-ba35-90dc7a98fe92.png)


Initial Tab 2 View:

![image](https://user-images.githubusercontent.com/92554209/144136673-b7bd9f27-ae2a-4ae4-aefc-61b321a465a0.png)


Five increments plotted between coordinates for Mount Washington Auto Road Entrance, and Mount Washington Summit:

![image](https://user-images.githubusercontent.com/92554209/144137071-ff80c7dc-ed2e-4ed6-b9c6-a41494bbfc3d.png)



