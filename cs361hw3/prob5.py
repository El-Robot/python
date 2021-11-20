def prob5(L,R):
    prob5.turn = 0
    result = [[-1] * R for _ in range(L)]
    print(result)

    def V(l, r):
        turn = (prob5.turn + 1) % 2

        if l <= 0 or r <= 0:
            return 0

        
        if l >= 1 and result[l-1][r] == -1:
            result[l-1][r] = (V(l-1,r) + 1) % 2

        if l >= 2 and result[l-2][r] == -1:
            result[l-2][r] = (V(l-2,r) + 1) % 2

        if r >= 2 and result[l][r-2] == -1:
            result[l][r-2] = (V(l,r-2) + 1) % 2

        if r >= 5 and result[l][r-5] == -1:
            result[l][r-5] = (V(l,r-5) + 1) % 2

        if result[l-1][r] == turn or result[l-2][r] == turn or result[l][r-2] == turn or result[l][r-5] == turn:
            return turn
        else:
            return (turn + 1) % 2

    return V(L-1,R-1)

print(str(prob5(3,3)))
        
        
