import urllib.request
from bs4 import BeautifulSoup
#a = urllib.request.urlopen('https://www.w3.org/Style/Examples/011/firstcss.en.html')
#c = (a.read())
#print(c)
#print('\n\n\n\n\n\n\n\n\n\n\n\n\n')

b = html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

print(type(b))
print('\n\n\n\n')
soup = BeautifulSoup(b, 'html.parser')
print(type(soup))
print('\n\n\n\n')
print(soup.prettify)
