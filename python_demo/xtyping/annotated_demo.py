from typing import Annotated
from dataclasses import dataclass


@dataclass
class ValueRange:
    lo: int
    hi: int


T1 = Annotated[int, ValueRange(-10, 5)]


def f1(a: T1) -> T1:
    return a

f1(100)