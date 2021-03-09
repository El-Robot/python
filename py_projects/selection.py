import random
import time

def partition(arr, s, e, pivot):
        
        i = s + 1
        for j in range(s + 1,e):
                if arr[j] < pivot:
                        temp = arr[j]
                        arr[j] = arr[i]
                        arr[i] = temp
                        i += 1

        i -= 1
        arr[s] = arr[i]
        arr[i] = pivot  
        #print(arr)
        return i

def select(arr, n, i):
        if len(arr) <= 1:
                return arr[0]
        p = random.randrange(0,len(arr))
        pivot = arr[p]
        arr[p] = arr[0]
        arr[0] = pivot

        #print(str(pivot) + " looking for: " + str(i))

        j = partition(arr, 0, len(arr), pivot)

        if j == i:
                return arr[i]
        if j > i:
                return select(arr[:j], j - 1, i)
        if j < i:
                return select(arr[j+1:], n - j, i - j - 1)

def makeList(n):
    arr = []
    for i in range(n):
        arr.append(n - i)
    return arr

n = 10000000

array = makeList(n)

print("starting")
start = float(round(time.time() * 1000))
select(array, len(array), len(array)//2)
print("r select in ms: " + str(float(round(time.time() * 1000)) - start))

array = makeList(n)

#start = float(round(time.time() * 1000))
#insertion_sort(array)
#print("insertion sort in ms: " + str(float(round(time.time() * 1000)) - start))
