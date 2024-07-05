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
direction_index = random.randint(0, 3)
if direction_index == 0:
    direction = "n"
elif direction_index == 1:
    direction = "e"
elif direction_index == 2:
    direction = "s"
else:
    direction = "w"

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
if direction == "n":
    direction_string = "North"
elif direction == "s":
    direction_string = "South"
elif direction == "e":
    direction_string = "East"
elif direction == "w":
    direction_string = "West"

# The robot talks!
print(f"Hello. My name is {name}. My ID is {identifier}.")

# Moving the robot until it hits the cell that has Ribena:
while (row_co != 9) or (col_co != 9):
    # Moving the robot all the way to the grid's edge and change the direction by 90 degrees clockwise when it hits the edge.
    if direction == "n":
        while row_co > 0:
            print(f"I am currently at ({row_co}, {col_co}), facing {direction_string}.")
            # Move the robot one step forward
            print("Moving one step forward.")
            row_co = row_co - 1

    if direction == "s":
        while row_co < grid_size - 1:
            print(f"I am currently at ({row_co}, {col_co}), facing {direction_string}.")
            # Move the robot one step forward
            print("Moving one step forward.")
            row_co = row_co + 1

    if direction == "w":
        while col_co > 0:
            print(f"I am currently at ({row_co}, {col_co}), facing {direction_string}.")
            # Move the robot one step forward
            print("Moving one step forward.")
            col_co = col_co - 1

    if direction == "e":
        while col_co < grid_size - 1:
            print(f"I am currently at ({row_co}, {col_co}), facing {direction_string}.")
            # Move the robot one step forward
            print("Moving one step forward.")
            col_co = col_co + 1

    if row_co == 9 and col_co == 9 :
        break

    # Robot's talking:
    print(f"I am currently at ({row_co}, {col_co}), facing {direction_string}.")
    print("I have a wall in front of me.")

    # Turning the robot:
    print("Turning 90 degrees clockwise.")
    # Fancy solution: add one to direction index above to move to the next clockwise direction
    # Use modulus to get the number to cycle back to 0 if the number is more than 3 (so (3+1) % 4 == 0)
    direction_index = (direction_index + 1) % 4  # actually ignoring %4 is also alright
    if direction_index == 0:
        direction = "n"
        direction_string = "North"
    elif direction_index == 1:
        direction = "e"
        direction_string = "East"
    elif direction_index == 2:
        direction = "s"
        direction_string = "South"
    else:
        direction = "w"
        direction_string = "West"

print(f"I am currently at ({row_co}, {col_co}), facing {direction_string}.")
print(f"I am drinking Ribena! I am happy!")



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
#print(f"My current location is ({row_co}, {col_co}). I am in the {quadrant} quadrant.")
