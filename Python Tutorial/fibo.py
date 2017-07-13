# fibonance numbers module

def fib(n):
	a, b = 0, 1
	while b < n:
		print(b, end=' ')
		a, b = b, a+b
	print()

def fib2(n):
	a, b = 0, 1
	rslt = []
	while b < n:
		rslt.append(b)
		a, b = b, a + b
	return rslt

if __name__ == '__main__':
	import sys
	fib(int(sys.argv[1]))
	print(fib2(int(sys.argv[2])))
