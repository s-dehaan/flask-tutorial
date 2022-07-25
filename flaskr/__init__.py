"""This module is the Application Factory."""
import os

from flask import Flask

def create_app(test_config=None):
    """Creating the app."""

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='development',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )

    # Load the instance config, if it exists, else the test config
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # Make sure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'hello'

    return app
