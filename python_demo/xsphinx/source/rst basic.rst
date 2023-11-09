=====
标题1
=====

.. contents:: 目录

标题2
=====

标题3
-----


*text*  **text**  ``code``  

* list1
  
  * sub list1
  * sub list2
  
* list2
* list3

1. list1
2. list2
3. list3

#. list1
#. list2
#. list3


#. `链接语法1 <https://www.baidu.com>`_
#. 链接语法2_
#. `链接语法3`__

__ https://www.baidu.com

.. _链接语法2: https://www.baidu.com

`另外一个链接4`__

__ https://github.com/

直接连接到目录下其它文件 `<reS1.rst>`__

.. This is comments.

..
    This is multiline commnets.
    Other.


这里有脚注 [#f1]_


这是另外一种代码形式::

  def add(a, b):
    return a + b


另外一个代码形式:

.. code:: python

  def add(a, b):
    return a + b


|r|

.. substitution 定义在conf.py内部

|version|

|release|


``note``、 ``warning`` 等依赖于主题的展示情况。

.. note:: 
  This is note.

.. warning:: 
  This is warning.


.. image:: https://img.shields.io/github/license/xmlclone/pdesign.svg



``topic``、 ``sidebar`` 也依赖于主题的展示情况。

.. topic:: 这是topic

  这是Topic内容。

.. sidebar:: 这是sidebar

  这是sidebar内容。


+------------------------+------------+----------+----------+
| Header row, column 1   | Header 2   | Header 3 | Header 4 |
| (header rows optional) |            |          |          |
+========================+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | column 4 |
+------------------------+------------+----------+----------+
| body row 2             | ...        | ...      |          |
+------------------------+------------+----------+----------+


=====  =====  =======
A      B      A and B
=====  =====  =======
False  False  False
True   False  False
False  True   False
True   True   True
=====  =====  =======


参考链接
--------

* `基础语法 <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_
* `Sphinx-Directive <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html>`_
* `Autodoc <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_

.. rubric:: Footnotes

.. [#f1] This is foot notes 1.
.. [#f2] This is foot notes 2.

.. |r| unicode:: U+00AE