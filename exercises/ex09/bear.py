"""File to define Bear class."""
__author__ = "730477496"


class Bear:
    """Bear behavior."""
    age: int
    hunger_score: int

    def __init__(self):
        """Sets age and hunger score for bears."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """Adds age and hunger score as a day goes by."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Hunger score changes when bear eats fish."""
        self.hunger_score += num_fish
    