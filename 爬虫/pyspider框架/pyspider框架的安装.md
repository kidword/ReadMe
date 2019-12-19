#### 1. windows下安装

```
1.错误: Command "python setup.py egg_info" failed with error code 10 in
2.访问下载对应的安装包：https://www.lfd.uci.edu/~gohlke/pythonlibs/#
3.启动时错误：- Deprecated option 'domaincontroller': use 'http_authenticator.domain_controller' instead
4.去Lib中site-packages\pyspider\webui.py修改
修改:
	'domaincontroller': NeedAuthController(app)
修改为:
	'http_authenticator':{
        'HTTPAuthenticator':NeedAuthController(app),
    },
```

