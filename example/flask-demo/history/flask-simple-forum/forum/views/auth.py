from flask import render_template


def login():
    return render_template('login.html')


def logout():
    return render_template('logout.html')


def register():
    return render_template('register.html')