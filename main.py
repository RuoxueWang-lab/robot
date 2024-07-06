from robot_init import RobotFactory
from robot import Robot

def load_names_from_file(filename):
    """Load the robot's name in our robot_names.txt

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


def indexed_robots_dict_list(robots_dict_list):
    """ Put the dictinory of each robot into a single dictionary where keys are their ids

    Args:
        robots_dict_list (list): A list of robots personal information dictionaries.

    Returns:
        dict: keys are the ids of robots and values are dictionaries of robots' themselves.

    """
    robots_dict = {}
    for dic in robots_dict_list:
        robots_dict[dic["id"]] = dic
    return robots_dict


def clipping_the_coordinates(robot, grid_size):
    """ The robot can only move inside the grid

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


def generate_target_row_col(robot):
    """Generate taget row coordinate and column coordinate.

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

    Args:
        number (int): The number of robots that you want to create.
        filename (str): The file that reserves all the robot's name.
        grid_size (int): The size of the grid. Defaults to 10.
        terget_list (list): A list of target coordinates.
    """
    names = load_names_from_file(filename)
    robot_factory = RobotFactory(10, names)
    robots = robot_factory.create_robots(3)

    for robot in robots:
        robot.greet()
    print()

    for robot in robots:
        targeted_position = generate_target_row_col(robot)
        robot.print_search_for_drink()
        robot.navigate_to_target_position(targeted_position)
        print()

    return None

run_simulation(3, "robot_names.txt")
