*** Settings ***
Test Tags    suite7
Test Timeout    10


*** Test Cases ***
Case1
    [Timeout]    5s
    [Teardown]    Log    This is case1 teardown
    Sleep    6
    Log    This is case1

Case2
    Sleep    6
    Log    This is case2
    