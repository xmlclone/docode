from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def configure_models(app: Flask):
    db.init_app(app)


