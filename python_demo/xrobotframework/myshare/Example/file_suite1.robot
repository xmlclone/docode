*** Settings ***
Suite Setup    No Operation


*** Variables ***
${GVAR1}    This is global var1.


*** Test Cases ***
Case1
    Log    This is case1

Case2
    Log    This is case2


*** Keywords ***
Keyword1
    No Operation