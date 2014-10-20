

class Tile:
    def __init__(self, x, y, group, ttype=None):
        self.x, self.y = x, y
        self.group = group
        self._type = ttype

    def relcoord(self, x=0, y=0):
        x = x + self.x
        y = y + self.y
        try:
            return self.group[(x, y)]
        except KeyError:
            return None

    def adjacent(self):
        for x, y in ((0, -1), (1, 0), (0, 1), (-1, 0)):
            yield self.relcoord(x, y)

    def across(self):
        for x, y in ((-1, -1), (1, -1), (1, 1), (-1, 1)):
            yield self.relcoord(x, y)
