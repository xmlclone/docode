'''
flask --app server1.py run --debug
'''

import time
from random import randint
from flask import Flask

app = Flask(__name__)


@app.route('/api/v1/f1')
def f1():
    return 'f1'

@app.route('/api/v1/f2')
def f2():
    time.sleep(2)
    return 'f2'