"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730477496"


class Simpy:
    """A utility class that is helpful for working with sequences of numerical data."""

    values: list[float]
   
    def __init__(self, values: list[float]):
        """Initialize values."""
        self.values = values
    
    def __str__(self) -> str:
        """Covert simpy to str representation."""
        return f"Simpy({str(self.values)})"
    
    def fill(self, value: float, count: int) -> None:
        """Fill a simpys values with a specific number of repeating values."""
        self.values = [value] * count

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """To fill in 'values' attribute with range of values."""
        assert step != 0.0
        self.values = []
        i = start
        if step > 0:
            while i < stop:
                self.values.append(i)
                i += step
        else:
            while i > stop:
                self.values.append(i)
                i += step

    def sum(self) -> float:
        """Purpose is to compute and return the sum of all items in the `values` attribute."""
        return sum(self.values)
    
    def __add__(self, other: Union[float, Simpy]) -> Simpy:
        """Add ability to use addition operation in conjection with Simpy."""
        if isinstance(other, Simpy):
            assert len(self.values) == len(other.values)
            return Simpy([a + b for a, b in zip(self.values, other.values)])
        elif isinstance(other, float):
            return Simpy([a + other for a in self.values])
        else:
            raise TypeError(f"unsupported operand type(s) for +: Simpy and {type(other).__name__}")

    def __pow__(self, other: Union[Simpy, float]) -> Simpy:
        """Add ability to use power operator in conjunction with Simpy."""
        if isinstance(other, float):
            return Simpy([x ** other for x in self.values])
        else:
            assert len(self.values) == len(other.values)
            return Simpy([x ** y for x, y in zip(self.values, other.values)])

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Add the ability to produce a _mask_, or a `list[bool]`, based on the equality of each item in the `values` attribute."""
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values), "Simpy objects have different lengths"
            return [self.values[i] == rhs.values[i] for i in range(len(self.values))]
        elif isinstance(rhs, float):
            return [self.values[i] == rhs for i in range(len(self.values))]
        else:
            raise TypeError("unsupported operand type(s) for ==: 'Simpy' and '{}'".format(type(rhs).__name__))

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Add the ability to produce a _mask_, or a `list[bool]`, based on the greater than relationship between each item in the `values` attribute."""
        if isinstance(rhs, float):
            return [x > rhs for x in self.values]
        elif isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values), "Simpy objects must have the same length"
            return [x > y for x, y in zip(self.values, rhs.values)]
        else:
            raise TypeError(f"unsupported operand type(s) for >: 'Simpy' and '{type(rhs)}'")
        
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Test for whether `rhs` is an instance of an `int` or not."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            return Simpy([x for x, mask in zip(self.values, rhs) if mask])