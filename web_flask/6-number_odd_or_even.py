#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display():
    """creates dynamic routing"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display1():
    """creates static routing"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display2(text):
    """creates static routing"""
    text = text.replace("_", " ")
    return f"C {text}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display3(text):
    """creates static routing"""
    text = text.replace("_", " ")
    return f'Python {text}'


@app.route('/number/<int:n>', strict_slashes=False)
def display4(n):
    """displays only if n is an integer"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def display5(n):
    """displays using rendered template"""
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display6(n):
    """displays whether n is odd or even"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(debug=True)
