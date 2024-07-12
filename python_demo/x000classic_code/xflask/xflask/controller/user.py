import logging
from flask import Blueprint


from .base import BaseControllerItem, BaseControllerGroup
from ..service import UserService


logger = logging.getLogger(__name__)
bp = Blueprint('user', __name__)


def init_bp(_bp: Blueprint):
    bp.add_url_rule('/user/<int:id>', view_func=UserItem.as_view('user-item'), endpoint='useritem')
    bp.add_url_rule('/user', view_func=UserGroup.as_view('user-group'), endpoint='usergroup')
    _bp.register_blueprint(bp)


class UserItem(BaseControllerItem):
    def __init__(self):
        self.service = UserService()


class UserGroup(BaseControllerGroup):
    def __init__(self):
        self.service = UserService()