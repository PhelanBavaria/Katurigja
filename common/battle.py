

from content.maps import mapgen


class Battle:
    def __init__(self, setup):
        self.setup = setup
        self.turn = 0
        self.history = {}
        self.units = {}
        self.tiles = {}
        self._setup(setup)

    def _setup(self, setup):
        self.tiles = mapgen.load(setup['map'])

    def make_turn(self):
        self.turn += 1
        print('turn: ', self.turn)
