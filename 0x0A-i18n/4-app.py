#!/usr/bin/env python3
""" flask simple api """
from flask import Flask, render_template
from flask_babel import Babel, gettext, request

app = Flask(__name__)
babel = Babel(app)


class Config():
    """ babel config class """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def hello():
    """ Hello world """
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    """ determine the best match with supported languages """
    locale = request.args.get("locale")
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
