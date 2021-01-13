from flask import Flask
from Web.config import Config

app = Flask(__name__)

def create_app(config_class=Config):
    app.config.from_object(config_class)

    from Web.main.routes import main

    app.register_blueprint(main)

    return app