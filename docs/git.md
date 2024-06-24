# 常用操作

```sh
# 查看已经被跟踪的文件
git ls-files -c
# 查看被修改的文件(新增的不算)
git ls-files -m
# 查看被删除的文件(已经被跟踪的)
git ls-files -d
# 查看新增的将要被跟踪的文件
git ls-files -o --exclude-standard


# 恢复到add之前
git reset HEAD .
```

# 国内访问受限

访问下面的所有域名IP，更新到hosts文件后重新访问即可，比如linux下一般是修改`/etc/hosts`，注意备份；
如果访问失效，可以重新访问下面地址后更新IP。

https://ip.tool.chinaz.com/assets-cdn.github.com
https://ip.tool.chinaz.com/github.global.ssl.fastly.net
https://ip.tool.chinaz.com/github.com

> 国内建议使用以下配置

```sh
151.101.113.194 github.global.ssl.fastly.net
192.30.253.112 github.com
185.199.109.153 assets-cdn.github.com
185.199.110.153 assets-cdn.github.com
185.199.111.153 assets-cdn.github.com
```

# 基本命令

```shell
# 初始化一个git仓库
# 首先进入希望的目录，输入下面命令
git init

# 克隆远程仓库
git clone url
git clone -b dev url #克隆指定的分支/指定tag也用相同的命令，-b dev的dev指定为tag即可

# 推送
git push
git push origin master
git push origin master:master (本地分支名:远程分支名)
git push origin dev:dev
git push -u origin dev:dev (把默认的推送到origin dev:dev，后续就可以直接使用git push方式)

# 查看远程地址
git remote -v

# 回退管理
# 注意HEAD表示当前，HEAD^表示上一次提交，可以通过git log查看当前处于哪个commit
# 一次commit表示一个版本，add不算是一个版本
git reset --hard HEAD^  直接把整个工作区恢复到初始状态，会删除文件
git reset --mixed HEAD^ 退回到add之前
git reset --soft HEAD^  退回到commit之前
git reset --mixed 是默认行为

# 查看分支
git branch # 只查看本地的
git branch -a # 本地和远程

# 创建分支(改动的代码不会恢复，即新分支仍然是改动后的代码，不用担心创建新分支后代码丢失)
git checkout -b new_branch

# 切换分支
git checkout new_branch_name

# 暂存
git stash
# 然后在需要的任何地方使用pop把暂存内容弹出
git stash pop

# 分支合并，比如要把new_branch_name分支合并到master分支，首先需要切换到master分支
git checkout master
git merge new_branch_name

# 删除分支
git branch -d delete_branch

# tag
git tag -a v1.0 -m "commit msg"
git tag #查看tag
git tag --list #查看tag
git tag -l v1.* #查看指定模式的tag
git push origin v1.0 #推送指定tag
git push --tags #推送所有tag
git push origin --tags #推送所有tag
git tag -d v1.0 #删除tag
git push origin :refs/tags/v1.0 #删除远程tag

# 拉取远程所有信息
git fetch origin --prune

# 查询远程tag
git ls-remote --tags origin
```

# 配置

```shell
# 配置, global是全局配置，local是当前仓库的配置
git config -l #查看
git config --local/global/system -l
git config --global core.editor vim
git config --global core.editor "'C:/Program Files (x86)/Notepad++/notepad++.exe' -multiInst -notabbar -nosession -noPlugin"

git config --global user.name test
git config --global user.email test@test.com
ssh-keygen -t rsa -C test@test.com -b 4096

# 配置代理(全局配置，如果只想对当前git仓库生效，可以不用--global选项)
git config --global http.proxy "127.0.0.1:7790"
git config --global https.proxy "127.0.0.1:7790"
# 取消代理配置
git config --global --unset http.proxy
git config --global --unset https.proxy
```

> `ssh-keygen`可以增加多个账号，在生成配置文件时，会提示文件保存路径，我们可以自定义自己的，比如命名为testxxx(默认是`id_rsa.pub`和`id_rsa`两个文件)
> 需要在`.ssh`目录下，需要增加一个`config`文件，文件配置如下:

```
Host github.com    # 这个建议配置和下面的hostname一致           
    HostName github.com
    IdentityFile C:\\Users\\linlei\\.ssh\\testxxx   #这里不需要加.pub后缀
    PreferredAuthentications publickey
    User 这里可以填写用户名和邮箱即可
```

