```sh
git clone url
git clone -b dev url #克隆指定的分支/指定tag也用相同的命令，-b dev的dev指定为tag即可

git push
git push origin master
git push origin dev
git push origin master:master (本地分支名:远程分支名)
git push origin dev:dev

# 本地已有main分支，需要拉取远程dev分支
git pull   # 一定先pull
git checkout -b dev origin/dev

git branch -d dev

git stash
git stash pop
```