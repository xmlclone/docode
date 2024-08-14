# 安装和运行

```shell
pip install jupyterlab
jupyter lab

pip install notebook
jupyter notebook
```

# 远程访问

```sh
# 生成配置文件，一般在 ~/.jupyter/jupyter_notebook_config.py
jupyter notebook --generate-config

# 生成访问密码(可选)
jupyter notebook password


c.NotebookApp.allow_origin = '*'     # 允许所有来源访问
c.NotebookApp.ip = '0.0.0.0'         # 监听所有的 IP 地址
c.NotebookApp.open_browser = False   # 不自动打开浏览器

# 密码配置(可选)
c.NotebookApp.password_required = True    # 启用密码验证
c.NotebookApp.password = 'your_password'  # 设置之前生成的密码


# 启动
jupyter notebook
```

新版本配置:

```sh
c.ServerApp.allow_origin = '*'
c.ServerApp.ip = '0.0.0.0'
c.ServerApp.open_browser = False
# password 直接使用 jupyter notebook password 生成的密码即可
```

## lab远程

```sh
c.ServerApp.allow_origin = '*'
c.ServerApp.ip = '0.0.0.0'
c.ServerApp.open_browser = False
# password 直接使用 jupyter lab password 生成的密码即可

jupyter lab password
jupyter lab
```