__author__ = "Jeremy Nelson"

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<path:name>/")
def topic(name):
    return render_template("{}.html".format(name))

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    from elsa import cli
    app.run(host='0.0.0.0', debug=True, port=9180)
