import logging


from .base import BaseControllerItem, BaseControllerGroup
from ..service import UserService


logger = logging.getLogger(__name__)


class UserItem(BaseControllerItem):
    def __init__(self):
        self.service = UserService()


class UserGroup(BaseControllerGroup):
    def __init__(self):
        self.service = UserService()