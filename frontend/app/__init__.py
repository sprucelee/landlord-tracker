from flask import Flask
from flask_bootstrap import Bootstrap5

from .config import config


def create_app(config_name="default"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    Bootstrap5(app)

    from .models import db

    db.init_app(app)

    from .main import main

    app.register_blueprint(main, url_prefix="/")

    return app
