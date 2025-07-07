from flask import Flask
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

from ..models import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))
    # email = db.Column(db.String(120), unique=True)

    def __repr__(self):
        return '<User %r>' % self.username