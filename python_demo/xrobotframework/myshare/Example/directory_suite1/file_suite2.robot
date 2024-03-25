*** Settings ***
# 此处配置的Test Setup会在本用例集内所有case生效
# 当某个case定义单独的[Setup]，则case的[Setup]会生效，此处配置不会执行
Test Setup    No Operation


*** Test Cases ***
Case1
    Log    This is case1

Case2
    [Setup]    No Operation
    Log    This is case2