```sh
# https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#listener-interface
# https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#registering-listeners-from-command-line

# 通常情况，参数可以使用:分开
robot --listener xxLis:args1:args2 test.robot
# 如果参数是列表形式，此时建议所有参数都把类型带上，比如 arg1 和列表内容都是字符串的情况下
robot --listener xxLis:"args1":"['args2']" test.robot
# 如果某个参数里面包含:，那么可以使用;作为分隔符 args:contain:path 是第一个参数，不是3个参数 args2:contain:path 才是第二个参数
robot --listener xxLis;args1:contain:path;args2:contain:path

robot --listener MyListener tests.robot
robot --listener path/to/MyListener.py tests.robot
robot --listener module.Listener --listener AnotherListener tests.robot
robot --listener listener.py:arg1:arg2 tests.robot
robot --listener "listener.py;arg:with:colons" tests.robot
robot --listener c:\path\listener.py;d:\first\arg;e:\second\arg tests.robot
robot --listener listener.py:name=value tests.robot
robot --listener "listener.py;name=value:with:colons;second=argument" tests.robot

# 8270会自动转换为int，false会自动转换为False，比如下面的python代码
robot --listener Listener:8270:false
```

```python
# 如果listener的参数有类型指定，会自动转换为指定的类型
class Listener:
    def __init__(self, port: int, log=True):
        self.port = post
        self.log = log
```

```python
# Listener implemented as a module using the listener API version 3.

# 可选2和3，从RF7.0开始，默认是3
ROBOT_LISTENER_API_VERSION = 3
ROBOT_LIBRARY_SCOPE = 'GLOBAL'

def start_suite(data, result):
    print(f"Suite '{data.name}' starting.")

def end_test(data, result):
    print(f"Test '{result.name}' ended with status {result.status}.")
```

```python
# Same as the above example, but uses an optional base class and type hints.

from robot import result, running
from robot.api.interfaces import ListenerV3


# 这里继承的基类是可选的，可以是object
class Example(ListenerV3):

    ROBOT_LISTENER_API_VERSION = 3
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def start_suite(self, data: running.TestSuite, result: result.TestSuite):
        print(f"Suite '{data.name}' starting.")

    def end_test(self, data: running.TestCase, result: result.TestCase):
        print(f"Test '{result.name}' ended with status {result.status}.")
```

```python
# 假设我们自己有一个Listener监听库
from listener import Listener

# 假设下面是我们自己写的RF的库(不是监听库)
class LibraryWithExternalListener:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    # 可以在这里进行注册监听库
    ROBOT_LIBRARY_LISTENER = Listener()
    # 可以设置多个listener
    ROBOT_LIBRARY_LISTENER = [Listener1(), Listener2(), Listener3()]

    def example_keyword(self):
         ...
```

```python
class LibraryItselfAsListener:
    ROBOT_LIBRARY_SCOPE = 'SUITE'
    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self):
        # 如果库自己本身就需要监听，也可以自己注册自己
        self.ROBOT_LIBRARY_LISTENER = self

    # Use the '_' prefix to avoid listener method becoming a keyword.
    # 为了避免end_suite被识别为keyword，增加了_前缀
    def _end_suite(self, name, attrs):
        print(f"Suite '{name}' ending with status {attrs['id']}.")

    def example_keyword(self):
         ...
```