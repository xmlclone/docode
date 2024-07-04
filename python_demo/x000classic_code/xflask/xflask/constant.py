from enum import Enum


class ResponseStatus(Enum):
    success = 0
    fail = 1
    unkonwn = 2


class UserRole(Enum):
    admin = 'admin'
    user = 'user'