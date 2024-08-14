*** Settings ***
Test Template    KW1


*** Test Cases ***

case1: setting test template1
    1    1
    1    2   # 执行失败
    2    2   # 仍然会执行，但是整个case1是失败的
    KW2    1    2   # 无法调用其它keyword，就算这样写了，其实类似于 KW1 KW2 1 2，故报错

case2: setting test template1
    [Template]    KW2    # 覆盖settings的Test Template配置
    1    1
    1    2   # 执行失败
    2    2   # 仍然会执行，但是整个case2是失败的
    KW1    1    1   # 无法调用其它keyword，就算这样写了，其实类似于 KW2 KW1 1 1，故报错
    

*** Keywords ***

KW1
    [Arguments]    ${a}    ${b}
    Should Be True    ${a} == ${b}


KW2
    [Arguments]    ${a}    ${b}
    Should Not Be True    ${a} == ${b}