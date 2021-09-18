class cut_left_overs:

    def __init__(self, length) -> None:
        self.leftover = length
        self.pieces = []

    def cut(self, cut_by):
        self.leftover -= cut_by
        self.pieces.append(cut_by)

    def __str__(self) -> str:
        return str([self.leftover, self.pieces])


def find_cuts(uncut, lengths) -> None:
    cut: cut_left_overs = []
    impossible = []
    for l in uncut:
        cut.append(cut_left_overs(l))

    for length in lengths:
        flag = True
        for log in cut:
            if log.leftover >= length:
                log.cut(length)
                flag = False
                break
        if flag:
            impossible.append(length)
                
    for x in cut:
        print(str(x))

    print("Impossible Pieces: " + str(impossible))


def main():
    pieces_to_cut = [8, 8, 8, 8, 8, 8]
    pieces_needed = [7, 2, 5, 3, 3, 3, 3, 4, 4]

    find_cuts(pieces_to_cut, reversed(sorted(pieces_needed)))


if __name__ == "__main__":
    main()
