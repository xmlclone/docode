from typing import Type
from .base import Dao
from ..model.user import UserDB
from ..model.user import UserPy


class UserDao(Dao):

    def __init__(self):
        super().__init__(UserDB, UserPy)