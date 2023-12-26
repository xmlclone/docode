```sh
# 忘记密码处理方式
# 先查看你的分发版本名称，比如Ubuntu-22.04
wsl -l
# 以root身份进入，进入后，就可以通过passwd <username>进行重置密码了
wsl -u root -d Ubuntu-22.04


# linux里面访问宿主机资源
# 一般挂载在/mnt目录下，比如c盘，就在/mnt/c
```