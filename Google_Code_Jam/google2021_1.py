def reversort(l):
    for i in range(len(l)):
        
        if (l == sorted(l)):
            return 0
        
        j = l.index(min(l))
        l[i-1:j] = reversed(l[i-1:j])
        return (j - i + 1) + reversort(l)

def main():
    totalCases = int(input())
    count = 1
    while count <= totalCases:
        input()
        rawInput = list(input().split(' '))
        numberInput = [int(num) for num in rawInput]
        depth = 0
        result = ""
        
        result = reversort(numberInput)
        
        print("Case #%d: %s" % (count, result))

        count += 1
    
if __name__ == "__main__":
    main()