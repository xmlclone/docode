from typing import Annotated
from pydantic import StringConstraints


str_11 = Annotated[str, StringConstraints(max_length=11)]
str_30 = Annotated[str, StringConstraints(max_length=30)]
str_60 = Annotated[str, StringConstraints(max_length=60)]
str_120 = Annotated[str, StringConstraints(max_length=120)]
