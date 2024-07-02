import random


def load_names_from_file(filename):
    """Load the robot's name in our robot_names.txt

    Extended description of function

    Args:
        filename (str): the name of the file where you reserve the robot's name

    Returns:
        list: A list of robot's names."""
    names = []
    textfile = open(filename)
    for line in textfile:
        name = line.strip()
        names.append(name)
    return names


def robot_setup(filename, grid_size=10):
    """ Initialize the robot's name, ID, initial coordinates and direction.

    Extended description of function

    Args:
        grid_size (int): The size of the grid. Defalts to 10.
        filename (str): The name of the file where you reserve the robot's name

    Returns:
        str : Robot name
        int : Robot ID
        int : Robot's row coordinate
        int : Robot's column coordinate
        str : Robot's direction ("n", "s", "e", or "w")
    """
    names = load_names_from_file(filename)
    name = random.choice(names)
    row = random.randint(0, grid_size-1)
    col = random.randint(0, grid_size-1)
    direction = random.choice(["n", "s", "e","w"])

    return (name,row, col, direction)


def print_robot_greeting(name, id):
    """ Print the robot's greeting.

    Extended description of function

    Args:
        name (str): the name of robot
        id (str): the id of robot
    """
    return print(f"Hello. My name is {name}. My ID is {id}.")


def print_robots_greeting(name_list, id_list):
    """Print a list of several robots greeting

    Extended descriptionof function

    Args:
       name_list (list): A list of robot's names.
       id_list (list): A list of robot's indentifiers.
    """
    for index in range(len(name_list)):
        print_robot_greeting(name_list[index], id_list[index])
    return None


def direction_to_string(direction):
    """ Represent direction in string form: "North", "Sounth", "East", "West"

    Extended description of the function

    Args:
        dirction (str): Robot's direction ("n", "s", "e", or "w")

    Returns:
        str: Robot's direction in string form ("North", "Sounth", "East", "West")
    """
    if direction == "n":
        direction_string = "North"
    elif direction == "s":
        direction_string = "South"
    elif direction == "e":
        direction_string = "East"
    elif direction == "w":
        direction_string = "West"

    return direction_string


def direction_to_index(direction):
    """ Assign numbers(0,1,2,3) to each direction

    Extended description of function

    Args:
        direction (str): Dirction of the robot

    Return:
        int: the direction's corresponding index(0,1,2,3)
    """
    if direction == "n":
        direction_index = 0
    if direction == "e":
        direction_index = 1
    if direction == "s":
        direction_index = 2
    if direction == "w":
        direction_index = 3

    return direction_index


def print_robot_positon_direction(current_row,
                               current_col,
                               current_direction):
    """ Robot states its current position and next moving.

    Extended description of function

    Args:
        current_row (int): The current row coordinate of the robot.
        current_col (int): The current column coordinate of the robot.
        current_direction (str): The current dirction("n","e","s","w") of the robot.
    """
    direction_string = direction_to_string(current_direction)
    return print(f"I am currently at ({current_row}, {current_col}), facing {direction_string}.")



def moving_one_step_forward(current_row, current_col, current_direction):
    """ Move the robot one step forward

    Extended description of function

    Args:
        current_row (int): The current row coordinate of the robot.
        current_col (int): The current column coordinate of the robot.
        current_direction (str): The current dirction("n","e","s","w") of the robot.

    Returns:
        int: Robot's new row coordinate
        int: Robot's new column coordinate
    """
    print("Moving one step forward.")
    if current_direction == 'n':
        new_row = current_row - 1
        new_col = current_col
    if current_direction == 's':
        new_row = current_row + 1
        new_col = current_col
    if current_direction == 'w':
        new_col = current_col - 1
        new_row = current_row
    if current_direction == 'e':
        new_col = current_col + 1
        new_row = current_row

    return (new_row, new_col)


def rotate_90_clockwise(direction_index):
    """ Rotate the robot by 90 degrees clockwise when it hits a wall

    Extended description of function

    Args:
        direction_index (int): the corresponding index assigned to the specific direction

    Returns:
        str: Robot's direction after rotating ("n","e","s","w")
        str: direction in stirng form ("North", "East", "South","West")
    """
    print("Turn 90 degrees clockwise.")
    direction_index = (direction_index + 1) % 4
    if direction_index == 0:
        direction = "n"
    elif direction_index == 1:
        direction = "e"
    elif direction_index == 2:
        direction = "s"
    else:
        direction = "w"

    return direction


def clipping_the_coordinates(current_row, current_col, grid_size):
    """ The robot can only move insed the grid

    Extended description of function

    Args:
        current_row (int): The current row coordinate of the robot.
        current_col (int): The current column coordinate of the robot.
        grid_size (str): The size of the grid.

    Returns:
        int: The new row coordinate of the robot.
        int: The new column coordinate of the robot.
    """
    if current_row < 0:
        new_row = 0
    elif current_row > grid_size-1:
        new_row = grid_size-1
    if current_col < 0:
        new_col = 0
    elif current_col > grid_size-1:
        new_col = grid_size-1

    return (new_row, new_col)


