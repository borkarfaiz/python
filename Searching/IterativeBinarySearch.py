def IterativeBinarySearch(a, key):
	low = 0
	high = len(a)
	while (low <= high):
		mid = (low + high) // 2
		if a[mid] == key:
			return mid
		elif key  < a[mid]:
			high = mid - 1
		else:
			low = mid + 1
	return -1


a = [1, 4, 6, 12, 15, 17, 21, 25, 27, 31, 36, 39, 67]
print(a)
key = int(input("Enter the Number to find\t"))
index = IterativeBinarySearch(a, key)
if index != -1:
	print("The Element is found at location\t", index)
else:
	print("The Element is not in the list")