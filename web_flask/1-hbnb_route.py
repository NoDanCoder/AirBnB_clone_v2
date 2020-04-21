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


if __name__ == '__main__':
    """ Entry point """
    app.run(host='0.0.0.0', port=5000)
