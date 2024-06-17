from contextlib import contextmanager, closing


# demo1
@contextmanager
def user_open1(file, mode='r'):
    fp = open(file, mode)
    try:
        yield fp
    except Exception as e:
        print(e)
    finally:
        fp.close()

with user_open1('test.txt') as fp:
    print(fp)
    # raise Exception('user exception')


# demo2 closing
class C1:
    def __init__(self) -> None:
        print('c1::__init__')

    def print(self):
        print("c1::print")

    def close(self):
        print('c1::close')

# 某个对象具有 close 的时候可以这样使用，而不用 contextmanager
with closing(C1()) as c1:
    c1.print()
    raise Exception('user exception')