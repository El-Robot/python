# Agorithms and Data Structures 2 (cs 362)

# 4 techniques for algorithm design:
# Recursion
#   breaking down a complex problem to a set of simple problems
#   Merge sort
# Induction
#   starting with simple situations
#   dynamic programming (DP)
#   Djkistas algortithm - only works on graphs with positive edge cost
#   ussually if you cant source/sort? something then you can use induction
# Reduction
#   not reinventing the wheel
#   tranform the problem into something we already know how to solve
#   in the context of NP-Completeness
# Randomization 
#   How to defeat the adversaries -- fights the bias of sampling
#   

def main() -> None:
    print(fib(9999))

def euclid(a:int, b:int) -> int:
    """
    Exlpanation
    -----------
    Let a, b elem of Z+, a > b 

    Returns the GCD of a and b
    """
    r = a % b
    if r == 0:
        return b
    else:
        return euclid(b, r)

def euclid_loop(a:int, b:int) -> int:
    """
    Exlpanation
    -----------
    Let a, b elem of Z+, a > b 

    Returns the GCD of a and b
    """
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b

# Euclids algorithm Big-O
# Observations: a = q*b + r; r = a % b; then r < a/2
# 

def fib(n:int) -> int:
    a = 1
    b = 1
    for i in range(n):
        a = a + b
        b = a
    return a

if __name__ == "__main__":
    main()