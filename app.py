<<<<<<< HEAD
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


if __name__=='__main__':
	app.run(debug=True)
=======
from Flask import flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

>>>>>>> c10143bd052b4c6291b7faec7285b96cdf79d854
