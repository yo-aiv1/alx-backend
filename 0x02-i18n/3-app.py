#!/usr/bin/env python3

"""simple flask webapp"""

from flask_babel import Babel
from flask import Flask, render_template, request


class Config(object):
    """lang config class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


myapp = Flask(__name__)
myapp.config.from_object(Config)
babel = Babel(myapp)


@babel.localeselector
def get_locale() -> str:
    """Retrieves the locale for a web page.
    """
    return request.accept_languages.best_match(myapp.config["LANGUAGES"])


@myapp.route("/")
def welcome() -> str:
    """
    render hello world
    """
    return render_template("0-index.html")


if __name__ == '__main__':
    myapp.run()
