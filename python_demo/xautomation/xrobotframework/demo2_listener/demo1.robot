# 可以指定多个，相互不冲突，都可以被应用
# robot --listener lis1.py --listener lis2.py demo1.robot
# https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#listener-interface

*** Test Cases ***
case1: test1
    log    test1

case2: test2
    should be equal    1 == 2