"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    initial_cargo = 0
    cargo = 0
    max_cargo = 200

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.max_cargo = max_cargo

    def load_cargo(self, load):
        if load + self.cargo <= self.max_cargo:
            self.cargo += load
        else:
            raise CargoOverload(load)

    def remove_all_cargo(self):
        self.cargo = 0
