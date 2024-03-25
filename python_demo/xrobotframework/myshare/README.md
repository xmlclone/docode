# 环境配置

示例代码在以下环境下执行通过：

```sh
> conda --version
conda 4.10.3

> python --version
Python 3.12.2

> pip --version
pip 24.0

> pip freeze
robotframework==7.0

> robot --version
Robot Framework 7.0

> systeminfo | findstr /B /C:"OS 名称" /C:"OS 版本"
OS 名称:          Microsoft Windows 10 专业版
OS 版本:          10.0.19045 暂缺 Build 19045
```


# level0-1

1. 基础快速回顾
   1. 用例、用例集(文件级别和目录级别)
   2. 变量(标量、字典、列表)
   3. 关键字
2. 执行用例
   1. ride
   2. robot(目录、文件、tag等)
3. 控制结构(FOR、WHILE、IF、TRY等)
   1. FOR IN ENUMERATE
   2. FOR IN RANGE
   3. FOR IN ZIP
4. 资源文件的定义与使用
5. 三方库的引入与使用
6. Setup、Teardwon、Tags、Timeout
7. 常用内置变量part1(None Empty True False ${0}等)


https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#built-in-variables


# level0-2

1. 常用的内置变量part2(${TEST NAME}  ${TEST STATUS}  ${PREV TEST STATUS}等)
2. 用python编写一个keyword
3. 调用python的库(以random举例)
4. 变量使用中可能存在的坑(字典、列表、空值、数字等)
5. 执行时改变变量的值(--variable --variablefile)
6. 日志的一些技巧
   1. 日志级别
   2. 日志分离
   3. 轻量化日志
   4. 日志修复
7. 监听器
8. 远程库


# level1

1. 变量的优先级和作用域
2. 基于python对象的变量
3. 常用库和关键字
4. 第三方库参考
5. robot常用命令行参数
6. 虚拟环境参考
7. 全中文支持(比如`***Test Cases***`可以写为`***测试用例***`)