from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

# initializing application
def create_app(config_name):

    app = Flask(__name__)

# setting up configuration
    app.config.from_object(config_options[config_name])

# initializing flask extensions
    bootstrap.init_app(app)

# registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app



