=================
Syntax
=================


.. contents:: 

Variable
===============

python
--------

.. code:: python

    a = 1
    b: int = 2

String
========

python
---------

.. code:: python
    
    # 字符串定义
    a = '123'
    b = "456"
    c = '''789'''
    d = """012"""

    # 字符串格式化
    a.format()
    print(f"{}")

    # 字符串连接
    # 1 + "2"   python不支持字符串和数值类型直接通过+连接，java、groovy等可以通过+号连接形成一个新的字符串，但是python不行，但是可以通过字符串格式化的方式达到此目的

    # 字符串操作
    print(len(a))

.. code:: groovy

    // groovy也支持 和python一样的定义字符串的引号方式，也就是单引号，双引号，三引号都支持

Array/List/Map...
====================

If
==========

python
---------

.. code:: python

    # python 逻辑运算使用的是 and or not
    if a:
        code
    elif b > 0:
        code
    else:
        code

groovy
---------

.. code:: groovy

    // groovy 逻辑运算使用的是 && || !    & | ^ ~
    if (a > 0) {
        println("a > 0")
    } else if (a < 0) {
        println("a < 0")
    } else {
        println("a = 0")
    }

For
=========

python
---------

.. code:: python

    # python没有for(var; exp; inc)，可以简单想象为python没有++ --运算符
    for i in [1, 2, 3]:
        print(i)

    for idx, val in enumerate([1, 2, 3]):
        print(idx, val)

groovy
------------

.. code:: groovy

    for (int i = 0; i < 5; i++) {
        println("loop for: " + i)
    }

    for (i in 5..10) {
        println("loop for in: " + i)
    }

While
============

Switch
============

Function
==============

python
----------

.. code:: python

    def f1():
        ...

    def f2(a, b=2):
        return a + b

    def f3(a, *args):
        ...

    def f4(a, **kwargs):
        ...

    def f5(a, /, c):
        ...

    def f6(a, *, c):
        ...

groovy
--------------

.. code:: groovy

    // 定义方式与python类似，也支持位置参数的方式

Class
==========

Exception
============

Import
==========

python
---------

.. code:: python

    import os
    from os import path
    from os import path as os_path

Commnets(注释)
================

python
-----------

.. code:: python

    # 单行注释

    """
    多行注释
    """

groovy
----------

.. code:: groovy

    // 单行注释

    /*
    多行注释
    */

