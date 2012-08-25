from flask import Flask, url_for, render_template, g
import random

DATABASE = 'quotes.db'

app = Flask(__name__)

def connect_db():
	return sqlite3.connect(DATABASE)

def query_db(query, args=(), one=False):
	cur = g.db.execute(query, args)
	rv = [dict((cur.description[idx][0], value) for idx, value in enumerate(row)) for row in cur.fetchall()]
	return (rv[0] if rv else None) if one else rv

@app.route('/')
def index():
	quote = 'Random Quote Goes Here'
	return render_template('main.html', quote=quote)

if __name__ == "__main__":
	app.run()
