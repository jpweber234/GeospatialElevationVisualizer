from button_ops import *

# TAB 1 BUTTONS

# Creates add button, which adds a line to the plot
add_button = ttk.Button(tab1, text="Add", width=20, command=add)
add_button.grid(row=1, column=0, padx=10, pady=10)

# Creates remove button, which removes most recently added line from plot
remove_button = ttk.Button(tab1, text="Remove", width=20, command=remove)
remove_button.grid(row=2, column=0, padx=10, pady=10)

# Creates recalculate button, which recalculates most recently added line based on new inputs
recalculate_button = ttk.Button(tab1, text="Recalculate", width=20, command=recalculate)
recalculate_button.grid(row=3, column=0, padx=10, pady=10)

# Creates reset button, which returns all stacks and plots to their default state
reset_button = ttk.Button(tab1, text="Reset", width=20, command=reset)
reset_button.grid(row=3, column=2, padx=10, pady=10)

# TAB 2 BUTTONS

# Creates Calculate button, which plots a path between two geographic coordinates based on a given increment
calculate_button = ttk.Button(tab2, text="Calculate", width=20, command=calculate)
calculate_button.grid(row=1, column=0, padx=10, pady=10)

# Creates remove button, which removes most recently added line from plot
remove_button_2 = ttk.Button(tab2, text="Remove", width=20, command=remove)
remove_button_2.grid(row=2, column=0, padx=10, pady=10)

# Creates reset button, which returns all stacks and plots to their default state
reset_button_2 = ttk.Button(tab2, text="Reset", width=20, command=reset)
reset_button_2.grid(row=3, column=4, padx=10, pady=10)

# Tkinter main loop
root.mainloop()
