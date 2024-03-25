*** Settings ***
Library    SeleniumLibrary
Suite Setup    Open Browser    browser=${BROWSER}
Suite Teardown    Close Browser
Test Setup    Go To    url=${URL}
Test Timeout    20s


*** Variables ***
# 公共的全局变量，正常情况应该定义到一个资源文件.resource内
${URL}    https://www.baidu.com
${BROWSER}    gc
# 元素定义器，同理，应该定义到资源文件.resource内
${LOCATOR_INPUT_SEARCH}    id:kw
${LOCATOR_BUTTON_BAIDUYIXIA}    id:su


*** Test Cases ***
Case1-百度首页搜索robotframework
    Input Text    ${LOCATOR_INPUT_SEARCH}    robotframework
    Click Button    ${LOCATOR_BUTTON_BAIDUYIXIA}
    Wait Until Page Contains    robotframework.org

Case2-百度首页搜索python
    Input Text    ${LOCATOR_INPUT_SEARCH}    python
    Click Button    ${LOCATOR_BUTTON_BAIDUYIXIA}
    Wait Until Page Contains    python.org
    
