# 常用命令

```sh
# 忘记密码处理方式
# 先查看你的分发版本名称，比如Ubuntu-22.04
wsl -l
# 以root身份进入，进入后，就可以通过passwd <username>进行重置密码了
wsl -u root -d Ubuntu-22.04


# linux里面访问宿主机资源
# 一般挂载在/mnt目录下，比如c盘，就在/mnt/c
# windows访问wsl
# 一般通过windows的资源管理器访问 \\wsl.localhost\Ubuntu-22.04，通常资源管理器左边会显示Linux共享

# 查看正在运行的
wsl --list --running

# 停止所有
wsl --shutdown
# 停止某一个
wsl --terminate <name>

# 配置文件(每个配置文件可配置的内容可能不一样，比如.wslconfig可以配置memory)
cat /etc/wsl.conf  # 针对单独某个发行版生效
cat .wslconfig     # 全局生效，一般在%UserProfile%下，比如C:\Users\<UserName>\.wslconfig，如果不存在可以手动创建
```

# 修改基于WSL的docker-desktop的docker配置

```sh
# 查看wsl发行版
wsl --list --verbose

# 进入发行版，一般都叫docker-desktop
wsl -u root -d docker-desktop

# 找到配置文件(配置文件名有可能是其它的，比如config.json、daemon.json或docker.json)
find / -name docker.json
```

# QA

## WSL内部中文显示乱码

# 参考

1. [wls.conf和.wslconfig](https://learn.microsoft.com/en-us/windows/wsl/wsl-config#configure-global-options-with-wslconfig)