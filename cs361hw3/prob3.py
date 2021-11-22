def prob3(c: list, w: list, W1: int, W2: int):
    n_t = len(c)
    memo = [[-1 for x in range(W2 + 1)] for y in range(n_t + 1)]

    def k(n, cap) -> int: 
        if memo[n][cap] != -1:
            return memo[n][cap]

        if n == 0 and cap > W2 - W1:
            return -1-c[n]
        
        elif n == 0 or cap == 0:
            return 0
        
        if w[n-1] > cap:
            return k(n - 1, cap)
        
        if w[n-1] <= cap:
            memo[n - 1][cap - w[n - 1]] = c[n - 1] + k(n -1, cap - w[n - 1])
            memo[n - 1][cap] = k(n - 1, cap)

            if memo[n - 1][cap - w[n - 1]] < 0 and n < n_t:
                memo[n - 1][cap - w[n - 1]] = -1-c[n]
            if memo[n - 1][cap] < 0 and n < n_t:
                memo[n - 1][cap] = -1-c[n]

            return max(memo[n - 1][cap - w[n - 1]], memo[n - 1][cap])
    
    return k(n_t, W2)


val = [100, 100, 2]
weights = [1, 2, 20]

print(prob3(val, weights, 3, 20))