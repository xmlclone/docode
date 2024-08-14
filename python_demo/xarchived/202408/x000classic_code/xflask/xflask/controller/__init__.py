from flask import Flask, Blueprint

from ..service.auth import load_user


bp = Blueprint('api', __name__)


def register_blueprint():
    from .user import init_bp as user_init_bp
    from .auth import init_bp as auth_init_bp
    for blueprint in [
        user_init_bp,
        auth_init_bp,
    ]:
        blueprint(bp)


def init_app(app: Flask):
    # as_view 后面可以跟参数，参数都是传递给对应 View 的 __init__ 的
    # app.add_url_rule('/v1/api/user/<int:id>', view_func=UserItem.as_view('user-item'), endpoint='useritem')
    # app.add_url_rule('/v1/api/user', view_func=UserGroup.as_view('user-group'), endpoint='usergroup')

    # app.add_url_rule('/v1/api/login', view_func=login, methods=['POST'], endpoint='login')
    # app.add_url_rule('/v1/api/logout', view_func=logout, methods=['POST'], endpoint='logout')

    register_blueprint()
    app.register_blueprint(bp, url_prefix='/v1/api')
    
    app.before_request(load_user)