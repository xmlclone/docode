*** Settings ***
Documentation    演示把文件当成case，testcase当成步骤的使用
Test Setup    Run Keyword If 


*** Test Cases ***
Step1: 步骤1pass
    No Operation

Step2: 步骤2fail
    Fail

Step3: 不会被执行
    Log    This is step3.