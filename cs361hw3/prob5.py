def prob5(L, R):
    result = [[-1] * (R+1) for _ in range(L+1)]

    for l in range(L + 1):
        result[l][0] = 0

    for r in range(R + 1):
        result[0][r] = 0

    for l in range(1, L + 1):
        for r in range(1, R + 1):
            if r - 5 >= 0 and result[l][r-5] == 0:
                result[l][r] = 1
            elif r - 2 >= 0 and result[l][r-2] == 0:
                result[l][r] = 1
            elif l - 2 >= 0 and result[l-2][r] == 0:
                result[l][r] = 1
            elif result[l - 1][r] == 0:
                result[l][r] = 1
            elif result[l][r - 1] == 0:
                result[l][r] = 1
            else:
                result[l][r] = 0

    return result[L][R]

print("100,100 => " + str(prob5(100, 100)))
