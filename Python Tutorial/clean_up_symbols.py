word_list = list('how are##$ you@! i an2#&^^ seeing#@ y@O#u after a lin#1g t!I#ne'.split(' '))
print(word_list)

def clean_up(word_list):
	
	clean_uped_list = list()
	for word in word_list:
		print(word)
		symbols = '!@#$%^&*()_+=-<>?'
		for i in range(0, len(symbols)):
			print()
		clean_uped_list.append(word)
print(clean_up(word_list))