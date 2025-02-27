"""File to define River class."""

__author__ = "730477496"
from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """Defines how the river will function."""
    
    day: int
    bears: int
    fish: int

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Ages of fish and bears are checked, removed if necessary."""
        alive_fish = []
        alive_bears = []
        for i in self.fish:
            if i.age <= 3:
                alive_fish.append(i)
        self.fish = alive_fish

        for j in self.bears:
            if j.age <= 5:
                alive_bears.append(j)
        self.bears = alive_bears

        return None
    
    def remove_fish(self, amount: int) -> None:
        """Remove fish from river."""
        for i in range(amount):
            if self.fish:
                self.fish.pop(0)

    def bears_eating(self):
        """Bears eating habits and how much they eat."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None
    
    def check_hunger(self):
        """If Bears starve, remove them."""
        alive_bears = []
        for bear in self.bears:
            if bear.hunger_score < 0:
                alive_bears.append(bear)
        self.bears = alive_bears
        return None
        
    def repopulate_fish(self):
        """How to repopulate fish."""
        num_fish = len(self.fish)
        num_new_fish = num_fish // 2 * 4
        for i in range(num_new_fish):
            new_fish = Fish()
            self.fish.append(new_fish)
        return None
    
    def repopulate_bears(self):
        """How to repopulate bears."""
        num_bears = len(self.bears)
        num_new_bears = num_bears // 2
        for i in range(num_new_bears):
            new_bear = Bear()
            self.bears.append(new_bear)
        return None
    
    def view_river(self):
        """Prints the fish and bear populations of the river respectively."""
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
        """Loops 7 river days."""
        for _ in range(7):
            self.one_river_day()
            
