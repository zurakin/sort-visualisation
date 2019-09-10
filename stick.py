

class Stick():
    def __init__(self, height):
        self.height = height
        self.selected = False
        self.min = False
        self.current = False
        self.sorted = False
    def get_fill(self):
        if self.sorted:
            return 'blue'
        if self.current:
            return 'green'
        if self.min:
            return 'red'
        if self.selected:
            return 'yellow'
        return 'black'

    def __repr__(self):
        return str(self.height)
