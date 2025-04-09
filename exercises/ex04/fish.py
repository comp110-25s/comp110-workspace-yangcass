"""File to define Fish class."""

__author__: str = "730717480"


class Fish:
    """This is just looking at the fish class."""

    age: int

    def __init__(self):
        """This is the starting point."""
        self.age = 0
        return None

    def one_day(self):
        """Looking at one day in a fish life."""
        self.age += 1
        return None
