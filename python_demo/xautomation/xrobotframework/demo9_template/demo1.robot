*** Test Cases ***

case1: normal Keyword driven
    KW1    1    1
    KW1    1    2   # 执行失败
    KW1    2    2   # 不会被执行


case2: templates ref
    [Template]    KW1
    1    1
    1    2   # 执行失败
    2    2   # 仍然会执行，但是整个case2是失败的

case3: embedded arguments
    [Documentation]    参数嵌入到keyword名称里面，使用方式类型
    [Template]         The ${a} should equal to ${b}
    1    1
    1    2
    2    2

*** Keywords ***

KW1
    [Arguments]    ${a}    ${b}
    Should Be True    ${a} == ${b}


The ${a} should equal to ${b}
    Should Be True    ${a} == ${b}