from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('main.html')

@app.route("/login")
def login():
	return render_template('login.html')

@app.route("/changepwd")
def changepwd():
	return render_template('changepwd.html')

@app.route("/register")
def register():
	return render_template('register.html')

@app.route("/feature")
def feature():
	return render_template('feature.html')

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000, debug=True)
