*** Settings ***
Documentation    忘记密码功能
Resource    ../keywords.resource
Test Timeout    30s


*** Test Cases ***
忘记密码链接验证
    [Documentation]
    ...    *脚本描述* 验证忘记密码链接可正常跳转
    ...
    ...    *脚本作者* LINLEI
    ...
    ...    *功能用例* 如果有，则关联功能用例ID，否则置为无
    ...
    ...    *测试步骤*
    ...    - 点击忘记密码，预期在新tab页打开重置密码页面(窗口数量为2)，并且新窗口页面标题为"验证码"
    ...
    ...    *更新历史*
    ...    - 20240221 LINLEI 创建
    [Tags]    p0    smoke
    [Teardown]    Close Forget Page
    # step1
    Select Frame    ${E_LOGIN_IFRAME}
    Click Link    ${E_LOGIN_FORGETPASSWORD}
    @{handles}    Get Window Handles
    Length Should Be    ${handles}    2
    Switch Window    验证码
    Title Should Be    验证码


*** Keywords ***
Close Forget Page
    [Documentation]
    ...    关闭忘记密码页
    ...
    ...    *参数* 无
    ...
    ...    *返回值* 无
    ...
    ...    *更新历史*
    ...    - 20240221 LINLEI 创建
    Switch Window    验证码
    Close Window
    Switch Window
