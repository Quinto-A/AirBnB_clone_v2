#!/usr/bin/python3
"""script that starts a Flask web apllication"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def display():
    """Creates dynamic routing"""
    return "Hello HBNB!"


@app.route("/HBNB", strict_slashes=False)
def display1():
    """creates static routing"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display2(text):
    """Creates static routing"""
    text = text.replace("_", " ")
    return f'C {text}'


if __name__ == "__main__":
    app.run(debug=True)
