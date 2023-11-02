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

# 修改conda源

在`$HOME/.condarc`文件更新(创建)如下内容:

```yml
channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
  - defaults
ssl_verify: true
show_channel_urls: true
```

或者用阿里云:

```yml
channels:
  - https://mirrors.aliyun.com/anaconda/pkgs/main/
  - https://mirrors.aliyun.com/anaconda/pkgs/free/
  - https://mirrors.aliyun.com/anaconda/cloud/conda-forge/
  - https://mirrors.aliyun.com/anaconda/cloud/pytorch/
  - defaults
ssl_verify: true
show_channel_urls: true
```