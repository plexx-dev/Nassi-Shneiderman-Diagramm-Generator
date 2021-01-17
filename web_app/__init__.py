from flask import Flask
from web_app.config import Config

app = Flask(__name__)

def create_app(config_class=Config):
    app.config.from_object(config_class)

    from web_app.main.routes import main
    from web_app.errors.handlers import errors
    
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app