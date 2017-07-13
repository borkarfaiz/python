import re

f = open('random.txt')

strToSearch = ''

for line in f:
	strToSearch += line


patFinder2 = re.compile('[a-z]', re.IGNORECASE)

findPat2 = re.findall(patFinder2, strToSearch)

for i in findPat2:
	print(i)