import random
from robot import Robot

class RobotFactory:
    def __init__(self, grid, candidate_names=[], prevent_id=-1):
        self.grid = grid
        self.names =  candidate_names
        self.prevent_id = prevent_id


    def _generate_id(self):
        """ Generate a unique ID for the robot.

        If id is given and is >=0, the function will return prev_id+1
        Otherwise, the function will generate a random number between 1 to 1,000,000 as an ID.

        Returns:
            int : robot ID
        """
        if self.prevent_id >= 0:
            self.prevent_id += 1
            return self.prevent_id
        else:
            return random.randint(1, 1000000)


    def _generate_name(self):
        """ Select a robot's name at random from a given list

        Returns:
            str : Robot name
        """
        if len(self.names) > 0:
            return random.choice(self.names)
        else:
            return "Robot"


    def _generate_position(self):
        """ Generate a random (row, col) position for the robot.

        The coordinates will be between 0 to self.grid.size.

        Returns:
            tuple : The coordinate of robot's position
        """
        row = random.randint(0, self.grid-1)
        col = random.randint(0, self.grid-1)
        return tuple((row, col))


    def _generate_direction(self):
        """ Generate a random direction for the robot.

        Returns:
            str : direction ("n", "s", "e" or "w")
        """
        return random.choice(["n", "s", "e","w"])


    def create_robot(self):
        """ Initialize the robot's name, ID, initial coordinates and direction.

        Args:
            filename (str): The name of the file where you reserve the robot's name

        Returns:
            Robot:
        """
        name = self._generate_name()
        id = self._generate_id()
        position = self._generate_position()
        direction = self._generate_direction()
        robot = Robot(id, name, position, direction, self.grid)

        return robot


    def create_robots(self, number):
        """ Create multiple robot instances.

        Each robot will be initialised with a random robot name, ID, and
        initial position and direction.

        Args:
            number (int) : The number of robots to create (defaults to 1)

        Returns:
            list[Robot]
        """
        robots = []
        for _ in range(number):
            robot = self.create_robot()
            robots.append(robot)
        return robots
