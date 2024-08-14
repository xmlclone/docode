*** Settings ***
Documentation    用户名密码登录功能
Resource    ../keywords.resource
Resource    testdata.resource
Test Timeout    30s


*** Test Cases ***
登录成功验证
    [Documentation]
    ...    *脚本描述* 验证用户输入正确的用户名和密码功能，预期登录成功
    ...
    ...    *脚本作者* LINLEI
    ...
    ...    *功能用例* 如果有，则关联功能用例ID，否则置为无
    ...
    ...    *测试步骤*
    ...    - 使用正确的用户名和密码登录，预期登录成功(页面能查找到退出元素表示登录成功)
    ...
    ...    *更新历史*
    ...    - 20240221 LINLEI 创建
    [Tags]    p0    smoke
    [Teardown]    Logout Account
    # step1
    Login With Username    ${USERNAME}    ${PASSWORD}
    Wait Until Page Contains Element    ${E_COMMON_LOGOUT}

错误密码验证
    [Documentation]
    ...    *脚本描述* 验证用户输入错误密码功能，预期登录失败
    ...
    ...    *脚本作者* LINLEI
    ...
    ...    *功能用例* 无
    ...
    ...    *测试步骤*
    ...    - 使用错误的密码登录，预期登录失败(登录按钮value值变更为"用户名或密码错误")
    ...
    ...    *更新历史*
    ...    - 20240221 LINLEI 创建
    [Tags]    p1    smoke
    [Teardown]    Unselect Frame
    # step1
    Login With Username    ${USERNAME}    ${ERROR_PASSWORD}
    Wait Until Keyword Succeeds
    ...    6x
    ...    0.5s
    ...    Element Attribute Value Should Be    ${E_LOGIN_LOGIN}    value    用户名或密码错误

用户名密码空值验证
    [Documentation]
    ...    *脚本描述* 验证用户未输入用户名、密码登录功能，预期登录失败
    ...
    ...    *脚本作者* LINLEI
    ...
    ...    *功能用例* 无
    ...
    ...    *测试步骤*
    ...    - 使用空用户名登录，预期登录失败(登录按钮value值变更为"请输入用户名")
    ...    - 使用空密码登录，预期登录失败(登录按钮value值变更为"请输入密码")
    ...    - 使用空用户名和密码登录，预期登录失败(登录按钮value值变更为"请输入用户名")
    ...
    ...    *更新历史*
    ...    - 20240221 LINLEI 创建
    [Tags]    p2
    [Teardown]    Unselect Frame
    # step1
    Login With Username    ${EMPTY}    sdfaq342dsfs
    Wait Until Keyword Succeeds
    ...    6x
    ...    0.5s
    ...    Element Attribute Value Should Be    ${E_LOGIN_LOGIN}    value    请输入用户名
    Unselect Frame
    # step2
    Login With Username    ${USERNAME}    ${EMPTY}
    Wait Until Keyword Succeeds
    ...    6x
    ...    0.5s
    ...    Element Attribute Value Should Be    ${E_LOGIN_LOGIN}    value    请输入密码
    Unselect Frame
    # step3
    Login With Username    ${EMPTY}    ${EMPTY}
    Wait Until Keyword Succeeds
    ...    6x
    ...    0.5s
    ...    Element Attribute Value Should Be    ${E_LOGIN_LOGIN}    value    请输入用户名
