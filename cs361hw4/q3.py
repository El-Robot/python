class Node:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

def bfs(start: str, graph: dict):
    seen = {start}
    q = [start]

    while q:
        node = q.pop(0)

        for i in graph[node]:
            if i not in seen:
                q.append(i)
                seen.add(i)
    return


def main(matrix, x1, y1, x2, y2):
    q = [Node(x1, y1, x2, y2)]

    while q:
        node = q.pop(0)
        
        


        for i in 

if __name__ == "__main__":

    matrix = [
        [0, 1, 1],
        [0, 1, 0],
        [0, 1, 1]
    ]
    main(matrix, 2, 2, 1, 1)
