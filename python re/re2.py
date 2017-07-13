import re 

f = open('random.txt')

strToSearch = ""

for line in f:
	strToSearch += line

print(strToSearch)

patFinder1 = re.compile('a+$')

findPat = re.search(patFinder1, strToSearch)

print(re.findall(patFinder1, strToSearch))

