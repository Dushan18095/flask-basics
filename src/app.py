import os

from flask import Flask, request
import src.functions as f


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'Hello, World!'

    @app.route('/factorize')
    def factorize():
        number = request.args.get('number')
        return f.factorize(int(number))

    @app.route('/number-of-digits')
    def number_of_digits():
        number = request.args.get('number')
        return str(f.number_of_digits(int(number)))
    return app