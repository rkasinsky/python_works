from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle:
    weight = 2000
    started = False
    fuel = 60
    fuel_consumption = 10

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started and self.fuel > 0:
            self.started = True
        elif self.started and self.fuel > 0:
            pass
        else:
            raise LowFuelError(self.fuel)

    def move(self, distance):
        if distance <= (self.fuel / self.fuel_consumption) and self.fuel > 0:
            self.fuel = self.fuel - distance * self.fuel_consumption
        else:
            raise NotEnoughFuel(self.fuel)
