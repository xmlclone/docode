from typing import final


# 注意：只影响静态检查工具，并不影响实际的执行


class Base:
    @final
    def done(self) -> None:
        ...
class Sub(Base):
    def done(self) -> None:  # Error reported by type checker
        ...


@final
class Leaf:
    ...
class Other(Leaf):  # Error reported by type checker
    ...