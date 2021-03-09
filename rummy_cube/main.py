from Board import Board
from Tile import Tile

if __name__ == "__main__":
    b = Board()
    t1 = Tile('green', 4)
    t2 = Tile('green', 5)
    t3 = Tile('blue', 13)
    b.add(t1)
    b.add(t2)
    b.add(t3)

    for i in b.tiles:
        print(i)
