### 1. 安装pyinstaller

```python
pip install pyinstaller
```

### 2. 测试编写的程序在cmd中是否能运行起来

```python
python run.py
```

### 3. 开始打包

```python
# 带黑窗口的打包方式
pyinstaller -F run.py
# 不带黑窗口的打包方式（后台运行）
pyinstaller -w run.py
# 给exe文件设置图片
pyinstaller -w -i fire.ico run.py
```

### 4. 执行成功后

​		在dist文件中查找打包生成的exe文件，目前在dist/run/run.exe。

​		