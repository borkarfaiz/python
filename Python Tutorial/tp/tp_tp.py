import urllib.request

a = urllib.request.urlopen('https://www.w3.org/Style/Examples/011/firstcss.en.html')
b = (str(a.readlines()))
