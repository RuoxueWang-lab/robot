import random
from robot import Robot

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


def identifiers_generator(name):
    """Generate specific id for each robot

    Extended details of function

    Args:
        name (str): Robot's name.

    Returns:
        int: Robot's identfier.
    """
    if name=='shameer':
        id_robot = 2628
    if name=='ruoxue':
        id_robot = 2629
    if name=='emma':
        id_robot = 2630
    if name=='olivia':
        id_robot = 2631
    return id_robot


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
    id = identifiers_generator(name)
    row = random.randint(0, grid_size-1)
    col = random.randint(0, grid_size-1)
    position = (row, col)
    direction = random.choice(["n", "s", "e","w"])
    robot = Robot(id, name, position, direction)

    return robot


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
    robots_list = []
    for _ in range(number):
        robot_single = robot_setup(filename, grid_size=10)
        robots_list.append(robot_single)
    return robots_list


def indexed_robots_dict_list(robots_dict_list):
    """ Put the dictinory of each robot into a single dictionary where keys are their ids

    Extended description of function

    Args:
        robots_dict_list (list): A list of robots personal information dictionaries.

    Returns:
        dict: keys are the ids of robots and values are dictionaries of robots' themselves.

    """
    robots_dict = {}
    for dic in robots_dict_list:
        robots_dict[dic["id"]] = dic
    return robots_dict


def print_search_for_drink(robot):
    name = robot.name
    return print(f"{name} is searching for its drink.")


def print_robot_greeting(name, identifier):
    """ Print the robot's greeting.

    Extended description of function

    Args:
        name (str): the name of robot
        id (str): the id of robot
    """
    return print(f"Hello. My name is {name}. My ID is {identifier}.")


def print_robots_greeting(robots_list):
    """Print a list of several robots greeting

    Extended descriptionof function

    Args:
       name_list (list): A list of robot's names.
       id_list (list): A list of robot's indentifiers.
    """
    for robot in robots_list:
        print_robot_greeting(robot.name, robot.identifier)
    return None


def direction_to_string(robot):
    """ Represent direction in string form: "North", "Sounth", "East", "West"

    Extended description of the function

    Args:
        dirction (str): Robot's direction ("n", "s", "e", or "w")

    Returns:
        str: Robot's direction in string form ("North", "Sounth", "East", "West")
    """
    if robot.direction == "n":
        direction_string = "North"
    elif robot.direction == "s":
        direction_string = "South"
    elif robot.direction == "e":
        direction_string = "East"
    elif robot.direction == "w":
        direction_string = "West"

    return direction_string


def direction_to_index(robot):
    """ Assign numbers(0,1,2,3) to each direction

    Extended description of function

    Args:
        direction (str): Dirction of the robot

    Return:
        int: the direction's corresponding index(0,1,2,3)
    """
    if robot.direction == "n":
        direction_index = 0
    if robot.direction == "e":
        direction_index = 1
    if robot.direction == "s":
        direction_index = 2
    if robot.direction == "w":
        direction_index = 3

    return direction_index


def print_robot_positon_direction(robot):
    """ Robot states its current position and next moving.

    Extended description of function

    Args:
        current_position (tup): The current coordinates of the robot.
        current_direction (str): The current dirction("n","e","s","w") of the robot.
    """
    direction_string = direction_to_string(robot)
    position = robot.position
    return print(f"I am currently at {position}, facing {direction_string}.")



def moving_one_step_forward(robot):
    """ Move the robot one step forward

    Extended description of function

    Args:
        current_position (tup): The current coordinates of the robot.
        current_direction (str): The current dirction("n","e","s","w") of the robot.

    Returns:
        tuple: The new position of the robot.
    """
    print("Moving one step forward.")
    current_row, current_col = robot.position
    if robot.direction == 'n':
        new_row = current_row - 1
        new_col = current_col
    if robot.direction == 's':
        new_row = current_row + 1
        new_col = current_col
    if robot.direction == 'w':
        new_col = current_col - 1
        new_row = current_row
    if robot.direction == 'e':
        new_col = current_col + 1
        new_row = current_row

    robot.position = tuple([new_row, new_col])

    return robot


