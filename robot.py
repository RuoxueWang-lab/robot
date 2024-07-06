class Robot:
    def __init__(self, identifier, name, position, dirction, grid_size ):
        self.identifier = identifier
        self.name = name
        self.position = position
        self.direction = dirction
        self.grid = grid_size

    def greet(self):
        return print(f"Hello. My name is {self.name}. My ID is {self.identifier}.")


    def print_search_for_drink(self):
        return print(f"{self.name} is searching for its drink.")


    def _direction_to_string(self):
        """ Represent direction in string form: "North", "Sounth", "East", "West"

        Returns:
            str: Robot's direction in string form ("North", "Sounth", "East", "West")
        """
        if self.direction == "n":
            direction_string = "North"
        elif self.direction == "s":
            direction_string = "South"
        elif self.direction == "e":
            direction_string = "East"
        elif self.direction == "w":
            direction_string = "West"

        return direction_string


    def _direction_to_index(self):
        """ Assign numbers(0,1,2,3) to each direction
        """
        if self.direction == "n":
            direction_index = 0
        if self.direction == "e":
            direction_index = 1
        if self.direction == "s":
            direction_index = 2
        if self.direction == "w":
            direction_index = 3

        return direction_index


    def print_positon_direction_message(self):
        """ Robot states its current position and next moving."""
        direction_string = self._direction_to_string()
        position = self.position
        return print(f"I am currently at {position}, facing {direction_string}.")


    def moving_one_step_forward(self):
        """ Move the robot one step forward."""
        print("Moving one step forward.")
        current_row, current_col = self.position
        if self.direction == 'n':
            new_row = current_row - 1
            new_col = current_col
        if self.direction == 's':
            new_row = current_row + 1
            new_col = current_col
        if self.direction == 'w':
            new_col = current_col - 1
            new_row = current_row
        if self.direction == 'e':
            new_col = current_col + 1
            new_row = current_row

        self.position = tuple([new_row, new_col])


    def rotate_90_clockwise(self, direction_index):
        """ Rotate the robot by 90 degrees clockwise when it hits a wall

        Args:
            direction_index (int): the corresponding index assigned to the specific direction
        """
        print("Turn 90 degrees clockwise.")
        direction_index = (direction_index + 1) % 4
        if direction_index == 0:
            self.direction = "n"
        elif direction_index == 1:
            self.direction = "e"
        elif direction_index == 2:
            self.direction = "s"
        else:
            self.direction = "w"


    def navigate_to_wall(self):
        """ Navigate the robot to until"""
        if self.direction == "n":
            current_position = self.position
            while current_position[0] > 0:
                self.print_positon_direction_message()
                self.moving_one_step_forward()
                current_position = self.position
        if self.direction == "s":
            current_position = self.position
            while current_position[0] < self.grid-1:
                self.print_positon_direction_message()
                self.moving_one_step_forward()
                current_position = self.position
        if self.direction == "w":
            current_position = self.position
            while current_position[1] > 0:
                self.print_positon_direction_message()
                self.moving_one_step_forward()
                current_position = self.position
        if self.direction == "e":
            current_position = self.position
            while current_position[1] < self.grid-1:
                self.print_positon_direction_message()
                self.moving_one_step_forward()
                current_position = self.position

        self.position = current_position
        self.print_positon_direction_message()


    def navigate_to_target_position(self,
                                    target_position):
        """ Navigate to out targer position. Defalts to (9, 9)

        Args:
            target_position (tup): The current coordinates of the target cell.
        """
        current_position = self.position
        while current_position[0]!=target_position[0] or current_position[1]!=target_position[1]:
            self.navigate_to_wall()
            current_position = self.position
            if current_position[0]==target_position[0] and current_position[1]==target_position[1]:
                print("I am drinking Ribena! I am happy!")
                break
            print("I have a wall in front of me.")
            direction_index = self._direction_to_index()
            self.rotate_90_clockwise(direction_index)
            current_position = self.position
