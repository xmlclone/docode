from flask import Flask
from .views.main import index
from .views.auth import login, logout, register


def configure_urls(app: Flask):
    app.add_url_rule('/', view_func=index)
    app.add_url_rule('/login', view_func=login)
    app.add_url_rule('/logout', view_func=logout)
    app.add_url_rule('/register', view_func=register)