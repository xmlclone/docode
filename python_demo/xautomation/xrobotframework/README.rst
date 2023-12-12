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

    # 失败重试(第一次执行)，其实只需要--output即可，但是为了看出来每次log report区别，下面指定了对应的参数(实际使用中，只需要--output即可)
    robot --output 1_output.xml --log 1_log.html --report 1_report.html test.robot
    # 如果在jenkins等进行构建，需要增加参数 --nostatusrc 以保证构建顺序
    # 重试
    robot --output 2_output.xml --log 2_log.html --report 2_report.html -R 1_output.xml test.robot
    # 合并日志(就算只有一次执行，只要知道xml文件，也可以合并，并不是非得有多个xml文件)
    # 默认不会再次生成output.xml，需要通过--output output.xml参数指定(当然如果不需要也可也不指定)
    rebot --output output.xml --merge *.xml


参考链接
--------------

* `github <https://github.com/robotframework/robotframework>`_
* `内建变量 <http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#built-in-variables>`_
* `控制结构 <http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#control-structures>`_
* `可用配置(每个块支持的配置项) <http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#available-settings>`_
* `Timeout格式 <http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#time-format>`_
* `命令行选项 <http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#command-line-options>`_
* `测试库编写 <http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#creating-test-libraries>`_
    