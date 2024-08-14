from flask import Flask
from orm_demo1.config import FLASK_HOST, FLASK_PORT
from orm_demo1.services import UserService

app = Flask(__name__)
user_service = UserService()

@app.route('/')
def index():
    users = user_service.get_all_users()
    return str(users)

if __name__ == '__main__':
    app.run(host=FLASK_HOST, port=FLASK_PORT)