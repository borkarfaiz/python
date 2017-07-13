import re

reg = re.compile(r'^(\w|_)+[\d|\w|_]*$')

def demo_bad_catch():
	try:
		var = input("Enter variable name")
		if re.find(reg, var):
			print('The input is valid')
	except ValueError as e: