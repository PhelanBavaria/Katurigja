

from interfaces import Base
from interfaces import Player
from interfaces import AI
from battle import Battle
from common import Unit
from common import Formation


class CommandLine(Base):
    counter = 0
    last_action = None

    def __init__(self, game):
        Base.__init__(self, game)
        self.actions = {
            'exit': self.exit,
            'eval': self._eval,
            'create_character': self.create_character,
            'setup_example_battle': self.setup_example_battle,
            'place_formation': self.place_formation,
            'move': self.move,
            'make_turn': self.make_turn
        }

    def update(self):
        if self.counter:
            self.last_action()
            self.counter -= 1
        else:
            command = input('>>> ')
            try:
                action = self.actions[command]
            except KeyError:
                print('Action not supported')
                return
            return action()

    def _eval(self):
        if self.game.config['eval']:
            try:
                return eval(input('\t'))
            except NameError:
                print('No valid command')
            except SyntaxError:
                print('SyntaxError')
        else:
            print('You are not allowed to use this command')

    def exit(self):
        return False

    def create_character(self):
        def warning_overwrite():
            yesno = input('Character already exists, continue? (y/n)')
            if yesno == 'y':
                return True
            elif yesno == 'n':
                return False
            else:
                print('No valid answer!')
                return warning_overwrite()
        name = input('name: ')
        unit = Unit(name, 'general')
        unit.save(warning_overwrite)

    def setup_example_battle(self):
        battle = Battle()
        testian = Unit('Testian', 'general')
        formation = Formation([testian,])
        player = Player(self.game)
        player.character = testian
        battle.controllers.append(player)
        for i in range(10):
            unit = Unit()
            formation.add_unit(unit)
            ai = AI(self.game)
            ai.character = unit
            battle.controllers.append(ai)
        self.game.battle = battle

    def place_formation(self):
        id_name = input('Commander ID: ')
        for controller in self.game.battle.controllers:
            is_id = controller.character._id == id_name
            is_name = controller.character.name == id_name
            if is_id or is_name:
                commander = controller.character
                break
        else:
            print('Commander not found')
            return
        pos = input('Position: ')
        try:
            x, y = pos.split(' ')
            x, y = int(x), int(y)
        except ValueError:
            print('Input must be: X Y')
            return
        commander.formation.place(x, y)

    def move(self):
        k_move = self.game.keymap['p_move']
        #keys_down = self.game.keys_down
        self.game.keys_down.append(k_move)
        #self.game.keys_down = set(keys_down)

    def make_turn(self):
        '''only advised to use if config['battle_turn_time'] is 0'''
        try:
            self.game.battle.update()
        except AttributeError:
            print('Battle has to be setup first')
            return
