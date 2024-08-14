'''
pip install flask==3.0.0
flask --app demo0.py run --debug


pip install waitress
waitress-serve --host 127.0.0.1 hello:app
waitress-serve --host 127.0.0.1 --call hello:create_app
'''


from flask import Flask
from waitress import serve


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


serve(app)
