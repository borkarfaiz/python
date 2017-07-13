fw = open('sample.txt', 'w')
fw.write('i am jusst writing any thing\n you can write whatever you want\n but be carefull what are you writing')
fw.close()

fw = open('sample.txt', 'r')
print(fw.read())
fw.close()
