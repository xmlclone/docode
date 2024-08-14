*** Settings ***
# 可以直接引用py文件
Variables    variables.py

*** Test Case ***

case1
    should be equal    1     1

case2
    should be equal    1     1
    
case3
    log    ${email_host}