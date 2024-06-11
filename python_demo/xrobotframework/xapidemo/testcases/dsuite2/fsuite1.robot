*** Settings ***
Library    ../../py_lib1.py


*** Test Cases ***

测试用例1
    Should Be True    1 == 1
    关键字1    1    1
    add    1    2


*** Keywords ***
关键字1
    [Arguments]    ${arg1}    ${arg2}
    Should Be Equal    ${arg1}    ${arg2}
    FOR    ${i}    IN RANGE    1    4
        Log    ${i}
    END
    关键字2    10    10

关键字2
    [Arguments]    ${arg1}    ${arg2}
    Should Be Equal    ${arg1}    ${arg2}
    ${ret}    add    1    2
    Should Be Equal    ${ret}    3
