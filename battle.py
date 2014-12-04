

class Battle:
    def __init__(self):
        self.turn = 0
        self.controllers = []

    def update(self):
        for controller in self.controllers:
            controller.update()
        self.turn += 1
