Sphinx Demo
================

.. contents:: 目录

基础使用
----------

.. code:: console

    # 安装
    pip install sphinx

    # 快速生成一个基础的目录
    sphinx-quickstart

    # 编译
    sphinx-build -M html source build
    
    # 如果make工具，也可以使用下面的make命令
    # Makefile里面也就是替换为了 sphinx-build -M html source build
    make html

    # 编译为单个html文件
    # sphinx-build -M singlehtml source build
    make singlehtml

    # 编译为pdf，首先需要安装相关依赖
    sudo apt install texlive-latex-base
    sudo apt-get install latexmk
    pdflatex --version
    latexmk --version
    sudo tlmgr install cmap
    make latexpdf

参考连接
--------

* `基础语法 <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_
* `详细语法 <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#quick-syntax-overview>`_
* `Sphinx指令 <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html>`_
* `Autodoc <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_
* `PY指令 <https://www.sphinx-doc.org/en/master/usage/domains/python.html#role-py-mod>`_
* `配置文件 <https://www.sphinx-doc.org/en/master/usage/configuration.html>`_
* `shields.io <https://shields.io/badges>`_