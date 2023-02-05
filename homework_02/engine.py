"""
create dataclass `Engine`
"""

from dataclasses import dataclass


@dataclass
class Engine:
    """Class for the Engine info"""
    volume: int
    pistons: int

    def __init__(self, volume: int, pistons: int):
        self.volume = volume
        self.pistons = pistons
