

import yaml
from interfaces import CommandLine


class Game:
    local_interface = None
    gui = None
    battle = None
    config = yaml.load(open('config.yml').read())


if __name__ == '__main__':
    game = Game()
    game.local_interface = CommandLine(game)
    while not game.local_interface.exit:
        game.local_interface.update()
