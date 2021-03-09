import random

def find_pair_sum_ordered(arr, sum):
    "finds pair of numbers that add up to 'sum' in a sorted array"
    print("finding: %i" % (sum))
    right = len(arr) - 1
    left = 0
    for i in arr:
        print("R: " + str(right) + "   L: " + str(left))
        if arr[left] + arr[right] == sum:
            return True
        if arr[left] + arr[right] > sum:
            right -= 1
        if arr[left] + arr[right] < sum:
            left += 1
        if right == left:
            return False
    return False

def find_pair_sum(arr, sum):
    "finds pair of numbers that add up to 'sum' in any array"
    prev = set()
    for i in arr:
        if sum - i in prev:
            return True
        prev.add(i)
    return False
    

def make_array(n, max):
    arr = []
    for i in range(n):
        arr.append(random.randint(1,max))
    #sort(arr)
    return arr

def merge(arr, left, right):
    a = l = r = 0
    while l < len(left) and r < len(right):
        if left[l] > right[r]:
            arr[a] = right[r]
            r += 1
        else:
            arr[a] = left[l]
            l += 1
        a += 1

    while l < len(left):
        arr[a] = left[l]
        l += 1
        a += 1

    while r < len(right):
        arr[a] = right[r]
        r += 1
        a += 1

def sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2

        l = arr[:mid]
        r = arr[mid:]
        
        sort(l)
        sort(r)

        merge(arr, l, r)
        

a = make_array(10, 15)

print(a)
print(find_pair_sum(a, 25))
