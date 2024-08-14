*** Settings ***
Library    py_lib3    1    2

*** Test Cases ***
Case1
    ${ret}    Add 3
    Should Be Equal    ${ret}    ${3}
