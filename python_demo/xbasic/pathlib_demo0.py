import pathlib


path_a = pathlib.Path()
print(f"{path_a=}, {path_a.resolve()=}, {path_a.absolute()=}")

# path_a 和 path_b 是同一个目录，即当前目录
# path_a=WindowsPath('.')
# path_a.resolve()=WindowsPath('D:/github/docode/python_demo/xbasic'),
# path_a.absolute()=WindowsPath('D:/github/docode/python_demo/xbasic')
path_b = pathlib.Path(".")
# print(f"{path_b=}, {path_b.resolve()=}, {path_b.absolute()=}")

# 下面对比，看出resolve和absolute的区别
# path_c=WindowsPath('../xsqlalchemy')
# path_c.resolve()=WindowsPath('D:/github/docode/python_demo/xsqlalchemy')
# path_c.absolute()=WindowsPath('D:/github/docode/python_demo/xbasic/../xsqlalchemy')
path_c = pathlib.Path("../xsqlalchemy")
print(f"{path_c=}, {path_c.resolve()=}, {path_c.absolute()=}")


# 获取当前目录，下面两个方式都可用获取
print(f"{pathlib.Path.cwd()=}, {pathlib.Path(__file__).parent=}")