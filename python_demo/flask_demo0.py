'''
pip install flask==3.0.0


flask --app flask_demo0.py run --debug
'''

from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return "Index"


@app.route("/json")
def response_json():
    return {
        "name": "lin",
        "age": 10,
        "like": ["sport", "read"]
    }


