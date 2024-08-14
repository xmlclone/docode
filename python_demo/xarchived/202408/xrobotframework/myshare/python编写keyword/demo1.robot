*** Settings ***
# 如果直接引入py文件，其实相当于引入的是相对路径下的py文件，
# 故使用 robot path/to/case 可以直接找到库文件
Library    py_lib1.py
# 这里引入的不是py文件，虽然py_lib2.py和robot文件在相同目录，但robot仍无法找到此库
# 需要在命令行增加参数 -P 指定库文件路径才可以找到，"."表示当前目录
# robot -P . path/to/case
Library    py_lib2
Library    py_lib3    1    2

*** Test Cases ***
Case1
    ${ret}    Add    1    2
    Should Be Equal    ${ret}    ${3}
    ${ret}    Add 2    1    2    3
    Should Be Equal    ${ret}    ${6}
    ${ret}    Add 3
    Should Be Equal    ${ret}    ${3}


