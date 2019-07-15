import os

from flask import Flask

def create_app(test_config=None):
    # Create and configure the app
    # instance_relative_config = tells the app that configuration files are 
    #relative to the instance folder.
    app = Flask(__name__, instance_relative_config=True)


    app.config.from_mapping(SECRET_KEY='dev', 
    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),)

    # overrides the default configuration with values taken 
    # from the config.py file in the instance folder if it exists.
    # When a real key is set for example
    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
