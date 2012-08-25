import sqlite3

file = open('quotes_file.txt', 'r')

line = ''
quotes = []
for i in  file.readlines():
	if i == '\r\n':
		print "BLANK", i
		quotes.append(line)
		line = ''
	else:
		print "CONTENT", i
		line = line + ' ' + i.strip('\r\n')

conn = sqlite3.connect('quotes.db')
c = conn.cursor()
c.execute('''CREATE TABLE quotes(id int, quote text)''')

for i in range(len(quotes)):
	cleaned_string = quotes[i].replace("'", r"\'")
	comm = "INSERT INTO quotes VALUES ("+str(i)+", \'"+str(cleaned_string)+"\')"
	print i, quotes[i]
	print comm
	try:
		c.execute(comm)
	except:
		print 'apostraphe error'
		pass

conn.commit()
c.close()

