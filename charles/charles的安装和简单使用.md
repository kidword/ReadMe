#### 1. 安装

* 安装包为：charles-proxy-4.2.8-win64.msi
* 激活： charles.jar
* 安装好charles以后，先不要启动，替换Charles/lib/charles.jar包以后在启动

### 2. 配置charles

* 在Proxy中的Proxy Setting中查看端口，默认是8888（一般不用修改端口号）
* 配置证书
  * 在help中SSL Proxying安装证书
  * 里面有两个install都需要安装
  * 安装时选择受信任的根证书颁发机构
  * 如果不安装证书，大部分链接都会显示unknwn和乱码
* APP端配置
  * 在wifi设置中选择手动代理，输入pc上的ip地址和charles的设置的端口号
* 以上操作完毕以后，基本配置成功，可正常使用

#### 3. charles抓取chrome浏览器中数据

​		在charles中 Proxy/SSL Proxying setting 中点击add按钮，host : *    port：443 ，这样就解决了charles不能抓取https数据问题。

