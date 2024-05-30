"""
f-string: 
    https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals
    https://docs.python.org/zh-cn/3/reference/lexical_analysis.html#formatted-string-literals

format-string-syntax:   format函数
    https://docs.python.org/zh-cn/3/library/string.html#format-string-syntax
"""


class UserDefineObject:
    def __init__(self) -> None:
        self.a = 1
        self.b = 2

    def __str__(self):
        return f"{self.a=}, {self.b=}"
    
    def __repr__(self):
        return str(self.a + self.b)
    

obj = UserDefineObject()


# ================================================================format================================================================
print("{}".format("ni hao"))
print("{0} {1}".format("ni", "hao"))
print("{a} {b} {a}".format(a="111", b="222"))


# a代表ascii码
print("{0.b} {0.a} {0!s} {0!r} {0!a}".format(obj))


# 左对齐，中间默认补齐空白
print("{a:<30}xyz".format(a="123456"))
print("{:<30}".format("123456"))
# 后面没内容，不表示不补齐，仍然会补齐30个字符串，只不过后面是空白
x = "{:<30}".format("123456")
print(len(x))
# 左对齐的数据不够实际字符串长度时，以实际字符串的长度为准，即完整输出123456
print("{:<2}".format("123456"))
# 实际长度仍然是6，而不是截断为2
x = "{:<2}".format("123456")
print(len(x))


# 右对齐，左边默认补齐空白
print("{:>30}".format("123456"))
# 同理，以实际长度为准
print("{:>2}".format("123456"))


# 居中对齐
print("s{:^30}e".format("123456"))


# 填充*，前面的填充默认是空白
print("{:*^30}".format("123456"))

# 长度10，小数点保留2位，注意小数点也占10位的名额，即填充*只有6个，即输出 1.20******
print("{:*<10.2f}".format(1.2))
# 如果长度不够，仍然会保证小数点后面的位数后补齐输出 1.20
print("{:*<2.2f}".format(1.2))
print("{:*<5.8f}".format(1.2)) # 1.20000000
print("{:*<5.2f}".format(1.234567)) # 1.23*
print("{:*<5.2f}".format(123456.789)) # 123456.79


# 字符串才支持!s !r !a
print("{name!s:*^30}".format(name="1"))
# float类型支持% f等，%表示显示百分比，注意会把原始数据*100后面加%显示
# .2表示保留2位小数
# +表示整数的时候，前面会显示一个+号
# : 后面就是一些格式化的参数，包括填充、对齐、长度、位数、数据格式等信息
# 基本都是可以省略的，某些格式化标记需要和特定的标记联合使用，并且有的标记对传入的参数类型也有要求
print("{name:*^+30.2%}".format(name=3.14))

# 基本格式顺序总结   变量名!sra:*<>^N.Nf%    变量名[!格式(有rsa)]:[填充(默认空白)][对齐(<>^)][长度(N N.N)][格式(f%)]  ，简单记忆为 "变革田队长"
# 

print("int: {0:d}, hex: {0:x}, oct: {0:o}, bin: {0:b}".format(12))
print("int: {0:#d}, hex: {0:#x}, oct: {0:#o}, bin: {0:#b}".format(12))
print("int: {0:#0d}, hex: {0:#0x}, oct: {0:#0o}, bin: {0:#0b}".format(12))



print('-' * 100)


# f 字符串的格式化方式基本与 format 函数一致
name = "lin"
age = 18
print(f"{name} {age}")
print(f"{name=} {age=}")
# obj= 和 obj!r 一致
# obj 和 obj!s 一致
# obj!r= 无法在使用
print(f"{obj=} - {obj} - {obj!r} - {obj!s}")

print(f"{name:<10}")
print(f"{name:>10}")

print(f"{name:*<10}")
print(f"{name:*>10}")
print(f"{name:*^10}")

print(f"{age:<10.2f}")
print(f"{age:<10.2%}")


