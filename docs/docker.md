```sh
docker save -o xxx.tar imageName
docker save -o xxx.tar imageName:tag
docker load < xxx.tar
docker load -i xxx.tar

docker ps -a | grep Exited | awk '{print $1}' | xargs docker rm
```