def main():
    totalMatrixes = int(input())
    count = 1
    while count <= totalMatrixes:
        
        n = int(input())
        matrix = []
        for i in range(n):
            row = input()
            matrix.append(row.split(' '))
            for j in range(n):
                matrix[i][j] = int(matrix[i][j])
            
        trace = 0
        for i in range(n):
            trace += matrix[i][i]
        
        rowRep = 0
        for row in range(n):
            seen = set()
            for index in range(n):
                if matrix[row][index] in seen:
                    rowRep += 1
                    break
                seen.add(matrix[row][index])
                
        colRep = 0
        for col in range(n):
            seen = set()
            for index in range(n):
                if matrix[index][col] in seen:
                    colRep += 1
                    break
                seen.add(matrix[index][col])
        
        print('Case #%d: %d %d %d ' % (count, trace, rowRep, colRep))
        
        count += 1
    
if __name__ == "__main__":
    main()