

import operator
from common import util


class Formation:
    def __init__(self, units, commander=None):
        self.units = []
        if commander:
            self.commander = commander
        else:
            self.commander = units[0]
        self.__speed_tally = 0
        self.rotation = 0
        for unit in units:
            self.add_unit(unit)

    def speed(self):
        return self.__speed_tally / len(self.units)

    def add_unit(self, unit):
        self.units.append(unit)
        unit.formation = self
        self.__speed_tally += unit.stats['speed']

    def remove_unit(self, unit):
        self.units.remove(unit)
        self.__speed_tally -= unit.stats['speed']

    def move(self):
        for unit in self.units:
            unit.rotation = self.rotation
            unit.move()

    def place(self, x, y):
        for unit in self.units:
            unit.rotation = self.rotation
            unit.position = (x, y)

    def rotate(self, towards):
        center = (0, 0)
        for unit in self.units:
            center = map(operator.add, center, unit.position)
        center = (c / len(self.units) for c in center)
        relative = map(operator.sub, center, towards)
        self.rotation = util.rect(*relative)
        for unit in self.units:
            unit.rotation = self.rotation
