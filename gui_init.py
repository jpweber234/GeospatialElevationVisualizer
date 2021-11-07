from tkinter import *

# Creates Tkinter window
root = Tk()
root.title("Incline Visualizer")

# input fields
change = Entry(root, width=25, borderwidth=5)  # Elevation change input box
distance = Entry(root, width=25, borderwidth=5)  # Trail Distance input box

# Default text for above input fields
change.insert(0, "Enter Elevation Change (ft)")
distance.insert(0, "Enter Distance (miles)")

# Input field locations
change.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
distance.grid(row=0, column=2, columnspan=2, padx=10, pady=10)

#  Status Text
status_text = Label(root, text="Enter a valid input:\n"
                               "1. Both inputs must be numeric\n"
                               "2. Elevation change must not exceed Distance", justify=LEFT)
status_text.grid(row=2, column=2, padx=10, pady=10)
