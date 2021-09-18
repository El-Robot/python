def main():
    totalCases = int(input())
    count = 1
    while count <= totalCases:
        rawInput = list(input())
        numberInput = [int(num) for num in rawInput]
        depth = 0
        result = ""
        
        for num in numberInput:
            while num > depth:
                result += "("
                depth += 1
            while num < depth:
                result += ")"
                depth -= 1
            
            result += str(num)

        while depth > 0:
                result += ")"
                depth -= 1
        
        print("Case #%d: %s" % (count, result))

        count += 1
    
if __name__ == "__main__":
    main()
