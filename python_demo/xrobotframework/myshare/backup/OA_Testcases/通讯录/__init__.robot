*** Settings ***
Documentation    通讯录模块
Resource    ../keywords.resource
Suite Setup    Open AddressbookPage
Suite Teardown  Close AddressbookPage


*** Keywords ***
Open AddressbookPage
    [Documentation]
    ...    打开并切换到通讯录页面
    ...
    ...    *参数* 无
    ...
    ...    *返回值* 无
    ...
    ...    *更新历史*
    ...    - 20240221 LINLEI 创建
    Login With Username    ${USERNAME}    ${PASSWORD}
    Click Link    ${E_INDEX_ADDRESSBOOK}
    Switch Window    NEW

Close AddressbookPage
    [Documentation]
    ...    关闭通讯录页面并切换到首页
    ...
    ...    *参数* 无
    ...
    ...    *返回值* 无
    ...
    ...    *更新历史*
    ...    - 20240221 LINLEI 创建
    Close Window
    Switch Window
