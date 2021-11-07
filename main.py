from button_ops import *

# Creates add button, which adds a line to the plot
add_button = Button(root, text="Add", height=2, width=20, command=add)
add_button.grid(row=1, column=0, padx=10, pady=10)

# Creates remove button, which removes most recently added line from plot
remove_button = Button(root, text="Remove", height=2, width=20, command=remove)
remove_button.grid(row=2, column=0, padx=10, pady=10)

# Creates recalculate button, which recalculates most recently added line based on new inputs
recalculate_button = Button(root, text="Recalculate", height=2, width=20, command=recalculate)
recalculate_button.grid(row=3, column=0, padx=10, pady=10)

# Tkinter main loop
root.mainloop()
