from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/home/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/home/events")
def events():
    return render_template("events.html")

@app.route("/home/events/events01")
def events01():
    return render_template("events01.html")

@app.route("/home/events/events02")
def events02():
    return render_template("events02.html")

@app.route("/home/events/events03")
def events03():
    return render_template("events03.html")

@app.route("/home/execom")
def execom():
    return render_template("execom.html")

@app.route("/home/committee")
def committee():
    return render_template("committee.html")


if __name__=='__main__':
	app.run(debug=True)
