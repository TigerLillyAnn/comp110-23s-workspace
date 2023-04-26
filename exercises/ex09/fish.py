"""File to define Fish class."""
__author__ = "730477496"


class Fish:
    """Fish behavior."""
    age: int
    hunger_score: int

    def __init__(self):
        """Sets the age of fish."""
        self.age = 0
        return None
    
    def one_day(self):
        """Adds 1 age for 1 day passed."""
        self.age += 1
        return None