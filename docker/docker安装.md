#### 1.安装 Docker

```linux
1.使用docker仓库进行安装
    sudo yum install -y yum-utils \
    device-mapper-persistent-data \
    lvm2
  
2.设置稳定的仓库
    sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo

3.最新版本的 Docker
	sudo yum install docker-ce docker-ce-cli containerd.io

4.启动 Docker
	sudo systemctl start docker

5.通过运行 hello-world 映像来验证是否正确安装了 Docker
	sudo docker run hello-world
```

