from werkzeug.exceptions import HTTPException
from werkzeug.sansio.response import Response


class UnkonwnError(HTTPException):
    code = 800
    description = 'unkonwn error.'


class AddObjectError(HTTPException):
    code = 801

    def __init__(self, description: str | None = None, response: Response | None = None, data=None) -> None:
        super().__init__(description, response)
        self.description = f'Add {data} failed.'


class DeleteObjectError(HTTPException):
    code = 802

    def __init__(self, description: str | None = None, response: Response | None = None, data=None) -> None:
        super().__init__(description, response)
        self.description = f'Delete {data} failed.'


class UpdateObjectError(HTTPException):
    code = 803

    def __init__(self, description: str | None = None, response: Response | None = None, data=None) -> None:
        super().__init__(description, response)
        self.description = f' Update {data} failed.'


class LoginFailed(HTTPException):
    code = 851
    description = "Login failed."


class NeedLogin(HTTPException):
    code = 852
    description = "Need login first."