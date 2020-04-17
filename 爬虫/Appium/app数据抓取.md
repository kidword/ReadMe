#### 1.简单

​		app里的数据比web端更容易抓取，反爬也没有那么强，大部分也都是http/https协议，返回的数据类型大多数为json。

#### 2. 困难

1. 可能需要适当的反编译，分析出加密算法并抓取到信息
2. 可能加固，需要脱壳，然后反编译，分析出加密算法并抓取到信息
3. 需要破解通过各式各样的签名，证书，设备绑定等方法，找到隐藏加密算法。

#### 3.查看app包名

E:\tools\android-SDK\build-tools\29.0.2>aapt.exe dump badging E:\迅雷下载\kaoyanbang_3.5.6.1.273.apk

#### 4.查看夜神模拟器的服务端口

根据PID条件查看windows进程，找到NoxVMHandle Frontend的pid，然后执行cmd中执行netstat -ano | findstr "2148"命令，夜神模拟器的端口号有规律，一般为62001 、62005之类的，最后在cmd中输入adb connect 127.0.0.1:62001，则连接成功。

#### 5.mitmdump和python脚本交互

```
mitmdump -p 8889 -s test.py
```

#### 6. 当执行adb devices命令时，出现 adb server version(36) doesn't math this client(40);kill时

需要把高版本的adb同步到低版本中去。

将E:\tools\android-SDK\platform-tools下的三个文件adb.exe、AdbWinApi.dll、AdbWinUsbApi.dll拷贝到夜神模拟器中的E:\tools\yeshen\Nox\bin里面，备份文件以后点击覆盖，将adb.exe替换nox_adb.exe文件，最后版本同步成功，目的是将Android的adb版本和夜神模拟器的同步到一个版本。