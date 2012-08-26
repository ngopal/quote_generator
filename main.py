from flask import Flask, url_for, render_template, g
import random

DATABASE = 'quotes.db'

app = Flask(__name__)

def connect_db():
	return sqlite3.connect(DATABASE)

def get_connection():
	db  = getattr(g, '_db', None)
	if db is None:
		db = g._db = connect_db()
	return db

def query_db(query, args=(), one=False):
	cur = g.db.execute(query, args)
	rv = [dict((cur.description[idx][0], value) for idx, value in enumerate(row)) for row in cur.fetchall()]
	return (rv[0] if rv else None) if one else rv

@app.route('/')
def index():
	def generate_quote():
		index = str(random.randint(0,640))
		randquery = 'SELECT * FROM quotes'
		for k in query_db(randquery):
			print k
		return randquery 
	try:
		quote = generate_quote()
	except:
		quote = 'Random Quote Goes Here'
	return render_template('main.html', quote=quote)

@app.route('/quote/<id>')
def show_quote_by_id(id):
	return 'Quote by ID %s' % id

if __name__ == "__main__":
	app.debug = True
	app.run()
