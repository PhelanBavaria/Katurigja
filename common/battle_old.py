

from content.maps import mapgen
from common import Unit


class Battle:
    def __init__(self, setup):
        self.setup = setup
        self.turn = 0
        self.history = {}
        self.tiles = {}
        self._setup(setup)

    def _setup(self, setup):
        self.tiles = mapgen.load(setup['map'])

    def make_turn(self):
        self.turn += 1
        print(Unit.units)
        [unit.update() for unit in Unit.units]
        print('turn: ', self.turn)
