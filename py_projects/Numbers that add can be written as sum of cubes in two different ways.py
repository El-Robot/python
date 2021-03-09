i = 2
s = {8}

while True:
    num = i**3 + 1
    s.add(i**3)
    for n in range(2, i):
        
        if ( num - n**(3) ) in s:
            print("HERE:  " + str(num))
    
    i+=1
