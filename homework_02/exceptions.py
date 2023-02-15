"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    def __init__(self, fuel, text="Fuel level is low"):
        self.fuel = fuel
        self.txt = text
        super().__init__(self.txt)


class NotEnoughFuel(Exception):
    def __init__(self, fuel, text="Fuel level is not enough"):
        self.fuel = fuel
        self.txt = text
        super().__init__(self.txt)


class CargoOverload(Exception):
    def __init__(self, text):
        self.txt = "Cargo is overloaded"
