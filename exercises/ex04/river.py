"""File to define River class."""

__author__: str = "730717480"

from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear


class River:
    """This is the river class looking and what is within the river  class."""

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """This is just checking the bear and fish age."""
        new_list_bear: list[Bear] = []
        new_list_fish: list[Fish] = []
        new_list_fish = self.fish
        new_list_bear = self.bears
        idx: int = 0
        while idx < len(self.fish):
            if new_list_fish[idx].age > 3:
                new_list_fish.pop(idx)
            else:
                idx += 1
        while idx < len(self.bears):
            if new_list_bear[idx].age > 5:
                new_list_bear.pop(idx)
            else:
                idx += 1
        self.fish = new_list_fish
        self.bears = new_list_bear
        return None

    def remove_fish(self, amount: int) -> None:
        """This remove any fish from the top of the list or a given number."""
        idx: int = 0
        while idx < amount:
            self.fish.pop(0)
            idx += 1
        return None

    def bears_eating(self):
        """This is just looking at how the bear eat and when it can get the fish."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None

    def check_hunger(self):
        """This check how hunger the bear are."""
        new_list_bears: list[Bear] = []
        new_list_bears = self.bears
        idx: int = 0
        while idx < len(new_list_bears):
            if new_list_bears[idx].hunger_score < 0:
                new_list_bears.pop(idx)
            else:
                idx += 1
        self.bears = new_list_bears
        return None

    def repopulate_fish(self):
        """This help the repopulate of the new fish."""
        f: int = (len(self.fish) // 2) * 4
        idx: int = 0
        while idx < f:
            self.fish.append(Fish())
            idx += 1
        return None

    def repopulate_bears(self):
        """This help the repopulate of the new bear."""
        b: int = len(self.bears) // 2
        idx: int = 0
        while idx < b:
            self.bears.append(Bear())
            idx += 1
        return None

    def view_river(self):
        """This just help show the day, fish population, and bear population."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """This is looking at the river for one week."""
        idx = 0
        while idx < 7:
            self.one_river_day()
            idx += 1
        return None
