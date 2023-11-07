RobotFramework
=================

.. contents:: 目录


命令行
----------

.. code-block:: console

    # 根据文件执行
    robot test_1.robot

    # 注意下面的选项均需要在测试路径之前指定，比如
    robot -i xxx paths
    # 根据tag执行，支持 * ? []，AND OR NOT
    robot -i/--include 

    # 排除tag
    robot -e/--exclude

    # 指定日志级别
    robot -L/--loglevel TRACE/DEBUG/INFO/WARN/NONE

    # 指定python库查找路径，多个路径通过:分割
    robot -P/--pythonpath


参考链接
--------------

* `github <https://github.com/robotframework/robotframework>`_
* `内建变量 <http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#built-in-variables>`_
* `控制结构 <http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#control-structures>`_
* `可用配置(每个块支持的配置项) <http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#available-settings>`_
* `Timeout格式 <http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#time-format>`_
* `命令行选项 <http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#command-line-options>`_
* `测试库编写 <http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#creating-test-libraries>`_
    