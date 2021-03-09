class Board:
    def __init__(self):
        self.tiles = set()

    def __str__(self):
        return str(self.tiles) + ' Yay!'

    def add(self, new_tile):
        self.tiles.add(new_tile)

    def isLegal(self):
        pass