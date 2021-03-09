def sort(a):
	for i in range(1,len(a)):
		num = a[i]
		j = i
		while j > 0:
			if a[j - 1] > num:
				a[j] = a[j - 1]
				a[j - 1] = num
				j -= 1
			else:
				break
	print(a)
	
arr = [1,2,3,4,6,7,5]
sort(arr)
input('stop')