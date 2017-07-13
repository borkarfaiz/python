import webbrowser as wb 
codechef = ['www.google.com', 'www.facebook.com', 'www.gmail.com']
django = ['https://www.djangoproject.com/start/']
def hi(m):
	for i in m:
		wb.open_new_tab(i)

a = int(input("""Which mode in you want to open
			1.CodeChef
			2.Django
			3.bootstrap4
						"""))

if a==1:
	hi(codechef)
elif a==2:
	hi(django)

