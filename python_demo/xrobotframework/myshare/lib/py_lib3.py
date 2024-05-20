class py_lib3:
    # 直接定义一个和文件名同名的类
    # robot里面可以直接通过 Library py_lib3引用到此类
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    # 类相关的方法可以当成keyword直接使用
    def add3(self) -> int:
        return self.a + self.b