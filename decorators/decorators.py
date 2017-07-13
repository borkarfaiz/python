import os

def exists(oldFunc):
	def inside(filenmae):
		if(os.path.exists(filenmae)):
			print('Teri to ')
		#	oldFunc(filenmae)
		else:
			print("The File Does Not Exist")
	return inside

@exists
def outputline(inFile):
	with open(inFile) as f:
		print(f.readlines())


# without decorator
# func = exists(outputline)
# func('decorators.py')
# func('test.py')

# calling with decorator
# outputline('test.py')
outputline('decorators.py')
