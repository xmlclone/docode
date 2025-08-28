# 常用命令

```sh
npm init
npm init -y

npm install
npm install express
npm install express -D
npm install -g express
npm uninstall express
npm remove
npm update express

npm -v 
npm list
npm config list

# 执行 package.json 的 scrpts 下定义的命令
npm run build
npm run start
```

# 镜像源

```sh
# 查看镜像源
npm config get registry

# 镜像源配置
npm config set registry https://registry.npmmirror.com
# npm config set registry https://npm.aliyun.com
npm config set registry http://mirrors.cloud.tencent.com/npm/
# npm config set registry https://mirrors.huaweicloud.com/repository/npm/
```