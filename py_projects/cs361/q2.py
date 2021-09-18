import math

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


def dist(p1:Point, p2:Point):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)


stops = [Point(1, 1), Point(1, 2), Point(1, 3)]


def find_time(stops:list):
    curr_pos = Point(0, 0)
    time = 0
    while len(stops):
        smallest = dist(curr_pos,stops[0])
        next_pos = 0
        for x in range(len(stops)):
            test = dist(curr_pos,stops[x])
            if test < smallest:
                smallest = test
                next_pos = x
        time += smallest
        time += 5
        curr_pos = stops[next_pos]
        stops.pop(next_pos)
    print(str(time))

def main():
    find_time(stops)

if __name__ == "__main__":
    main()
