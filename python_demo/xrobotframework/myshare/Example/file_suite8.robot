*** Test Cases ***
Case1
    ${var1}    Set Variable    1
    ${var2}    Evaluate    ${var1} + 1
    Log    ${var2}