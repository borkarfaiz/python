def pyramid(number):
	for i in range(1, number+1):
		c = (number + 10) - i
		while c!=0:
			print(end=" ")
			c-=1
		for j in range(1, i+1):
			print(j, end='')
		for k in range(i-1,0,-1):
			print(k, end='')

		print('\n')

number = int(input('Enter a number               '))
pyramid(number)
