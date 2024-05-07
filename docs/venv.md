```sh
# 默认创建出来的python版本和你本地使用的python版本一致
# 会在你指定的目录生成一个venv1的文件夹，里面包含虚拟环境的信息

# –-system-site-packages 指定了此参数，表示虚拟环境可以使用系统环境安装的包
# 比如系统环境有requests，默认情况新建的虚拟环境无法访问requests
# 要么通过激活虚拟环境后使用pip install requests安装
# 要么指定此参数
# 差别在pyvenv.cfg文件的include-system-site-packages = false配置是true还是false

python -m venv venv1

# 激活和去激活，windows直接运行bat，linux可以使用source命令
Scripts\activate
Scripts\deactivate

# 激活虚拟环境后通过pip安装的包，会在虚拟环境内部，不影响其它虚拟环境
# 安装在虚拟环境的Lib\site-packages里面
pip install requests

# 删除虚拟环境，直接删除对应的目录即可

# ****************************************************************！！！！！！！！！！
# venv不像conda的虚拟环境
# conda的虚拟环境，可以直接把整个目录打包放到其它同操作系统的机器上，就可以使用虚拟环境了
# venv直接打包(比如上面创建的venv1)放到其它机器上是无法直接使用的
# 除非两个机器的python相关配置完全一致(包括python路径、版本等)
```