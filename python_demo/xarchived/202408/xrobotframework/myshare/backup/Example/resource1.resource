*** Keywords ***
If Keyword1
    [Arguments]    ${var1}
    IF    ${var1} == 1
        Log    var1 is 1.
    ELSE
        Log    var1 not 1.
    END

If Keyword2
    [Arguments]    ${var1}
    IF    ${var1} == 1
        Log    var1 is 1.
    ELSE IF    ${var1} == 2
        Log    var1 is 2.
    ELSE
        Log    var1 not 1.
    END

Inline If
    [Arguments]    ${var1}
    IF    ${var1} == 1    Log    var1 is 1.    ELSE    Log    var1 not 1.

For Keyword1
    FOR    ${i}    IN    cat    dog
        Log    ${i}
    END

For Keyword2
    @{list_var}    Create List    cat    dog
    FOR    ${i}    IN    @{list_var}
        Log    ${i}
    END
    # 猜猜下面逻辑是如何执行的
    FOR    ${i}    IN    ${list_var}
        Log    ${i}
    END

For In Range Keyword1
    FOR    ${i}    IN RANGE    1    10    2
        Log    ${i}
    END

For In Range Keyword2
    @{list_var}    Create List    cat    dog
    FOR    ${idx}    ${val}    IN ENUMERATE    @{list_var}
        Log    list_var[${idx}]=${val}
    END