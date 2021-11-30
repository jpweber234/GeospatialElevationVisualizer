from tkinter import *
import tkinter as tk
from tkinter import ttk

# Creates Tkinter window
root = tk.Tk()
root.title("Incline Visualizer")
tabControl = ttk.Notebook(root)

# Creates 2 tabs
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tab_array = [tab1, tab2]

# Sets tab names
tabControl.add(tab1, text='Elevation and Distance')
tabControl.add(tab2, text='Coordinates')
tabControl.pack(expand=1, fill="both")

# TAB 1

# input fields
change = ttk.Entry(tab1, width=25)  # Elevation change input box
distance = ttk.Entry(tab1, width=25)  # Trail Distance input box

# Default text for above input fields
change.insert(0, "Enter Elevation Change (ft)")
distance.insert(0, "Enter Distance (miles)")

# Input field locations
change.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
distance.grid(row=0, column=1, columnspan=2, padx=10, pady=10)

# Status Text
status_text = ttk.Label(tab1, text="Enter a valid input:\n"
                                   "1. Both inputs must be numeric\n"
                                   "2. Elevation change must not exceed Distance", justify=LEFT)
status_text.grid(row=2, column=2, padx=10, pady=10)

# TAB 2

# Input fields
latitude_1 = ttk.Entry(tab2, width=25)  # Starting latitude input box
longitude_1 = ttk.Entry(tab2, width=25)  # Starting longitude input box
latitude_2 = ttk.Entry(tab2, width=25)  # Ending latitude input box
longitude_2 = ttk.Entry(tab2, width=25)  # Ending longitude input box
increment_box = ttk.Entry(tab2, width=25)  # Increment number input box

# Default text for above input fields
latitude_1.insert(0, "Enter Starting Latitude")
longitude_1.insert(0, "Enter Starting Longitude")
latitude_2.insert(0, "Enter Ending Latitude")
longitude_2.insert(0, "Enter Ending Longitude")
increment_box.insert(0, "Enter Increment Number")

# Input field locations
latitude_1.grid(row=0, column=2, columnspan=2, padx=10, pady=10)
longitude_1.grid(row=1, column=2, columnspan=2, padx=10, pady=10)
latitude_2.grid(row=2, column=2, columnspan=2, padx=10, pady=10)
longitude_2.grid(row=3, column=2, columnspan=2, padx=10, pady=10)
increment_box.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Status text
status_text_2 = ttk.Label(tab2, text="Enter 2 valid coordinates and\n"
                                     "number of increments to plot", justify=LEFT)
status_text_2.grid(row=0, column=4, padx=10, pady=10)