> 参考: [在同一台电脑上添加多个ssh key](https://blog.csdn.net/iss_jin/article/details/121901985)

# 拉取远程非master分支

```shell
# 先拉取分支
git fetch origin dev

# 在关联分支
git checkout -b dev origin/dev

# 更新
git pull origin dev
```

> 更简单的方式(拉取全部分支):

```shell
git fetch origin
git checkout new-branch
```

# 拉取指定commit id代码

```shell
# 首先需要在仓库找到指定的commit id, 假如为idx

# 拉取最新的代码，如果有分支指定-b参数，如果直接拉master，则不用指定
git clone http://xxx/yyy.git -b branch

# 恢复到指定的commit id
git reset --hard idx

# 恢复到先前一个版本
git reset --hard HEAD^

# git status 看见提示有xx个commit，提示可以git pull更新，此时如果就想保持当前代码，比如前面忘了设置tag，想给这里代码加tag，可以在这里直接操作
git tag -a vv
git tag -a -m "commit message"  tagnum
git push origin vv
```

# 在已有目录下创建仓库并且关联到远程

```shell
# 创建 git 仓库
mkdir apiscan
cd apiscan
git init
touch README.md
git add README.md
git commit -m "first commit"
git remote add origin xxx.git
git push -u origin master

# 已有仓库的情况
cd existing_git_repo
git remote add origin xxx.git
git push -u origin master
```

# gitignore

在git仓库下创建.gitignore文件

1. 如果要忽略所有.pyc文件，在文件里面增加一行`*.pyc`
2. 如果要反向匹配，使用如下

```
# 即忽略所有config-开始的yaml文件，但是config-dev.yaml和config-prod.yaml除外
config-*.yaml
!config-dev.yaml
!config-prod.yaml
```

# gitlab使用

## 设置保护分支

settings->repository->default branch 设置为dev分支(非master分支)

settings->repository->protected branches 设置master为保护分支，并且设置只有maintainers有merge和push权限(默认已经配置)

在仓库目录下点击branches可以看见所有分支，会提示是否保护

## 权限

1. master分支默认只允许master角色推送，devepoper不允许推送，但是可以发起merge请求

## merge

![](https://github.com/xmlclone/archived/blob/main/doc/git/img/gitlab_merge1.png)
![](https://github.com/xmlclone/archived/blob/main/doc/git/img/gitlab_merge2.png)
![](https://github.com/xmlclone/archived/blob/main/doc/git/img/gitlab_merge3.png)
![](https://github.com/xmlclone/archived/blob/main/doc/git/img/gitlab_merge4.png)
![](https://github.com/xmlclone/archived/blob/main/doc/git/img/gitlab_merge5.png)
![](https://github.com/xmlclone/archived/blob/main/doc/git/img/gitlab_merge6.png)

# github使用

## issue/PR

由于本章节覆盖了PR的操作，故对PR不单独进行说明

### 创建issue

![](static/img/github-issue1.png)

### 普通方式处理issue(不推荐)

![](static/img/github-issue2.png)

### 分支方式

![](static/img/github-issue3.png)
![](static/img/github-issue4.png)

处理完成后在本地仓库使用以下命令关联新分支:

```shell
git fetch origin
git checkout 2-test-issue
```

修改缺陷，提交代码到分支上，然后提交PR:

![](static/img/github-issue5.png)
![](static/img/github-issue6.png)

然后合并分支

![](static/img/github-issue7.png)

确认后，此时issue和pr都关闭了。

还可以删除分支(这里只是删除了远程分支，本地的分支仍然存在)

![](static/img/github-issue8.png)

# 冲突处理

## 非相同文件或相同文件不同的位置

当A同事修改了X文件，B同事修改了Y文件，A同事先提交，B同事经过add commit后push会报错，B同事可以使用git pull --rebase，在使用push即可

> 注意这个是add commit后，通过push发现不对的时候使用

# 问题记录

## github不显示图片问题

图片的md仍然采用默认的语法，比如![j1](./imgs/j1.png)，此时上传到github后不能打开图片，是因为我们网络不通，使用如下办法解决

1. 访问[ip138](https://site.ip138.com/raw.githubusercontent.com/)，输入你不通的域名，解析到ip后
2. 修改`C:\Windows\System32\drivers\etc\hosts`文件(windows)，把IP和域名修改为我们查询到的内容，然后再次访问即可

比如我们在hosts文件增加如下配置:

```
185.199.111.133 raw.githubusercontent.com
```

## 中文乱码

```sh
git config --global core.quotepath false
```

## git bash中文件名显示一堆数字

1. 增加下面的配置
```shell
git config core.quotepath false
```

2. 修改options-text-locale选择zh_CN, Character set选择UTF-8

## git add删除文件

```shell
git add * #删除的文件可能不会跟踪起来
git add . #可以使用这个
```

# 恢复

```shell
git reset --hard HEAD^
git reset --mixed HEAD^ 退回到add之前
git reset --soft HEAD^  退回到commit之前
```

## 本地删除文件重新同步远程文件

```shell
git fetch --all  
git reset --hard origin/master 
git pull
```

# 远程仓库更新密码后

需要在本地执行如下命令(使用管理员权限执行)

```shell
git config --system --unset credential.helper

# 上面命令执行后，后面每次都需要输入密码，可以执行下面命令后，只需要输入一次密码即可
git config --global credential.helper store
```

# 基础概念

## Merge Request 和 Pull Request(PR)

最终结果就是他们俩基本是一个意思，只不过在github上叫pull request，而在gitlab上叫merge request