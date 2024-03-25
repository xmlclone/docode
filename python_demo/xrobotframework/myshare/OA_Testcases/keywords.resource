*** Settings ***
Documentation    OA项目封装的通用Keyword
Resource    config.resource
Resource    locator.resource
Resource    testdata.resource
Library    SeleniumLibrary    timeout=${TIMEOUT}    implicit_wait=${IMPLICIT_TIMEOUT}    screenshot_root_directory=imgs


*** Keywords ***
Open Browser To Login Page
    [Documentation]
    ...    打开浏览器并访问登录页面
    ...
    ...    *参数* 无
    ...
    ...    *返回值* 无
    ...
    ...    *更新历史*
    ...    - 20240221 LINLEI 创建
    IF    "${SLOW}"    Set Selenium Speed    ${SLOW}
    Open Browser    ${URL}    browser=gc
    Title Should Be    登录

Logout Account
    [Documentation]
    ...    退出账户
    ...
    ...    *参数* 无
    ...
    ...    *返回值* 无
    ...
    ...    *更新历史*
    ...    - 20240221 LINLEI 创建
    Click Link    ${E_COMMON_LOGOUT}

Login With Username
    [Arguments]    ${username}    ${password}
    [Documentation]
    ...    用户名密码登录
    ...
    ...    *参数*
    ...
    ...    ${username} 登录用户名
    ...
    ...    ${password} 登录密码
    ...
    ...    *返回值* 无
    ...
    ...    *Example*
    ...
    ...    | `Login With Username` | username | password |
    ...
    ...    *更新历史*
    ...    - 20240221 LINLEI 创建
    Select Frame    ${E_LOGIN_IFRAME}
    Input Text    ${E_LOGIN_USERNAME}    ${username}
    Input Password    ${E_LOGIN_PASSWORD}    ${password}
    Click Button    ${E_LOGIN_LOGIN}

Login With SMS
    [Documentation]
    ...    短信验证码登录
    ...
    ...    *参数* 无
    ...
    ...    *返回值* 无
    ...
    ...    *更新历史*
    ...    - 20240221 LINLEI 创建
    No Operation
