

from interfaces import Base


class Player(Base):
    def __init__(self, game):
        Base.__init__(self, game)
        self.character = None
        self.key_actions = {
            'move': game.keymap['p_move']
        }

    def update(self):
        for action, key in self.key_actions.items():
            if key in self.game.keys_down:
                self.character.actions[action]()
