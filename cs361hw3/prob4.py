def prob4(r_or_b: list):
    n = len(r_or_b)
    sizes = [[0] * n for _ in range(n)]
    for c in range(n):
        if r_or_b[0][c] == 1:
            sizes[0][c] = 1
    for r in range(n):
        if r_or_b[r][0] == 1:
            sizes[r][0] = 1
    for r in range(1, n):
        for c in range(1, n):
            if r_or_b[r][c] == 1:
                sizes[r][c] = 1 + min(sizes[r][c - 1],sizes[r - 1][c],sizes[r - 1][c - 1])
    max_in_row = [0] * n
    for r in range(0, n):
        max_in_row[r] = max(sizes[r])
    return max(max_in_row)

input = [
    [0,1,1,1,1,1],
    [0,1,1,1,1,1],
    [0,1,1,1,1,1],
    [0,1,1,1,1,1],
    [0,1,1,1,1,1],
    [0,1,0,1,1,1]
]
print(prob4(input))