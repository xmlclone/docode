



*** Settings ***
# 引入Selenium库
Library    SeleniumLibrary
# 引入资源库，
# 这里把环境和定位相关的分为了两个资源文件，便于区分不同类型的变量
Resource    env.resource
Resource    locator.resource
# 顺便把一些通用的、不符合规范的代码也进行了整合
# # 所有用例的超时时间配置
Test Timeout    10s
# # 所有用例都需要打开浏览器，
## 那么在整个用例集期间只打开和关闭一次浏览器，提升执行效率
Suite Setup    Open Browser    browser=${BROWSER}
Suite Teardown    Close Browser


*** Test Cases ***
Case1-验证百度搜索python关键字功能正常
    # step1 打开浏览器，预期首页出现搜索框
    Go To   ${URL}
    Wait Until Element Is Visible    ${ELEMENT_INPUT_SEARCH}    3s
    # step2 搜索框输入python，预期搜索成功
    Input Text    ${ELEMENT_INPUT_SEARCH}    python
    Click Element    ${ELEMENT_BUTTON_SEARCH} 
    Wait Until Page Contains    python.org

Case2-验证百度搜索robotframework关键字功能正常
    # step1 打开浏览器，预期首页出现搜索框
    Go To    ${URL}
    Wait Until Element Is Visible    ${ELEMENT_INPUT_SEARCH}    3s
    # step2 搜索框输入robotframework，预期搜索成功
    Input Text    ${ELEMENT_INPUT_SEARCH}    robotframework
    Click Element    ${ELEMENT_BUTTON_SEARCH} 
    Wait Until Page Contains    robotframework.org