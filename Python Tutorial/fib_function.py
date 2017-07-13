#this is a function to generate fibonnaci series

def fib(n): # write Fibonanci series upto n 
	"""Print a fibonanci series upto n."""
	a, b = 0,1
	while a < n:
		print(a,end=' ')
		a,b = b, a+b
	print()
n = int(input("Enter a number to find the fibonanci series of it: "))

fib(n)