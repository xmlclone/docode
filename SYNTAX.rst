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

For
=========

python
---------

.. code:: python

    for i in [1, 2, 3]:
        print(i)

    for idx, val in enumerate([1, 2, 3]):
        print(idx, val)

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

