from pathlib import Path

# __file__才是获取当前文件，而不管文件被哪里调用
path = Path(__file__)
# . 表示的是执行者的路径，并不一定是当前文件的路径(本模块可能被其它模块调用，.就是其它模块的路径了)
path = Path('.')
# .
print(path)
# 绝对路径
print(path.absolute())
# 绝对路径的父路径，如果直接使用path，也就是.，parent仍然是点，故尽量使用绝对路径
# 并且注意，上面的点表示的是当前执行的路径(注意，如果这个模块被外层引用，执行外层代码时，.表示的是外层的路径，就不是本文件的路径了)
print(path.absolute().parent)
print(path.absolute().parent / 'logs')