"""
My amazing robot!
"""

import random

# Get the robot's name from the user
name = input('What is the name of the robot?')

# Set ID for the robot
identifier = 2628

# Maximum number of grid cells (rows and columns)
grid_size = 10

# Maximum row and column indices
max_row = grid_size - 1
max_col = grid_size - 1

# Generate random initial coordinates for the robot
row_co = random.randint(0, max_row)
col_co = random.randint(0, max_col)

# Generate a random moving direction for the robot
init_dir = random.choice(['n','s','w','e'])

# Clip the coordinates to be inside the grid
if row_co < 0:
    row_co = 0
elif row_co > max_row:
    row_co = max_row
if col_co < 0:
    col_co = 0
elif col_co > max_col:
    col_co = max_col

# Compute the quadrant
if 0 <= row_co <= max_row // 2:
    row_quadrant = "top"
else:
    row_quadrant = "bottom"

if 0 <= col_co <= max_col // 2:
    col_quadrant = "left"
else:
    col_quadrant = "right"

quadrant = f"{row_quadrant} {col_quadrant}"

# Generate a string representation for the direction, for printing
if init_dir == "n":
    direction_string = "North"
elif init_dir == "s":
    direction_string = "South"
elif init_dir == "e":
    direction_string = "East"
elif init_dir == "w":
    direction_string = "West"

# The robot talks!
print(f"Hello. My name is {name}. My ID is {identifier}.")
print(f"My current location is ({row_co}, {col_co}). I am in the {quadrant} quadrant.")
print(f"I am facing {direction_string}.")

# Move the robot one step forward
print("Moving one step forward.")

if init_dir == "n":
    if row_co > 0:
        row_co = row_co - 1
if init_dir == "s":
    if row_co < grid_size - 1:
        row_co = row_co + 1
if init_dir == "w":
    if col_co > 0:
        col_co = col_co - 1
if init_dir == "e":
    if col_co < grid_size - 1:
        col_co = col_co + 1

# Update the quadrant
if 0 <= row_co <= max_row // 2:
    row_quadrant = "top"
else:
    row_quadrant = "bottom"

if 0 <= col_co <= max_col // 2:
    col_quadrant = "left"
else:
    col_quadrant = "right"

quadrant = f"{row_quadrant} {col_quadrant}"

# Print the updated location and quadrant
print(f"My current location is ({row_co}, {col_co}). I am in the {quadrant} quadrant.")
