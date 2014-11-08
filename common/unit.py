

import os
import operator
import yaml
import characters
from common import util


class Unit:
    units = []
    def __init__(self, name=None, title=None):
        self.name = name
        self.title = title
        self.position = ()
        self.rotation = 0
        self.formation = None
        self.todo = ()
        self.actions = {
            'move': self.move
        }
        if name and name in characters.overview:
            self.load()
        else:
            self.create()
        Unit.units.append(self)

    def create(self):
        self.stats = {
            'strength': 1,
            'speed': 1,
            'stamina': 1,
            'willpower': 1,
            'strategic': 1,
            'dexterity': 1,
            'ambition': 1,
            'adabtability': 1,
            'size': 1,
            'loyalty': 1,
            'courage': 1
        }
        self.equipment = {}

    def update(self):
        if not self.todo:
            return
        self.actions[self.todo[0]](self.todo[1])

    def move(self, distance):
        speed = self.stats['speed']
        relative = util.rect(min(speed, distance), self.rotation)
        self.position = map(operator.add, self.position, relative)
        self.position = tuple(self.position)
        distance -= min(distance, speed)
        if distance > 0:
            self.todo = ('move', distance)
        else:
            self.todo = ()


    def load(self):
        stats = open('characters/' + self.name + '/stats.yml').read()
        equip = open('characters/' + self.name + '/equip.yml').read()
        self.stats = yaml.load(stats)
        self.equipment = yaml.load(equip)

    def save(self, on_existing=None):
        try:
            os.makedirs('characters/' + self.name)
        except OSError:
            if on_existing and not on_existing():
                return
        stats = yaml.dump(self.stats, default_flow_style=False)
        equip = yaml.dump(self.equipment, default_flow_style=False)
        open('characters/' + self.name + '/stats.yml', 'w+').write(stats)
        open('characters/' + self.name + '/equip.yml', 'w+').write(equip)
