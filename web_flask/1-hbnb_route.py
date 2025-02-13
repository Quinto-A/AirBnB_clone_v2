#!/usr/bin/python3
"""script that starts a Flask web apllication"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def display():
    """Creates dynamic routing"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def display1():
    """creates static routing"""
    return "HBNB"


if __name__ == "__main__":
    app.run(debug=True)
