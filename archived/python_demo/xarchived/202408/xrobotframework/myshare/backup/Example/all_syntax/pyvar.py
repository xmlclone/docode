class VarObj:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name


OBJ_VAR = VarObj("rf")
INT_VAR = 2