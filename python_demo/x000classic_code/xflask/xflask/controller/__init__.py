from flask import Flask

from .user import UserGroup, UserItem
from .auth import login, logout
from ..service.auth import load_user


def init_app(app: Flask):
    # as_view 后面可以跟参数，参数都是传递给对应 View 的 __init__ 的
    app.add_url_rule('/api/user/<int:id>', view_func=UserItem.as_view('user-item'))
    app.add_url_rule('/api/user', view_func=UserGroup.as_view('user-group'))

    app.add_url_rule('/api/login', 'login', login, methods=['POST'])
    app.add_url_rule('/api/logout', 'logout', logout, methods=['POST'])
    
    app.before_request(load_user)