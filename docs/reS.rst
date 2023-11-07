=====
标题1
=====

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

直接连接到目录下其它文件 `reS1.rst`__

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


参考链接
--------

* `基础语法 <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_
* `Sphinx-Directive <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html>`_
* `Autodoc <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_


.. rubric:: Footnotes

.. [#f1] This is foot notes 1.
.. [#f2] This is foot notes 2.