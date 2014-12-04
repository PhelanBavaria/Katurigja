

import os
import operator
import yaml
import characters
from common import util


class Unit:
    def __init__(self, name=None, title=None):
        self._id = util.rand_id()
        self.name = name
        self.title = title
        self.position = ()
        self.rotation = 0
        self.higher_commander = ''
        self.lower_commanders = []
        self.formation = None
        self.actions = {
            'move': self.move
        }
        if name and name in characters.overview:
            self.load()
        else:
            self.create()

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

    def move(self):
        speed = self.stats['speed']
        relative = util.rect(speed, self.rotation)
        self.position = map(operator.add, self.position, relative)
        self.position = tuple(self.position)

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
