*** Settings ***
Library    demo2_lib    # robotcode: ignore


*** Test Cases ***
case1
    UserKeyword Post Request


*** Keywords ***
UserKeyword Post Request
    Post Request    # robotcode: ignore
    Should Be Equal    1    2