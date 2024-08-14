from flask import Flask
from flask import request_started, request_finished


app = Flask(__name__)


@app.route('/')
def index():
    return 'Index'


