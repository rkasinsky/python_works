"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):
    engine = ''

    def set_engine(self, volume, pistons):
        self.engine = Engine(volume, pistons)
#
#
# my_car = Car(1500, 60, 15)
# my_car.set_engine(4, 6)
# print(my_car.engine)
