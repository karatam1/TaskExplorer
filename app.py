from flask import Flask, redirect, url_for, render_template, request
from think import *

app = Flask(__name__)

@app.route("/")

def home():
    return render_template("index.html")

@app.route("/base", methods=["POST", "GET"])
def login():

    if request.method == "POST":
        user = request.form["nm"]
        command = find(user)
        if command != "unknown":
            cmd = command+".html"
            return render_template(cmd)
        else:
            return render_template("base.html")
    else:
        return render_template("base.html")


@app.route("/music")
def music():
    return render_template("music.html")

@app.route("/photos")
def photo():
    return render_template("photos.html")


@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"



if __name__ == "__main__":
    app.run(debug=True)
