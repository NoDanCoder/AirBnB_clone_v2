#!/usr/bin/python3
""" Set up Flash Web Application """
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ return msg to GET request """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """ return msg to GET request, path in /hbnb """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """ return msg to GET request, path in /c/<var> """
    return "C " + text.replace("_", " ")


@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def display_python(text="is cool"):
    """ return msg to GET request, path in /python/<var> """
    return "Python " + text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def number_check(n):
    """ return msg to GET request, path in /number/<var> if int """
    return "{} is a number".format(n)


if __name__ == '__main__':
    """ Entry point """
    app.run(host='0.0.0.0', port=5000)
