#### 1. 安装pip

```
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
pip show pip （查看pip的版本信息）
```

#### 2.安装激活虚拟环境

```
Python -m venv gerapy-env
Source gerapy-env/bin/activate
virtualenv -p python2 venv
cd venv
source bin/activate
deactivate (退出虚拟环境)
```

#### 3.Centos中yum命令报错

```
File "/usr/bin/yum", line 30
except KeyboardInterrupt, e:
                            ^
SyntaxError: invalid syntax
修改usr/bin/yum第一行为python2.7
vim /usr/libexec/urlgrabber-ext-down
将/usr/bin/python改为/usr/bin/python2.7。
vim /usr/bin/yum-config-manager
解决办法同上： #!/usr/bin/python换成 #!/usr/bin/python2.7 
```

