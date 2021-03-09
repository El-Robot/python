import random

def partition(arr, s, e, pivot):
        i = s + 1
        for j in range(s + 1,e):
                if arr[j] < pivot:
                        temp = arr[j]
                        arr[j] = arr[i]
                        arr[i] = temp
                        i += 1
                #print(arr)

        arr[s] = arr[i-1]
        arr[i-1] = pivot

        return i

def qsort(arr, s, e):
        if len(arr[s:e]) <= 1:
                return
        
        rand = random.randint(s,e-1)
        #pivot = arr[s]

        pivot = arr[rand]
        arr[rand] = arr[s]
        arr[s] = pivot

        i = partition(arr, s, e, pivot)
        
        qsort(arr, s, i-1)

        qsort(arr, i, e)


def randarray(n):
        # TODO: Use Lamda
        arr = []
        for i in range(n):
                arr.append(random.randint(0,2*n))
        return arr

if __name__ == "__main__":
        a = randarray(int(input("enter len:")))
        #start = time
        print(a)
        qsort(a, 0, len(a))
        print(a)

