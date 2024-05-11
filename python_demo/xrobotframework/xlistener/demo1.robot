# 可以指定多个，相互不冲突，都可以被应用
# robot --listener lis1.py --listener lis2.py demo1.robot
# 如果listener需要传递参数，按下面方式传递
# --listener "MGTestGroupAutomation.listener.OAListener2;total_round_id=1;current_round_id=1;fail_notify=false

# https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#listener-interface
# https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#registering-listeners-from-command-line

*** Test Cases ***
case1: test1
    log    test1

case2: test2
    should be equal    1    2