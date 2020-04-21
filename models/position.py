"""This module defines classes and functions related to the positions used by items and he hero in the game."""


class Position:
    """This class represent a position on the maze with an y and y."""

    def __init__(self, x, y):
        """This function initialize a position with an x and y."""
        self.x = x
        self.y = y

    def update(self, direction):
        """This function allows to move the position from one step in a
        direction."""

        if direction == "r":
            self.x += 1
        elif direction == "l":
            self.x -= 1
        elif direction == "u":
            self.y -= 1
        elif direction == "d":
            self.y += 1

    def get_position(self):
        """This function returns the position thourgh a tuple."""

        return Position(self.x, self.y)

    def __eq__(self, other):
        """This function allows to compare two positions on the basis of their
        x and y."""
        if self.x == other.x and self.y == other.y:
            return True

    def __repr__(self):
        """This function return the position as x y."""

        return f"Position ({self.x}, {self.y})"

    @property
    def xy(self):
        return self.x, self.y
