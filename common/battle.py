

class Battle:
    def __init__(self, setup):
        self.setup = setup
        self.turn = 0
        self.history = {}
        self.units = {}
        self.tiles = {}

    def make_turn(self):
        self.turn += 1
        print('turn: ', self.turn)
