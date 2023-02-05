"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    def __init__(self, text):
        self.txt = "Fuel level is low"


class NotEnoughFuel(Exception):
    def __init__(self, text):
        self.txt = "Fuel level is not enough"


class CargoOverload(Exception):
    def __init__(self, text):
        self.txt = "Cargo is overloaded"
