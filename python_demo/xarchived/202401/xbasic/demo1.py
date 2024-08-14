# *****************************海象运算符 walrus operator  3.8引入
for i in range(100):
    # 把 i + 1赋值给c，并且判断 c == 10
    if (c := i + 1) == 10:
        break
    print(c)
# 等同于下面的代码，其实就简化了一行代码，常用于文件读取并进行判断
for i in range(100):
    c = i + 1
    if c == 10:
        break
    print(c)
print()