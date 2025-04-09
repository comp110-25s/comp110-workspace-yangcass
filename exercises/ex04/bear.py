"""File to define Bear class."""

__author__: str = "730717480"


class Bear:
    """This just looking at the Bear class and what is within this class."""

    age: int
    hunger_score: int

    def __init__(self):
        """This is the starting point."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Looking at one day in a bear life."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int) -> None:
        """This is jsut looking at how much the bear eat."""
        self.hunger_score += num_fish
        return None
