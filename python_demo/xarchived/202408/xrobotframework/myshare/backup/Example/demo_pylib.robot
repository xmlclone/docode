*** Settings ***
# 注意命令行的两种方式
# 如果使用的是Library  pylib1，表示引入的模块，如果模块不在python的搜索路径下，则需要增加-P参数指定pylib2和pylib2所在的路径，比如 robot -P . demo_pylib.robot
# 如果使用的是Library  pylib1.py  其实此时表示给定的就是文件的路径，那么命令行则不要使用-P参数
Library    pylib1
Library    pylib2    ${100}


*** Test Cases ***
Case1: test pylib1 add
    ${ret}    Add    ${1}    ${2}
    Should Be Equal    ${ret}    ${3}

Case2: test pylib2 add
    ${ret}    Pylib2 Add    ${1}    ${2}
    Should Be Equal    ${ret}    ${103}