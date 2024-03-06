def f1():
    yield from [1, 2, 3]
    yield from [4, 5, 6]
    yield from [7, 8, 9]

for i in f1():
    # 会迭代1 2 3 4 5 6 7 8 9
    print(i)