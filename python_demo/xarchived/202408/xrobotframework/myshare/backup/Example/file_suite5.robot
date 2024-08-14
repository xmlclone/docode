*** Settings ***
Suite Setup    Log    This is file suite5 suite setup
Suite Teardown    Log    This is file suite5 suite teardown
Test Setup    Log    This is file suite5 test setup
Test Teardown    Log    This is file suite5 test teardown


*** Test Cases ***
case1
    Log    This is case1

case2
    [Setup]    Log    This is case2 setup
    Log    This is case2

case3
    [Teardown]    Log    This is case3 teardown
    Log    This is case3

case4
    [Setup]    Log    This is case4 setup
    [Teardown]    Log    This is case4 teardown
    Log    This is case4