from flask import Flask, render_template


def index():
    return render_template('index.html')


def init_app(app: Flask):
    app.add_url_rule('/', view_func=index)