def Bsearch(a, x, low, high):
	if(low > high):
		return -1
	mid = (low + high) // 2
	if a[mid] == x:
		return mid
	elif a[mid] < x:
		return Bsearch(a, x, mid+1, high)
	else:
		return Bsearch(a, x, low, high - 1)

a = [1, 4, 6, 12, 15, 17, 21, 25, 27, 31, 36, 39, 67]
low = 0
high = len(a)-1
x = int(input("Enter the key to found:  "))
index = (Bsearch(a, x, low, high))
if index !=-1:
	print("The Element " +str(x) + " is found at locatiion " +str(index))
else:	
	print("the Element is not in the list")