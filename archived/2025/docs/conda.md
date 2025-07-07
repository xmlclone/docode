# 基础命令

```shell
conda info
conda env list

conda create -n mybook python=3.11
conda create -n mybook python=3.11 -y

# 激活虚拟环境(如果是没有activate命令，可以使用conda init后重新打开shell尝试)
conda activate mybook
conda deactivate mybook

# conda环境下的pip升级
python -m pip install -U pip

# linux下，如果安装时，最后指定了自动初始化conda base为基础shell，可以通过以下命令取消此默认配置
# 如果最后不指定conda base为基础shell，需要自己增加conda的路径到环境变量PATH下，一般修改~/.bashrc 修改 export PATH=$PATH:path/to/conda 后使用source ~/.bashrc生效，并且使用conda init后重新打开shell，才能使用conda activate xxx
# 如果指定了，只需要重进shell即可看见base环境
conda config --set auto_activate_base false

conda config --show

# 修改虚拟环境默认存储位置
conda config --prepend envs_dirs /new/path/for/envs
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

设置完成后，需要使用下列命令:

```sh
conda clean -i
conda info
```

# 重命名虚拟环境名

```sh
# 一般通过重命名envs下的目录名即可更新

# 但在wsl下遇见更新目录名并激活虚拟环境后，执行pip或者其它比如locust会提示找不到python解释器
# 仔细看日志，发现查找的python解释器路径还是原始的目录名，解决办法如下
# (已解决)暂时未解决，目前使用删除了旧的虚拟环境重新创建
# 先卸载在安装对应的包即可
python -m pip uninstall XXX
python -m pip install XXX
```

# linux虚拟环境包路径

一般在`/anaconda3/envs/<you venv name>/lib/python3.9/site-packages`下