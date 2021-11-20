def prob1(squares: list):
    if len(squares) < 3:
        return squares[1]
    weights = [0] * len(squares)
    weights[0] = squares[0]
    weights[1] = 0
    weights[2] = squares[0] + squares[2]
    for i in range(3, len(squares)):
        weights[i] = max(weights[i-2], weights[i-3]) + squares[i]
    return max(weights)

input = [0,0,0,3,1,1,2,1,1,10]
print(str(prob1(input)))
