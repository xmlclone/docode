*** Test Cases ***
case1
    ${var}    Evaluate    random.randint(0, 4)
    log to console    ${var}