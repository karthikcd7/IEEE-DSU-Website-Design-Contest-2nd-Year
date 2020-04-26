from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/events")
def events():
    return render_template("events.html")

if __name__=='__main__':
	app.run(debug=True)
