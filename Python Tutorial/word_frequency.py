import requests
from bs4 import BeautifulSoup
import operator

def start(url):
	print('\n\n\n')
	word_list = []
	source_code = requests.get(url).text
	soup = BeautifulSoup(source_code)
	for post_text in soup.findAll('a'):
		content = post_text.string
		print(content)
	#	words = content.split()
	#	for each_word in words:
	#		print(each_word)
	#		word_list.append(each_word)

start('http://mp4mania.org/index.php')