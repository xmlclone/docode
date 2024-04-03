# 安装

> 其它安装教程：

1. https://github.com/xmlclone/archived/tree/main/doc/k8s
2. https://github.com/xmlclone/archived/blob/main/doc/docker/docker.md

> docker安装与配置(本文安装的k8s 1.28.8已不在支持docker，故docker相关的步骤可以忽略):

本文采用vmbox安装虚拟机模拟集群操作，基础配置如下：

> 如果是虚拟机，可以把下面的1-7步在一台机器上配置好后，copy一个虚拟机(即1-8步骤均需要在所有机器操作部署)，在开始后面的设置，减少操作，如果是复制的，注意修订hostname，ip地址等

1. docker安装与配置(忽略)

```sh
apt-get -y install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | sudo gpg --no-default-keyring --keyring /usr/share/keyrings/aliyun-docker-ce.gpg --import -
add-apt-repository "deb [arch=amd64] https://mirrors.aliyun.com/docker-ce/linux/ubuntu $(lsb_release -cs) stable"
apt-get -y update

# 查找
apt-cache madison docker-ce
# 安装指定版本
apt-get -y install docker-ce=5:20.10.13~3-0~ubuntu-$(lsb_release -cs)
```

2. containerd安装与配置

containerd需要修改`/etc/containerd/config.toml`配置文件，并且把`disabled_plugins = ["cri"]`注释掉，通过命令`systemctl restart containerd`重启服务即可。

3. 两台ubuntu，系统信息如下:

```sh
# lsb_release -a
root@k8s:~# lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 22.04.4 LTS
Release:        22.04
Codename:       jammy

CPU: 4core
Memory: 4G

# master
10.0.2.101
# worker1
10.0.2.102
# worker2
10.0.2.103
```

4. 以下命令在所有主机上都需要执行

```sh
# 临时关闭swap，验证是否关闭成功，可以通过top命令查看swap属性为0表示安装成功
swapoff -a

# 一般使用永久关闭
vi /etc/fstab # 把UUID下面的一行注释掉，使用#注释，然后reboot重启即可

apt-get update && apt-get install -y apt-transport-https
curl -fsSL https://mirrors.aliyun.com/kubernetes-new/core/stable/v1.28/deb/Release.key |
    gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
echo "deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://mirrors.aliyun.com/kubernetes-new/core/stable/v1.28/deb/ /" |
    tee /etc/apt/sources.list.d/kubernetes.list
apt-get update
apt-get install -y kubelet kubeadm kubectl

# 查看版本号
root@k8s-master:~# kubectl version
Client Version: v1.28.8
Kustomize Version: v5.0.4-0.20230601165947-6ce0bf390ce3
The connection to the server localhost:8080 was refused - did you specify the right host or port?

root@k8s-master:~# kubeadm version
kubeadm version: &version.Info{Major:"1", Minor:"28", GitVersion:"v1.28.8", GitCommit:"fc11ff34c34bc1e6ae6981dc1c7b3faa20b1ac2d", GitTreeState:"clean", BuildDate:"2024-03-15T00:05:37Z", GoVersion:"go1.21.8", Compiler:"gc", Platform:"linux/amd64"}
```

5. 关闭防火墙

```sh
# 关闭防火墙
systemctl stop firewalld && systemctl disable firewalld

# 新版防火墙
ufw status
ufw disable

# 关闭selinux(22.04系统默认未启动，则不用关闭)
sed -i 's/SELINUX=enforcing/SELINUX=disabled/' /etc/selinux/config;cat /etc/selinux/config
# 临时关闭selinux
setenforce 0
```

6. 修改dns
   
直接配置`/etc/netplan/01-netcfg.yaml`文件即可

7. 配置hosts

```sh
# vi /etc/hosts，更新后可以重启一下
10.0.2.101    k8s-master
10.0.2.102    k8s-work1
10.0.2.103    k8s-work2
```

> 记得把127.0.0.1对应的k8s host注释掉

8. 修改两台虚拟机的hostname，一个是k8s-master,一个是k8s-work1,一个是k8s-work2

```sh
# 临时修改
hostname xxx

# 永久修改，直接输入需要修改的hostname即可
vim /etc/hostname
```

9. 机器之间配置免密ssh登录

```sh
# 被访问端
ssh-keygen

# 把上面生成的id_rsa.pub文件放到访问端的~/.ssh/authorized_keys文件里面即可，authorized_keys文件如果不存在可以手工创建
# 把每个其它端的pub内容写入这个文件即可
# 可以通过 cat xxx.pub >> authorized_keys
```

10. 在master机器上下发如下初始化命令

```sh
kubeadm init --apiserver-advertise-address=10.0.2.101 --pod-network-cidr=10.244.0.0/16
```

参数解释:

```sh
--kubernetes-version: 指定镜像版本，这个在docker拉取镜像缺失的时候可以使用，一般不使用此参数
--apiserver-advertise-address: k8s中的主要服务apiserver的部署地址，填自己的管理节点ip
--image-repository: 拉取的 docker 镜像源，因为初始化的时候kubeadm会去拉 k8s 的很多组件来进行部署，所以需要指定国内镜像源，下不然会拉取不到镜像
--pod-network-cidr: 这个是 k8s 采用的节点网络，因为我们将要使用flannel作为 k8s 的网络，所以这里填10.244.0.0/16就好
--kubernetes-version: 这个是用来指定你要部署的 k8s 版本的，一般不用填，不过如果初始化过程中出现了因为版本不对导致的安装错误的话，可以用这个参数手动指定
--ignore-preflight-errors: 忽略初始化时遇到的错误，比如说我想忽略 cpu 数量不够 2 核引起的错误，就可以用--ignore-preflight-errors=CpuNum
```

> 如果初始化过程中有任何ERROR，先使用`kubeadm reset`重置后，解决实际错误后，在进行初始化，同理如果还想增加一个work节点，直接复制的work1的话，需要先使用reset在join

> 如果初始化成功，请记录好join提示的命令在，后续节点加入需要使用，如果遗忘，可以通过`kubeadm token create --print-join-command`重新生成

11.  配置kubectl命令，执行如下命令即可

```sh
mkdir -p /root/.kube && \
cp /etc/kubernetes/admin.conf /root/.kube/config
```

然后使用`kubectl get nodes`测试是否正常输出

```sh
# 查看已加入的节点
kubectl get nodes

# 查看集群状态
kubectl get cs
```

12.  部署flannel

flannel是什么？它是一个专门为`k8s`设置的网络规划服务，可以让集群中的不同节点主机创建的`docker`容器都具有全集群唯一的虚拟IP地址。想要部署flannel的话直接执行下述命令即可

```sh
kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml

# 如果上面由于无法直接下载flannel的yml文件，这里找到了github的
https://github.com/flannel-io/flannel/blob/master/Documentation/kube-flannel.yml

# 把上面的文件内容复制到本地的kube-flannel.yml文件中，然后执行如下命令
kubectl apply -f kube-flannel.yml
```

13. 加入节点

```sh
# 在需要加入的节点输入kubeadm init产生的kubeadm join命令，由于每个人的不一样，不要直接复制
kubeadm join 192.168.141.9:6443 --token zh58qi.iqztqj8kbz7hffgh \
	--discovery-token-ca-cert-hash sha256:fecc44c5a652e6fbe375048ecdbd691cbb9eb185321917b393b07f6d859634da
```