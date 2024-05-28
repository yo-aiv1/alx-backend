#!/usr/bin/env python3

"""simple flask webapp"""

from flask_babel import Babel, gettext
from flask import Flask, render_template, request, g
from pytz import timezone
from pytz.exceptions import UnknownTimeZoneError


class Config(object):
    """lang config class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


myapp = Flask(__name__)
myapp.config.from_object(Config)
babel = Babel(myapp)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id: int) -> dict:
    """fetch user for me"""
    return users.get(user_id, {})


@myapp.before_request
def before_request() -> None:
    """gets user before handling request"""
    if bool(request.args):
        login_as = int(request.args.get('login_as'))
        user = get_user(login_as)
        g.user = user
    else:
        g.user = {}


@babel.localeselector
def get_locale() -> str:
    """set locale en"""
    locale = request.args.get("locale")
    lang = ["en", "fr"]
    loc = g.user
    if loc.get("locale") in lang:
        return loc.get("locale")
    if locale in lang:
        return locale
    return request.accept_languages.best_match(myapp.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """set local time zone"""
    time_zone = request.args.get("timezone")
    if time_zone is None:
        time_zone = g.user.get("timezone")
    if time_zone is not None:
        try:
            timezone(time_zone)
            return timezone
        except UnknownTimeZoneError:
            return "UTC"
    return "UTC"


@myapp.route("/")
def welcome() -> str:
    """
    render hello world
    """
    home_title = gettext("home_title")
    home_header = gettext("home_header")
    username = g.user
    username = username.get("name")
    return render_template('5-index.html',
                           home_title=home_title,
                           home_header=home_header,
                           username=username)


if __name__ == '__main__':
    myapp.run()
