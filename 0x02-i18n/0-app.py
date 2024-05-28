#!/usr/bin/env python3

"""simple flask webapp"""

from flask import Flask, render_template


myapp = Flask(__name__)


@myapp.route("/")
def welcome() -> str:
    """
    render hello world
    """
    return render_template("0-index.html")


if __name__ == '__main__':
    myapp.run()
