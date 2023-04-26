"""River Simulation."""

__author__ = "730477496"
from river import River
from river import Fish
from river import Bear


class RiverSimulation:
    """Defines the specific river simulation."""
    def __init__(self):
        """Sets starting numbers for my river."""
        self.my_river = River([Fish() for _ in range(10)], [Bear() for _ in range(10)])
