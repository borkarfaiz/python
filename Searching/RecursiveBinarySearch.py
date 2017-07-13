def RecursiveBinarySearch(a, key, low, high):
	if(low > high):
		return -1
	mid = (low + high) // 2
	if key == a[mid]:
		return mid
	elif key > a[mid]:
		RecursiveBinarySearch(a, key, mid+1, high)
	else:
		RecursiveBinarySearch(a, key, low, mid - 1)


a = [1, 4, 6, 12, 15, 17, 21, 25, 27, 31, 36, 39, 67]
key = int(input("Enter the key to found"))
low, high = 0, len(a)-1
print(RecursiveBinarySearch(a, key, low, high))