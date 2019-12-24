#### 1.docker中的命令

```linux
sudo docker info # 查看是否安装成功
sudo systemctl start docker  # 启动 Docker
service docker status # 查看docker服务的状态
docker search ubuntu # 镜像搜索
docker pull ubuntu  # 下载名为ubuntu镜像 
docker images  # 查看本地已存在的镜像
docker build -t [dockerfile] .  # 生成新镜像
docker run -it ubuntu-py-test /bin/bash   # 生成新的容器，并进入
exit  # 退出容器
docker ps -a  # 查看容器及其状态
docker rm -f [CONTAINER_ID] # 删除容器
docker rmi [镜像id]  # 删除镜像
```

