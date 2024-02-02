*** Settings ***
Suite Setup    Log    This is init setup.
Suite Teardown    Log    This is init teardown.

# 如果想本文件被执行，命令行执行时，需要指定为目录，而不是具体的测试文件，比如: robot demo1