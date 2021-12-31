def find_k(graph):
    
    seen = set()

    def bfs(start: str, graph: dict):
        seen.add(start)
        q = [start]
        
        while q:
            node = q.pop(0)
            
            for i in graph[node]:
                if i not in seen:
                    q.append(i)
                    seen.add(i)
        return
    
    count_connected = 0
    for node in graph.keys():
        if node not in seen:
            count_connected += 1
            bfs(node, graph)

    print(f"you need to add {count_connected - 1} edges")


def main():
    graph = {
        '1': ['2'],
        '2': ['1', '4', '6'],
        '3': [],
        '4': ['2', '6', '5'],
        '5': ['4'],
        '6': ['4','2'],
        '7': ['8','9'],
        '8': ['7'],
        '9': ['10','7'],
        '10': ['9']
    }
    find_k(graph)


if __name__ == "__main__":
    main()
