import webbrowser as wb
l = ['codechef.txt',]

def wb_open(name):
	with open(name, 'r') as f:
		urls = f.readlines()
		f.close()
	for i in urls:
		wb.open_new_tab(i)

a = int(input("""
			1.codechef
			2.django
			3.how
				  : """))


wb_open(l[0])