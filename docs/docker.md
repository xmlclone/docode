# 常用命令

```shell
# 批量重启某些服务
docker ps | grep nginx | awk '{print $13}' | xargs docker restart
# 批量删除服务
docker ps | grep nginx | awk '{print $13}' | xargs docker restart
```

# 基础命令