*** Settings ***
Documentation    通讯录搜索功能
Resource    ../keywords.resource
Resource    testdata.resource
Test Tags    ui    webui
Test Timeout    30s
Test Teardown    Reset Search


*** Test Cases ***
搜索功能验证点01
    [Documentation]
    ...    *脚本描述* 搜索功能支持以中文姓名全名、邮箱前缀、花名进行搜索
    ...
    ...    *脚本作者* LINLEI
    ...
    ...    *功能用例* 无
    ...
    ...    *测试步骤*
    ...    - 使用中文全名进行搜索，预期搜索正确
    ...    - 使用邮箱前缀进行搜索，预期搜索正确
    ...    - 使用花名全名进行搜索，预期搜索正确
    ...
    ...    *更新历史*
    ...    - 20240221 LINLEI 创建
    [Tags]    p0    smoke
    # step1
    Search    ${CN_NAME}
    Page Should Contain Link    ${CN_ALIAS_NAME}
    Reset Search
    # step2
    Search    ${MAIL_PREFIX}
    Page Should Contain Link    ${CN_ALIAS_NAME}
    Reset Search
    # step3
    Search    ${ALIAS_NAME}
    Page Should Contain Link    ${CN_ALIAS_NAME}


*** Keywords ***
Search
    [Arguments]    ${content}
    [Documentation]
    ...    搜索内容
    ...
    ...    *参数*
    ...
    ...    ${content} 待搜索的内容
    ...
    ...    *返回值* 无
    ...
    ...    *Example*
    ...
    ...    | `Search` | username |
    ...
    ...    *更新历史*
    ...    - 20240221 LINLEI 创建
    Input Text    ${E_ADDRESSBOOK_SEARCH_INPUT}    ${content}
    Click Button    ${E_ADDRESSBOOK_SEARCH_BUTTON}

Reset Search
    [Documentation]
    ...    重置搜索
    ...
    ...    *参数* 无
    ...
    ...    *返回值* 无
    ...
    ...    *更新历史*
    ...    - 20240221 LINLEI 创建
    Clear Element Text    ${E_ADDRESSBOOK_SEARCH_INPUT}
    Click Button    ${E_ADDRESSBOOK_SEARCH_BUTTON}
