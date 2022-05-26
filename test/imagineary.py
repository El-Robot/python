def nth(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    return nth(n-1)*nth(n-2)

def nth2(n):
    a0 = 1
    a1 = 2
    while n >= 2:
        temp = a0*a1
        a0 = a1
        a1 = temp
        n = n - 1
    return a1

def main():

    for i in range(10):
    
        print(str(nth(i)))

if __name__ == "__main__":
    main()
