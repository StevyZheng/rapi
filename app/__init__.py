# -*- coding: utf-8 -*-
from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app=app)
    db.init_app(app=app)

    from .v1_0 import v1_0 as api_blueprint
    app.register_blueprint(api_blueprint)

    return app
