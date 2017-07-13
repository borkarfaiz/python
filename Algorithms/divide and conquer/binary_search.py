def binarysearch(alist, item):
	first = 0
	last = len(alist) - 1
	found = False

	while first<=last and not found:
		midpoint = (first+last)//2
		if alist[midpoint] == item:
			found = True
		elif alist[midpoint] < item:
			first = midpoint + 1
		else:
			last = midpoint - 1

	if found:
		return midpoint + 1
	return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarysearch(testlist, 25,))
print(binarysearch(testlist, 42,))
print(binarysearch(testlist, 19,))

