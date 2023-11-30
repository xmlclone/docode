*** Settings ***
Library    SeleniumLibrary

*** Test Case ***
test1: test open chrome
    Open Browser    https://www.baidu.com    gc    options=add_argument("--headless")
    Log To Console   opened
    Capture Page Screenshot    EMBED
    Sleep    10s
