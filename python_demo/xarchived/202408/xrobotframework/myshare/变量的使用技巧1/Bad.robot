*** Settings ***
# 引入Selenium库
Library    SeleniumLibrary


*** Test Cases ***
Case1-验证百度搜索python关键字功能正常
    [Teardown]    Close Browser
    [Timeout]    10s
    # step1 打开浏览器，预期首页出现搜索框
    Open Browser    https://www.baidu.com    browser=gc
    Wait Until Element Is Visible    id:kw    3s
    # step2 搜索框输入python，预期搜索成功
    Input Text    id:kw    python
    Click Element    id:su
    Wait Until Page Contains    python.org

Case2-验证百度搜索robotframework关键字功能正常
    [Teardown]    Close Browser
    [Timeout]    10s
    # step1 打开浏览器，预期首页出现搜索框
    Open Browser    https://www.baidu.com    browser=gc
    Wait Until Element Is Visible    id:kw    3s
    # step2 搜索框输入robotframework，预期搜索成功
    Input Text    id:kw    robotframework
    Click Element    id:su
    Wait Until Page Contains    robotframework.org