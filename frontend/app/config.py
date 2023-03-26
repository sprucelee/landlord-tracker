import os
import uuid


class Config(object):
    TESTING = False


class DevelopmentConfig(Config):
    SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", uuid.uuid4().hex)
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    ...


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    TESTING = True


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
}

config["default"] = config.get(os.environ.get("ENVIRONMENT", ""), DevelopmentConfig)
