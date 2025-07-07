# 常用命令

```sh
docker run --rm -it ubuntu /bin/bash
docker run -it -v /usr/codeFile:/opt/code test /bin/bash
docker run -it -p 5000:5000 test /bin/bash
docker exec -it ubuntu /bin/bash
docker exec -u 0 -it ubuntu /bin/bash

docker cp src [container]:dst
docker cp chromedriver test:/opt/app
docker cp [container]:src local/path

docker commit -m "commit msg" -a "author" [ID] main:tag
docker save -o xxx.tar imageName
docker save -o xxx.tar imageName:tag
docker load < xxx.tar
docker load -i xxx.tar

docker images
docker ps
docker ps -a

# 重启包含nginx名称的容器
docker ps | grep nginx | awk '{print $13}' | xargs docker restart
# 删除已经退出（Exited）的容器
docker ps -a | grep Exited | awk '{print $1}' | xargs docker rm
# 删除为none的镜像
docker images | grep none | awk '{print $3}' | xargs docker rmi

docker network create --driver bridge --subnet=172.18.0.0/16 --gateway=172.18.0.1 zknet
docker network ls
docker network list
docker run --name zk1 --privileged --network zknet --ip 172.18.0.2
```

# 源配置

配置文件: `/etc/docker/daemon.json` 或 `C:\Users\<username>\.docker\daemon.json`

```json
{
    "registry-mirrors": [
        "https://docker.hpcloud.cloud",
        "https://docker.m.daocloud.io",
        "https://docker.unsee.tech",
        "https://docker.1panel.live",
        "http://mirrors.ustc.edu.cn",
        "https://docker.chenby.cn",
        "http://mirror.azure.cn",
        "https://dockerpull.org",
        "https://dockerhub.icu",
        "https://hub.rat.dev",
        "https://proxy.1panel.live",
        "https://docker.1panel.top",
        "https://docker.m.daocloud.io",
        "https://docker.1ms.run",
        "https://docker.ketches.cn"
    ],
    "insecure-registries": ["192.168.1.100:5000"]
}
```

配置完成后需要重启docker，可以通过`docker info`查看是否生效

# docker-compose

```sh
docker-compose up
docker-compose up -d

docker-compose down
```