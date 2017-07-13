def binarySearch(alist, item):
	if len(alist) == 0:
		return False
	else:
		midpoint = len(alist) // 2
		if alist[midpoint] == item:
			return midpoint
		elif item < alist[midpoint]:
			return binarySearch(alist[:midpoint],item)
		else:
			return binarySearch(alist[midpoint+1:], item)

a = [1, 4, 6, 12, 15, 17, 21, 25, 27, 31, 36, 39, 67]
print(binarySearch(a, 27))