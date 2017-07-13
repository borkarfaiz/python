def params(oldFunc):
	def inside(*args, **kwargs):
		print("Params : ", args, kwargs)
		return oldFunc(*args, **kwargs)
	return inside

@params
def Mult(x, y=10):
	print(x * y)

Mult(4)
Mult(x=5,y=1)
Mult(4,12)
