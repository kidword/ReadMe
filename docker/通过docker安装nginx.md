## 通过docker安装nginx

1. 首先拉取nginx镜像（这里选择的是nginx最新稳定版）

   ```shell
   # docker pull nginx:stable
   ```

2. 通过运行nginx镜像来创建一个nginx容器

   ```shell
   # docker run -d -p 80:80 --name my-nginx -v /usr/local/nginx/html:/usr/share/nginx/html -v /usr/local/nginx/logs:/var/log/nginx nginx:stable
   ```

3. 查看启动的nginx容器的id

   ```shell
   # docker ps
   ```

4. 进入到宿主机的与nginx容器的共享数据卷目录，然后把nginx容器的nginx.conf配置文件复制到宿主机

   ```shell
   # cd /usr/local/nginx
   # mkdir conf && cd conf
   # docker cp ebe41cecacdb:/etc/nginx/nginx.conf .
   ```

5. 删除刚刚运行的nginx容器

   ```shell
   # docker rm -f ebe41cecacdb
   ```

6. 重新通过nginx镜像运行nginx容器，并配置共享数据卷

   ```shell
   # docker run -d -p 80:80 --name my-nginx -v /usr/local/nginx/conf/nginx.conf:/etc/nginx/nginx.conf -v /usr/local/nginx/html:/usr/share/nginx/html -v /usr/local/nginx/logs:/var/log/nginx -v /usr/local/nginx/ssl:/ssl nginx:stable
   ```

7. 在浏览器通过80端口访问，可以看到nginx的欢迎页面，至此，nginx安装启动成功