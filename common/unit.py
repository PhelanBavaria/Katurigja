

import os
import yaml
import characters


class Unit:
    def __init__(self, name=None, title=None):
        self.name = name
        self.title = title
        if name and name in characters.overview:
            self.load()
        else:
            self.create()

    def create(self):
        self.stats = {
            'strength': 1,
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
        stats = yaml.dump(self.stats)
        equip = yaml.dump(self.equipment)
        open('characters/' + self.name + '/stats.yml', 'w+').write(stats)
        open('characters/' + self.name + '/equip.yml', 'w+').write(equip)