def navigate_to_wall(current_direction,
             current_row,
             current_col,
             grid_size):
    """ Navigate the robot to until

    Extended description of function

    current_direction (str): The current dirction("n","e","s","w") of the robot.
    current_row (int): The current row coordinate of the robot.
    current_col (int): The current column coordinate of the robot.
    grid_size (str): The size of the grid.

    Returns:
        int: The new row coordinate of the robot.
        int: The new column coordinate of the robot.
    """
    if current_direction == "n":
        while current_row > 0:
            print_robot_positon_direction(current_row, current_col, current_direction)
            current_row, current_col = moving_one_step_forward(current_row, current_col, current_direction)
    if current_direction == "s":
        while current_row < grid_size-1:
            print_robot_positon_direction(current_row, current_col, current_direction)
            current_row, current_col = moving_one_step_forward(current_row, current_col, current_direction)
    if current_direction == "w":
        while current_col > 0:
            print_robot_positon_direction(current_row, current_col, current_direction)
            current_row, current_col = moving_one_step_forward(current_row, current_col, current_direction)
    if current_direction == "e":
        while current_col < grid_size-1:
            print_robot_positon_direction(current_row, current_col, current_direction)
            current_row, current_col = moving_one_step_forward(current_row, current_col, current_direction)

    print_robot_positon_direction(current_row, current_col, current_direction)

    return current_row, current_col


def navigate_to_target_position(current_row,
                                current_col,
                                current_direction,
                                target_row,
                                target_col,
                                grid_size):
    """ Navigate to out targer position. Defalts to (9, 9)

    Extended description of function

    Args:
        current_direction (str): The current dirction("n","e","s","w") of the robot.
        current_row (int): The current row coordinate of the robot.
        current_col (int): The current column coordinate of the robot.
        target_row (int): The target row coordinate. Defaults to 9.
        target_col (int): The target column coordinate. Defaults to 9.
        grid_size (str): The size of the grid.
    """
    while current_row!=target_row or current_col!=target_col:
        current_row, current_col = navigate_to_wall(current_direction, current_row, current_col, grid_size)
        if current_row==target_row and current_col==target_col:
            print("I am drinking Ribena! I am happy!")
            break
        print("I have a wall in front of me.")
        direction_index = direction_to_index(current_direction)
        current_direction = rotate_90_clockwise(direction_index)

    return None


def generate_target_row_col(name):
    """Generate taget row coordinate and column coordinate.

    Extended description of function

    Args:
        name (str): Robot's name.

    Returns:
        int: Target row coordinate.
        int: Target column coordinate
        """
    if name=='shameer':
        target_row = 0
        target_col = 0
    if name=='ruoxue':
        target_row = 0
        target_col = 9
    if name=='emma':
        target_row = 9
        target_col = 0
    if name=='olivia':
        target_row = 9
        target_col = 9

    return (target_row, target_col)


def run_simulation(number, filename, grid_size=10, target_list=[(0,0),(9,0),(0,9),(9,9)]):
    """ Start robot navigation simulation.

    Extended description of function

    Args:
        number (int): The number of robots that you want to create.
        filename (str): The file that reserves all the robot's name.
        grid_size (int): The size of the grid. Defaults to 10.
        terget_list (list): A list of target coordinates.
    """
    names, ids, rows, cols, directions = create_several_robots(number, filename)

    print_robots_greeting(names, ids)
    print()

    for index in range(number):
        target_row, target_col = generate_target_row_col(names[index])
        print_search_for_drink(names[index])
        navigate_to_target_position(rows[index], cols[index], directions[index],
                                    target_row, target_col, grid_size)
        print()

    return None


def create_several_robots(number, filename):
    """Create different robots

    Extended description of function

    Args:
        number (int): The number of robots that you want to create.
        filename (str): The file that reserves all the robot's name.
    Returns:
        list: A list of robot's names
        list: A list of robot's identifiers
        list: A list of robot's row coordinates.
        list: A list of robot's column coordinate.
        list: A list of robot's directions.
    """
    names = []
    ids = []
    rows = []
    cols =[]
    directions = []
    for _ in range(0, number):
        name, row, col, direction = robot_setup(filename, grid_size=10)
        names.append(name)
        id = id_generator(name)
        ids.append(id)
        rows.append(row)
        cols.append(col)
        directions.append(direction)
    return (names, ids, rows, cols, directions)


def id_generator(name):
    """Generate specific id for each robot

    Extended details of function

    Args:
        name (str): Robot's name.

    Returns:
        int: Robot's id"""

    if name=='shameer':
        identifier = 2628
    if name=='ruoxue':
        identifier = 2629
    if name=='emma':
        identifier = 2630
    if name=='olivia':
        identifier = 2631
    return identifier




def print_search_for_drink(name):
    return print(f"{name} is searching for its drink.")


run_simulation(3, "robot_names.txt")
