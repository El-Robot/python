import math

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


def dist(p1:Point, p2:Point):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)


stops = [Point(0, 3), Point(0, 1), Point(0, 2), Point(0,-2)]


def find_time(stops:list):
    curr_pos = Point(0, 0)
    time = 0
    counter = 0
    while counter < len(stops):
        smallest = dist(curr_pos,stops[counter])
        next_pos = counter
        for x in range(counter+1, len(stops)):
            test = dist(curr_pos,stops[x])
            if test < smallest:
                smallest = test
                next_pos = x
        time += smallest
        time += 5
        curr_pos = stops[next_pos]
        temp = stops[next_pos]
        stops[next_pos] = stops[counter]
        stops[counter] = temp
        counter += 1
        
    print(str(time))

def main():
    find_time(stops)

if __name__ == "__main__":
    main()
