

import yaml
from interfaces import CommandLine


class Game:
    local_interface = None
    config = yaml.load(open('config.yml').read())
    keymap = yaml.load(open('keymap.yml').read())
    keys_down = set()
    battle = None


if __name__ == '__main__':
    game = Game()
    game.local_interface = CommandLine(game)
    result = None
    while result != False:
        result = game.local_interface.update()
        if game.battle and game.config['battle_turn_time']:
            game.battle.update()
