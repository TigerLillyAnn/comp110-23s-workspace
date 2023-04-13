from __future__ import annotations

class Point:

    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"
    
    def __mul__(self, factor: float) -> Point:
        scaled: Point = Point(self.x * factor, self.y * factor)
        return scaled
    
    def __add__(self, value: float) -> Point:
        """new_x: float = self.x + value
        new_y: float = self.y + value
        added_point: Point = Point(new_x, new_y)
        return added_point""" 
        # ^Classroom example
        sum: Point = Point(self.x + value, self.y + value)
        return sum



    

