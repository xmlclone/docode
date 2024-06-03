from typing import (
    List,
    Dict,
    Tuple,
    Union,
    Optional,
    Callable,
    NewType,
    TypeVar,   # 示例代码请参考 generic_demo0.py
    Annotated, # 参考 annotated_demo0.py
    Literal,
    Sequence as typeSequence
)

from collections.abc import (
    Mapping,
    Sequence as abcSequence
)


UserId = NewType('UserId', int)


def stub_function1(x: int, y: int) -> int:
    ...


class User:
    ...


def test_function1(
    user_ids: List[UserId],
    user_cls: type[User], 
    user: User,   # 注意 User 和 type[User] , User 表示是 User 的实例对象， 而 type[User] 表示的是传递 User 类或者 User 的子类
    call_fun1: Callable[[int, int], int],
    call_fun2: Callable[[int, int, Exception], int],
    tuple_var: Tuple[int, int],
    dict_vars: Dict[str, int],
    union_var: Union[str, int],
    union_var2: Union[int, None],
    literal_var: Literal['r', 'w', 'rb', 'wb'], # 类似于 choices
    optional_var: Optional[int] = 0,  # 其实等价于上面的 Union[int, None], 当然不包括后面的默认值
) -> None:
    ...



