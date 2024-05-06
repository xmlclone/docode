


*** Settings ***
# 引入Selenium库
Library    SeleniumLibrary


*** Variables ***
${URL}    https://www.baidu.com
${BROWSER}    gc
${ELEMENT_INPUT_SEARCH}    id:kw
${ELEMENT_BUTTON_SEARCH}    id:su


*** Test Cases ***
Case1-验证百度搜索python关键字功能正常
    [Teardown]    Close Browser
    [Timeout]    10s
    # step1 打开浏览器，预期首页出现搜索框
    Open Browser   ${URL}     browser=${BROWSER}
    Wait Until Element Is Visible    ${ELEMENT_INPUT_SEARCH}    3s
    # step2 搜索框输入python，预期搜索成功
    Input Text    ${ELEMENT_INPUT_SEARCH}    python
    Click Element    ${ELEMENT_BUTTON_SEARCH} 
    Wait Until Page Contains    python.org

Case2-验证百度搜索robotframework关键字功能正常
    [Teardown]    Close Browser
    [Timeout]    10s
    # step1 打开浏览器，预期首页出现搜索框
    Open Browser    ${URL}    browser=${BROWSER}
    Wait Until Element Is Visible    ${ELEMENT_INPUT_SEARCH}    3s
    # step2 搜索框输入robotframework，预期搜索成功
    Input Text    ${ELEMENT_INPUT_SEARCH}    robotframework
    Click Element    ${ELEMENT_BUTTON_SEARCH} 
    Wait Until Page Contains    robotframework.org