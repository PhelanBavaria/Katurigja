

from interfaces import Base


class AI(Base):
    def __init__(self, game):
        Base.__init__(self, game)
        self.character = None

    def update(self):
        self.character.move()
