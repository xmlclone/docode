class A1:
    def __enter__(self):
        print('A1::__enter__')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print('A1::__exit__')


class A2:
    def __enter__(self):
        print('A2::__enter__')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # 默认 exit 返回 None，即假值，异常会被再次抛出
        # 如果想屏蔽或掩饰异常，请返回一个真值(此时你应该在这里明确的处理异常)
        print('A2::__exit__')
        return True
    
with A2() as _:
    a = 1 / 0

with A1() as _:
    a = 2 / 0

# 下面代码无法得到执行
print('no run')

