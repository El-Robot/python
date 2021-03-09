class Tile:
    def __init__(self, color, number):
        self.color = color
        self.number = number

    def __str__(self):
        return str(self.color) + ' ' +  str(self.number)