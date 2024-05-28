#!/usr/bin/env python3

"""simple flask webapp"""

from flask_babel import Babel, gettext
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
    """set locale en"""
    locale = request.args.get("locale")
    lang = ["en", "fr"]
    if locale in lang:
        return locale
    return request.accept_languages.best_match(myapp.config['LANGUAGES'])


@myapp.route("/")
def welcome() -> str:
    """
    render hello world
    """
    home_title = gettext("home_title")
    home_header = gettext("home_header")
    return render_template('4-index.html',
                           home_title=home_title,
                           home_header=home_header)


if __name__ == '__main__':
    myapp.run()
