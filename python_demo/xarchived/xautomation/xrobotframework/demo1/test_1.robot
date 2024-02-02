*** Settings ***
Documentation    This is document. 演示基础语法
...              New line document.
...              示例代码里面有部分大小写混写是故意用于演示的，RF不区分大小写
Resource         res.resource
# Import Library 是一个keyword，不是setting
Library          String
# 如果通过物理路径方式引入库，必须指定文件后缀(.py)和路径分隔符
# 但是如果库已经在python查找路径下，则可以不用，比如 robot -L TRACE -P . test_1.robot   此时lib2和lib2都可以不用后缀的方式引入了
Library          lib1.py
Library          lib2    xmlclone    18
Library          String    AS   NEW_String    
Default Tags     defaulttags
Force Tags       forcetags
Test Setup       My kw1    This is file test setup.
Test Teardown    My kw1    This is file test teardown.
Suite Setup      My kw1    This is file suite setup.
Suite Teardown   My kw1    This is file suite teardown.

# timeout支持的格式: 如果纯数字则表示秒，更多请参考： http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#time-format
# Test Timeout     1 minute 42 seconds


*** Test Cases ***
Test1: test case1
    [Documentation]    This is test case document.
    [Tags]             case1    P0
    [Timeout]
    # 如果在case里面自定义了的和settings里面的冲突，则以case里面生效，settings里面的会被忽略
    [Setup]            My kw1    This is testcase1 setup.
    [Teardown]         My kw1    This is testcase1 teardown.
    ${ret}    My KW1    This is my kw1.
    Log    ${ret}

Test2: test case2
    Should Be Equal    1     1
    Res KW1
    # Should Be Lower Case属于String库，通过Library String方式引入后，可以直接使用Should Be Lower Case
    # 但本文由于演示 AS 多次引入了Should Be Lower Case，故这里用.的方式进行了引用区分
    String.Should Be Lower Case     abc
    NEW_String.should_be_lower_case   def

Test3: test case3
    # 大部分情况下，如果一行过长，均可以通过...的方式进行连接
    FOR    ${i}    IN     cat    dog
    ...    pig
        Log    test for in: ${i}
    END

    FOR    ${v}    IN    @{listvar}
        Log    test for in listvar: ${v}
    END

    # IN RANGE 类似python内 range，可以接受3个参数
    FOR    ${i}    IN RANGE    5
        Log    test for range: ${i}
    END

    # 也支持start参数
    # 也有 for in zip
    # for in 同样也支持字典，比如下面的&{dictvar}
    FOR    ${idx}    ${val}    IN ENUMERATE    @{listvar}
        LOG    test for enumerate: ${idx}, ${val}
    END

    ${var1} =    Set Variable    5
    WHILE    ${var1} > 0
        LOG    this is while: ${var1}
        ${var1} =    Evaluate    ${var1} - 1
        # 下面的代码会把var赋值为 4 - 1 字符串，再次循环到Evaluate时，会被替换为 4 - 1 - 1
        ${var1} =    Set Variable    ${var1} - 1
    END

    IF    ${var1} > 0
        Log    var1>0
    ELSE IF    ${var1} < 0
        log    var1<0
    ELSE
        log    var1=0
    END

Test4: user lib
    # 演示了两种调用方式，第一个得到的是字符串12(期望是3)，第二个才获得了2+3的结果(也就是5)
    ${v}    lib1.lib1_func1     1    2
    Log    ${v}
    ${v}    LIB1_FUNC1     ${2}    ${3}
    lOG    ${V}

    ${name}    Get Name
    Log    ${name}

Test5: user lib socpe test
    ${name}    Get Name
    Log    ${name}


*** Variables ***
${message}    This is variable message.
@{listvar}    1    2    3    4
&{dictvar}    a=1    b=2


*** Keywords ***
My KW1
    [Arguments]    ${message}
    Log    ${message}
    [Return]   my kw1 return.