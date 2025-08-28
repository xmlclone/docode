```sh
git clone url
git clone -b dev url #克隆指定的分支/指定tag也用相同的命令，-b dev的dev指定为tag即可

git push
git push origin master
git push origin dev
git push origin master:master (本地分支名:远程分支名)
git push origin dev:dev

# 本地已有main分支（相当于已经git clone了），需要拉取远程dev分支
git pull   # 一定先pull
git checkout -b dev origin/dev

# 删除dev分支
git branch -d dev

git stash
git stash pop


ssh-keygen -t rsa -C test@test.com -b 4096

# -l 代表 --list
# 不加 --global 或 --local 时，默认是 --local
git config --global -l
git config --local -l

# 配置代理(全局配置，如果只想对当前git仓库生效，可以不用--global选项)
git config --global http.proxy "127.0.0.1:7890"
git config --global https.proxy "127.0.0.1:7890"
# 取消代理配置
git config --global --unset http.proxy
git config --global --unset https.proxy


# git add 后发现操作失误，需要恢复
git reset  # 恢复到git add 之前，并且不会影响已经改动的文件
git reset -- README.md  # 只会对README.md取消 git add 操作，不会影响README.nd内容
git reset --hard  # ！危险，会把更改的文件恢复到之前的版本，如果是新增的文件会被删除
```