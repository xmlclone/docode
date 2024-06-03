from typing import cast, Optional


def f1(a: int, b: Optional[int] = None) -> int:
    b = cast(int, b)
    # 虽然这里的代码举例不是非常正确，但是可以很好的演示 cast 的使用
    # 默认情况，如果不使用上面的 cast 代码，则静态检查工具会对下面的代码提示 Operator "+" not supported for types "int" and "int | None"
    # 即静态检查不过，如果增加上面代码，则可以通过静态检查
    c = a + b
    return c