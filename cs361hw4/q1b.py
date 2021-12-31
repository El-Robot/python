import sys


class Node:
    def __init__(self, val: int, next: list):
        self.next = next
        self.val = val

    def add_to(self, next):
        self.next.append(next)

    def __dict__():
        return


def compare(word1: str, word2: str):
    count = 0
    if word1[0] != word2[0]:
        count += 1
    if word1[1] != word2[1]:
        count += 1
    if word1[2] != word2[2]:
        count += 1
    if word1[3] != word2[3]:
        count += 1
    return count


def main(need_to_find: str):
    words = []
    find = 0
    mapping = {}

    with open(sys.argv[1], "r") as word_file:
        words = word_file.read().splitlines()

    print(words)

    edges = 0

    for i, w1 in enumerate(words):
        mapping[w1] = []
        for w2 in words:
            if compare(w1, w2) == 1:
                edges += 1
                mapping[w1].append(w2)
                if w1 == need_to_find:
                    find += 1
    print()
    print(mapping)

    edges /= 2

    print()
    print(f"There are {edges} edges.")
    print()
    print(f"\'{need_to_find}\' has {find} neighbors.")
    print()

    def bfs(graph: dict, start: str, goal: str):
        """uses graph as a dictionary to go fromstat to goal and find the shortest path between them
        method uses BFS but keeps track of them"""
        
        seen = []
        q = [[start]]
        
        while q:
            path = q.pop(0)
            node = path[-1]
            
            if node not in seen:
                neighbours = graph[node]
                
                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    q.append(new_path)
                    
                    if neighbour == goal:
                        print(*new_path)
                        return
                seen.append(node)
    
        print("no path")
        return
            
    (bfs(mapping, 'root', "tree"))
    (bfs(mapping, 'frog', "toad")) 
    (bfs(mapping, 'foal', "pony")) 
            

if __name__ == "__main__":
    main("word")
