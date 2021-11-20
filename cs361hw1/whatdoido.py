a = [4,-1]

def whatdoido(left, right):
    if left == right:
        if a[left] < 0:
            return [0,0,0,a[left]]
        else:
            return [a[left],a[left],a[left],a[left]]
    if left < right:
        m = (left+right)//2
        l = whatdoido(left,m)
        r = whatdoido(m + 1, right)
        maxsum = max(l[0], r[0], r[1] + l[2])
        la = max(l[1], l[3] + r[1])
        ra = max(r[2], r[3] + l[3])
        sum = r[3] + l[3]
        return [maxsum, la, ra, sum]

print(whatdoido(0,len(a)-1))
