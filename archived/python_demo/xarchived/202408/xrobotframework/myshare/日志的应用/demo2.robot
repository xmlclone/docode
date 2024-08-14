*** Test Cases ***
Case1
    KW1    1    2

Case2
    KW1    1    2

Case3
    KW1    1    2

Case4
    Should Be Equal    1    2

Case5
    FOR KW1
    Tag KW1


*** Keywords ***
KW1
    [Arguments]    ${arg1}    ${arg2}
    No Operation
    RETURN    KW1

FOR KW1
    FOR    ${i}    IN    1    2    3    4
        Log    ${i}
    END

Tag KW1
    [Tags]    kw
    Log    tag kw.