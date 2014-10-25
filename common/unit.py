

class Unit:
    def __init__(self, title=None):
        self.title = title
        self.stats = {
            'strength': 1,
            'stamina': 1,
            'willpower': 1,
            'strategic': 1,
            'dexterity': 1,
            'ambition': 1,
            'adabtability': 1,
            'size': 1,
            'loyalty': 1,
            'courage': 1
        }
        self.equipment = {}
