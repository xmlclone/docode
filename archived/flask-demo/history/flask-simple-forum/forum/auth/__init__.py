from flask import Flask
from flask_login import LoginManager
from ..models.user import User


login_manager = LoginManager()


def configure_auth(app: Flask):
    login_manager.init_app(app)
    login_manager.login_view = 'login'
    login_manager.login_message = '请先登录'

    @login_manager.user_loader
    def load_user(user_id):
        user = User.query.get_or_404(user_id)
        return user