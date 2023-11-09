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

    # 字符串操作
    print(len(a))

Array/List/Map...
====================

If
==========

python
---------

.. code:: python

    if a:
        code
    elif b > 0:
        code
    else:
        code

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

