*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BROWSER}    chrome
${URL}        https://www.baidu.com

*** Test Cases ***
Search Baidu
    Open Browser    ${URL}    ${BROWSER}
    Input Text    id=kw    Robot Framework
    Click Button    id=su
    [Teardown]    Close Browser


Search Baidu2
    Open Browser    ${URL}    ${BROWSER}
    Input Text    id=kw    Robot Framework
    Click Button    id=su
    [Teardown]    Close Browser