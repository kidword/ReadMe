#### 1. Appium安装包下载地址

```
https://github.com/appium/appium-desktop/releases
```

#### 2. android环境搭建

```
# 1.下载android studio 安装包
https://developer.android.google.cn/studio/

# 2.安装android SDK
```

#### 3. 配置环境变量

```
# 1.在系统环境变量中添加
    ANDROID_HOME
    H:\tools\android-sdk

# 2.在path中添加以下内容：
	%ANDROID_HOME%
	%ANDROID_HOME%\tools
	%ANDROID_HOME%\platform-tools
	%ANDROID_HOME%\build-tools

# 3.打开cmd输入 adb命令，检查环境变量是否配置好
	adb devices -l
	将Android手机通过数据线和运行 Appium 的 PC 相连，同时打开USB调试功能，确保PC可以连接到手机
```

#### 4. 编辑Appium配置

```
platformName，平台名称，需要区分是 Android 还是 iOS，此处填写 Android。
deviceName，设备名称，是手机的具体类型。
appPackage，APP 程序包名。
appActivity，入口 Activity 名，这里通常需要以.开头。
```

#### 5.如何获取appActivity值

```
# 1.cmd中输入：
 	adb shell
# 2.继续输入：monkey -p uni.UNI2717CC7 -v -v -v 1
	PD1616:/ $ monkey -p uni.UNI2717CC7 -v -v -v 1

 // Allowing start of Intent { act=android.intent.action.MAIN cat=[android.intent.category.LAUNCHER] cmp=com.taobao.taobao/com.taobao.tao.welcome.Welcome } in package com.taobao.taobao
 
 cmp 后面就是appActivity的值。
 
可参考appium参数配置链接：https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/caps.md
```

