=============
README
============


.. contents:: 


NPM
=================

.. code:: console

    # 初始化一个项目(创建package.json文件)， --yes简化操作步骤
    npm init
    npm init --yes

    # 安装包，-g表示安装到全局的node_modules下，否则安装到本项目的node_modules下
    npm install express
    npm install -g express 

    # 根据package.json文件的依赖进行安装
    npm install

    # 执行package.json的script
    npm run <script>
