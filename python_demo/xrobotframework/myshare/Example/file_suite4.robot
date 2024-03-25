*** Settings ***
Resource    resource1.resource


*** Test Cases ***
Case1
    If Keyword1    ${1}
    If Keyword2    ${3}
    Inline If    ${1}

Case2
    [Tags]    for
    For Keyword1
    For Keyword2
    For In Range Keyword1
    For In Range Keyword2