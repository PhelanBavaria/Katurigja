

from common import Unit
from common import Battle


class CommandLine:
    counter = 0
    last_action = None
    exit = False

    def __init__(self, game):
        self.game = game
        self.actions = {
            'exit': self._exit,
            'eval': self._eval,
            'create_character': self.create_character,
            'setup_example_battle': self.setup_example_battle,
            'make_turn': self.make_turn
        }

    def update(self):
        if self.counter:
            self.last_action()
            self.counter -= 1
        else:
            command = input('>>> ')
            command = command.split(': ')
            action, args = command[0], command[1:]
            try:
                action = self.actions[action]
            except KeyError:
                print('Action not supported')
                return
            action(*args)

    def _exit(self, *args):
        self.exit = True

    def _eval(self, *args):
        if self.game.config['eval']:
            eval(args[0])
        else:
            print('You are not allowed to use this command')

    def create_character(self, *args):
        def warning_overwrite():
            yesno = input('Character already exists, continue? (y/n)')
            if yesno == 'y':
                return True
            elif yesno == 'n':
                return False
            else:
                print('No valid answer!')
                return warning_overwrite()
        unit = Unit(args[0], 'general')
        unit.save(warning_overwrite)

    def setup_example_battle(self, *args):
        setup = {
            'map': 'grassland'
        }
        self.game.battle = Battle(setup)
        print('Battle is ready!')

    def make_turn(self, *args):
        try:
            self.game.battle.make_turn()
        except AttributeError:
            print('Battle has to be setup first')
            return
        if args:
            times = int(args[0])-1
            self.counter += times
            self.last_action = self.make_turn