def rotate_90_clockwise(direction_index, robot):
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
        robot.direction = "n"
    elif direction_index == 1:
        robot.direction = "e"
    elif direction_index == 2:
        robot.direction = "s"
    else:
        robot.direction = "w"

    return robot


def clipping_the_coordinates(robot, grid_size):
    """ The robot can only move insed the grid

    Extended description of function

    Args:
        current_position (tup): The current coordinates of the robot.
        grid_size (str): The size of the grid.

    Returns:
        tuple: The new position of the robot.
    """
    current_row, current_col = robot.position
    if current_row < 0:
        new_row = 0
    elif current_row > grid_size-1:
        new_row = grid_size-1
    if current_col < 0:
        new_col = 0
    elif current_col > grid_size-1:
        new_col = grid_size-1

    robot.position = tuple([new_row, new_col])

    return robot


def navigate_to_wall(robot, grid_size):
    """ Navigate the robot to until

    Extended description of function

    current_direction (str): The current dirction("n","e","s","w") of the robot.
    current_position (tup): The current coordinates of the robot.
    grid_size (str): The size of the grid.

    Returns:
        tupel: The new position of the robot.
    """
    if robot.direction == "n":
        current_position = robot.position
        while current_position[0] > 0:
            print_robot_positon_direction(robot)
            current_position = moving_one_step_forward(robot).position
    if robot.direction == "s":
        current_position = robot.position
        while current_position[0] < grid_size-1:
            print_robot_positon_direction(robot)
            current_position = moving_one_step_forward(robot).position
    if robot.direction == "w":
        current_position = robot.position
        while current_position[1] > 0:
            print_robot_positon_direction(robot)
            current_position = moving_one_step_forward(robot).position
    if robot.direction == "e":
        current_position = robot.position
        while current_position[1] < grid_size-1:
            print_robot_positon_direction(robot)
            current_position = moving_one_step_forward(robot).position

    robot.position = current_position
    print_robot_positon_direction(robot)

    return robot


def navigate_to_target_position(robot,
                                target_position,
                                grid_size):
    """ Navigate to out targer position. Defalts to (9, 9)

    Extended description of function

    Args:
        current_direction (str): The current dirction("n","e","s","w") of the robot.
        current_position (tup): The current coordinates of the robot.
        target_position (tup): The current coordinates of the target cell.
        grid_size (str): The size of the grid.
    """
    current_position = robot.position
    while current_position[0]!=target_position[0] or current_position[1]!=target_position[1]:
        current_position = navigate_to_wall(robot, grid_size).position
        if current_position[0]==target_position[0] and current_position[1]==target_position[1]:
            print("I am drinking Ribena! I am happy!")
            break
        print("I have a wall in front of me.")
        direction_index = direction_to_index(robot)
        current_position = rotate_90_clockwise(direction_index,robot).position

    return None


def generate_target_row_col(robot):
    """Generate taget row coordinate and column coordinate.

    Extended description of function

    Args:
        name (str): Robot's name.

    Returns:
        int: Target row coordinate.
        int: Target column coordinate
        """
    if robot.name=='shameer':
        target_position = tuple([0,0])
    if robot.name=='ruoxue':
        target_position = tuple([0,9])
    if robot.name=='emma':
        target_position = tuple([9,0])
    if robot.name=='olivia':
        target_position = tuple([9,9])

    return target_position


def run_simulation(number, filename, grid_size=10, target_list=[(0,0),(9,0),(0,9),(9,9)]):
    """ Start robot navigation simulation.

    Extended description of function

    Args:
        number (int): The number of robots that you want to create.
        filename (str): The file that reserves all the robot's name.
        grid_size (int): The size of the grid. Defaults to 10.
        terget_list (list): A list of target coordinates.
    """
    robots_list = create_several_robots(number, filename)

    print_robots_greeting(robots_list)
    print()

    for robot in robots_list:
        targeted_position = generate_target_row_col(robot)
        print_search_for_drink(robot)
        navigate_to_target_position(robot,targeted_position, grid_size)
        print()

    return None

run_simulation(3, "robot_names.txt")
