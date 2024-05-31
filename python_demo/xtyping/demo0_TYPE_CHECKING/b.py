import typing


if typing.TYPE_CHECKING:
    from a import A


class B:
    def __init__(self, a: "A"):
        self.a = a