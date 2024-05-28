#!/usr/bin/env python3

"""simple flask webapp"""

from flask import Flask, render_template
from flask_babel import Babel


myapp = Flask(__name__)
babel = Babel(myapp)


class Config(object):
    """lang config class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


myapp.config.from_object(Config)


@myapp.route("/")
def welcome() -> str:
    """
    render hello world
    """
    return render_template("0-index.html")


if __name__ == '__main__':
    myapp.run()
