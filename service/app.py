from flask import Flask, render_template
import sqlite3


app = Flask(__name__)

# @ is a decorator which is a way to wrap a function and modifying its behavior
@app.route("/")
def main():
		return render_template("frontpage.html")


@app.route("/mainmenu")
def mainmenu():
	return render_template("mainmenu.html")

@app.route("/signup")
def signup():
	return render_template("signin.html")

@app.route("/session")
def sessionhub():
	return render_template("SessionHub.html")

@app.route("/basketball")
def basketball():
	return render_template("basketball.html")

@app.route("/football")
def football():
	return render_template("football.html")

@app.route("/soccer")
def soccer():
	return render_template("soccer.html")


if __name__ == "__main__":
	app.run(debug=True)