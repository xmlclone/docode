sphinx
================

.. contents:: 


Manual doc
---------------

.. py:function:: add(a: int, b: int) -> int

    Return a + b + c.  :class:`autodoc_demo.Foo`  (注意在中间不要出现空格)

    注释内的引用方式（同样适用于代码内）：

    :class:`autodoc_demo.Foo`

    :func:`autodoc_demo2.add`

    :attr:`autodoc_demo.Foo.bar`

    :mod:`autodoc_demo2`

    :data:`autodoc_demo2.module_var`

    :meth:`autodoc_demo.Foo.sta_method`

    :param a: value a.
    :type a: int or float
    :param b: value b.
    :type b: int or float
    :param c: optional value c.
    :type c: int or float or None
    :return: sum of a b c.
    :rtype: int or float

Auto doc
---------------

autodoc_demo.Foo
^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: autodoc_demo.Foo
    :members:

上面是自动根据类的注释生成的doc，下面是一些跨引用的方式：

* :py:mod:`autodoc_demo.Foo` 
* :py:attr:`autodoc_demo.Foo.bar`
* :py:attr:`autodoc_demo.Foo.qux`
* :py:attr:`autodoc_demo.Foo.add`
* :py:meth:`autodoc_demo.Foo.cls_method`
* :py:meth:`autodoc_demo.Foo.sta_method`
* :py:data:`autodoc_demo3.module_var`


指定部分内容生成doc
^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: autodoc_demo.Foo1
    :members: add, bar


模块级别
^^^^^^^^^^^^^^^^^^^^^^

.. automodule:: autodoc_demo2
    :members:

.. autodata:: autodoc_demo3.module_var


参考链接
-------------

* `基础语法 <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_
* `PY指令 <https://www.sphinx-doc.org/en/master/usage/domains/python.html#role-py-mod>`_
* `Autodoc <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#directive-autoattribute>`_