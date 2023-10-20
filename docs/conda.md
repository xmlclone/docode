# 基础命令

```shell
# 查看帮助
conda --help
conda create --help

# 查看信息
conda info

# 查看虚拟环境列表
conda env list

# 创建虚拟环境，并指定python版本
conda create -n mybook python=3.11
# 直接安装，不提示确认信息
conda create -n mybook python=3.11 -y

# 激活虚拟环境
conda activate mybook
# 退出虚拟环境
conda deactivate mybook

# conda环境下的pip升级
python -m pip install -U pip
```