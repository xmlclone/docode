*** Settings ***
Documentation    演示把文件当成case，testcase当成步骤的使用
# 如果上一个case的执行结果不是pass，则在case的setup里面直接fail
Test Setup       Run Keyword If    '${PREV TEST STATUS}' != 'PASS'    Fail    Prev step fail.
Suite Setup      Log    suite setup.
Suite Teardown   Log    suite teardown.


*** Test Cases ***
Step1: 步骤1pass
    # 第一个case(step)，需要屏蔽settings的setup，因为有可能其它文件的case失败，导致当前文件无法执行
    [Setup]    No Operation
    Log    step1 pass.

Step2: 步骤2fail
    Fail    step2 fail.

Step3: 不会被执行
    Log    This is step3.