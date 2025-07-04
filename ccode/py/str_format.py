# https://docs.python.org/3/library/string.html#formatstrings
# https://docs.python.org/zh-cn/3/library/string.html#format-specification-mini-language
# f-format: https://docs.python.org/zh-cn/3/reference/lexical_analysis.html#f-strings  3.6增加
# 与 % 比较: https://docs.python.org/zh-cn/3/library/string.html#format-examples
# % 格式: https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting


# 其中 s表示str(), r表示repr(), a表示ascii()
# 基本格式顺序总结： [变量名][!sra]:*[<>^][N N.N]f%    [变量名][!格式(有rsa)]:[填充(默认空白)][对齐(<>^)][长度(N N.N)][格式(f%)]
# 简单记忆为 "变革:田队长"


"{!s:*^10}".format("a")


# *****左对齐*****，中间默认补齐空白
# 123456                        xyz
a = "123456"
print("{a:<30}xyz".format(a="123456"))
print(f"{a:<30}xyz")
print("%-30sxyz" % a)
# 123456                           一直到这里，补齐了24个空格
print("{:<30}".format("123456"))


# 后面没内容，不表示不补齐，仍然会补齐30个字符串，只不过后面是空白
x = "{:<30}".format("123456")
print(len(x))   # 30
# 左对齐的数据不够实际字符串长度时，以实际字符串的长度为准，即完整输出123456
print("{:<2}".format("123456"))
# 实际长度仍然是6，而不是截断为2
x = "{:<2}".format("123456")
print(len(x))    # 6


# *****右对齐*****，左边默认补齐空白
#                         123456
print("{:>30}".format("123456"))
print(f"{a:>30}")
print("%30s" % a)
print("%+30s" % a)
# 同理，以实际长度为准，即完整输出123456
print("{:>2}".format("123456"))


# *****居中对齐*****
# s            123456            e
print("s{:^30}e".format("123456"))
print(f"s{a:^30}e")
# % 无法直接居中对齐


# *****填充*，前面的填充默认是空白，这里用*填充
# ************123456************
print("{:*^30}".format("123456"))
print(f"{a:*^30}")
# % 无法直接自定义填充字符串，但是可以填充整形
# 000000000000000000000000123456
print("%030d" % 123456)


# 长度10，小数点保留2位，注意小数点也占10位的名额，即填充*只有6个，即输出 1.20******
a = 1.2
print("{:*<10.2f}".format(1.2))
print(f"{a:*<10.2f}")
#       1.20
print("%10.2f" % 1.2)
# 如果长度不够，仍然会保证小数点后面的位数后补齐输出 1.20，即优先保证 .x 这里的 x 的个数
print("{:*<2.2f}".format(1.2))
print("{:*<5.8f}".format(1.2)) # 1.20000000
print("{:*<5.2f}".format(1.234567)) # 1.23*
print("{:*<5.2f}".format(123456.789)) # 123456.79



# int: 12, hex: c, oct: 14, bin: 1100
# int: 12, hex: 0xc, oct: 0o14, bin: 0b1100
# int: 12, hex: 0xc, oct: 0o14, bin: 0b1100
print("int: {0:d}, hex: {0:x}, oct: {0:o}, bin: {0:b}".format(12))
a = 12
print(f"int: {a:d}")
print("int: {0:#d}, hex: {0:#x}, oct: {0:#o}, bin: {0:#b}".format(12))
print("int: {0:#0d}, hex: {0:#0x}, oct: {0:#0o}, bin: {0:#0b}".format(12))
