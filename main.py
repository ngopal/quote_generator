from flask import Flask, url_for, render_template

DATABASE = 'quotes.db'

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('main.html')

if __name__ == "__main__":
	app.run()
