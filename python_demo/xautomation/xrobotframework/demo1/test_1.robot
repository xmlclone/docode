*** Settings ***
Documentation    This is document.
...              New line document.
Resource         res.resource
Library          String
# Import Library   
Library          String    AS   NEW_String    
Default Tags     defaulttags
Force Tags       forcetags
Test Setup       My kw1    This is file test setup.
Test Teardown    My kw1    This is file test teardown.
Suite Setup      My kw1    This is file suite setup.
Suite Teardown   My kw1    This is file suite teardown.
Test Timeout


*** Test Cases ***
Test1: test case1
    [Documentation]    This is test case document.
    [Tags]             case1    P0
    [Timeout]
    # 如果在case里面自定义了的和settings里面的冲突，则以case里面生效，settings里面的会被忽略
    [Setup]            My kw1    This is testcase1 setup.
    [Teardown]         My kw1    This is testcase1 teardown.
    My KW1    This is my kw1.

Test2: test case2
    Should Be Equal    1     1
    Res KW1
    # Should Be Lower Case属于String库，通过Library String方式引入后，可以直接使用Should Be Lower Case
    # 但本文由于演示 AS 多次引入了Should Be Lower Case，故这里用.的方式进行了引用区分
    String.Should Be Lower Case     abc
    NEW_String.should_be_lower_case   def


*** Variables ***
${message}    This is variable message.
@{listvar}    1    2    3    4
&{dictvar}    a=1    b=2


*** Keywords ***
My KW1
    [Arguments]    ${message}
    Log    ${message}