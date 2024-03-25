*** Variables ***
# 变量可以定义在*** Variables ***块下面
${VAR1}    1


*** Test Cases ***
Case1
    # 变量可以在用例或关键字内部
    ${var2}    Set Variable    2
    ${x}    Page Title Should Be    abc
    log    ${x}


*** Keywords ***
Keyword1
    # 关键字的参数也是变量
    [Arguments]    ${var3}
    ${var4}    Set Variable    3

Page Title Should Be
    [Arguments]    ${expected_title}
    Log    ${expected_title}
    RETURN    something