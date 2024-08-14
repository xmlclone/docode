# 镜像地址

1. [清华大学](https://mirrors.tuna.tsinghua.edu.cn/)
2. [清华大学-帮助](https://mirror.tuna.tsinghua.edu.cn/help/AOSP/)
3. [阿里巴巴](https://developer.aliyun.com/mirror/)

# anaconda

1. 配置文件为`$HOME/.condarc`，windows用户可以使用`conda config --set show_channel_urls yes`生成配置文件
2. 文件内容如下:

```sh
channels:
  - defaults
show_channel_urls: true
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch-lts: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  deepmodeling: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/
```

3. 使用`conda clean -i`清除缓存