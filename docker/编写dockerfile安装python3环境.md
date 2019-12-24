#### 1.编写dockerfile文件

​	文件名：pyenv-dockerfile

```linux
# 基础镜像来源
FROM ubuntu 
# 镜像制作者
LABEL author="itcast" 

# 安装python3.6必要的包。
# 安装ifconfig vim curl wget等工具
RUN apt-get update
RUN apt-get install -y vim net-tools curl wget

#安装python
RUN apt-get install -y python3
RUN apt install -y python3-dev
RUN apt install -y python3-venv

#安装pip
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py

# print()时在控制台正常显示中文
# ENV PYTHONIOENCODING=utf-8
```

#### 2.创建指定名称的新镜像

```
1.生成名为pyenv-dockerfile的新镜像
	docker build -t pyenv-dockerfile .
	
2.查看新生成的镜像 docker images
```

#### 3.执行命令生成新的容器，并进入

```
docker run -it pyenv-dockerfile /bin/bash
```

#### 4.运行一个简单的python程序

```
cd /home
vi a.py

print('this is my docker-python!')
python3 a.py
```

### 5.退出容器

 在容器中的终端执行`exit` 