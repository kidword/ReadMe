#### selenium基本操作和使用 

```python
from selenium import webdriver
browser = webdriver.Chrome()
browser.get("https://www.baidu.com")
```

#### 执行javascript

```python
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
browser.execute_script('alert("driver Bottom")')
```

#### 切换Frame

```python
from selenium.common.exceptions import NOSuchElementException

browser.switch_to.frame('iframeResult')   # 切换到子frame里面
try:
	browser.find_elements_by_id('logo')
except NOSuchElementException:
	print('没找到')
browser.switch_to.parent_frame()   # 切回到父级frame
```

#### 延时等待

* 隐式等待

当时用隐式等待执行测试的时候，如果selenium没有在DOM中找到节点，将继续等待，超过设定时间后，则抛出找不到节点的异常。

```
browser.implicitly_wait(10)
```

* 显示等待

指定的查找节点，然后指定一个最长等待时间。如果在规定时间内加载出来这个节点，就返回查找的节点；如果在规定的时间内依然没有加载出该节点，则抛出异常。

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get("https://www.taobao.com")
wait = WebDriverWait(browser,10)
input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
print(input, button)
```

####  反屏蔽

```
from selenium.webdriver import ChromeOptions

option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_experimental_option("useAutomationExtension", False)
# 配置无头浏览
# option.add_argument('--headless')
browser = webdriver.Chrome(options=option)
browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",
                        {'source': 'Object.defineProperty(navigator, "webdriver",{get:() => undefined})'})
                        
browser.get('http://ah.gsxt.gov.cn/index.html')
```

### selenium 添加代理请求
```
from selenium import webdriver
import time

from file_action.mogu_ip import MoGu

mogu = MoGu()
ip = mogu.get_ip
print('ip:', ip)
options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=http://' + ip)
browser = webdriver.Chrome(options=options)
browser.get('https://httpbin.org/get')
print(browser.page_source)

time.sleep(20)
browser.quit()

```

### selenium 携带cookie请求登录后的页面
```
# !/bin/bash
# -*- coding: utf-8 -*-
"""
@author kidword
@desc 先模拟登陆以后，使用selenium的get_cookies方法将网站的cookies保存到本地文件，
      本模块使用selenium读取本地cookies以后，访问登录之后的界面
@date 2020/08/04
"""


import json
from selenium import webdriver


class SeleniumCookie:
    def __init__(self):
        self.driver = webdriver.Chrome()
        # 目标url
        self.targer_url = "http://data.cma.cn/order/list/show_value/normal.html"

    def close(self):
        self.driver.quit()

    def req(self):
        # 初次建立连接，随后方可修改cookie
        self.driver.get(self.targer_url)
        # 删除第一次建立连接时的cookie
        self.driver.delete_all_cookies()
        # 读取登录时存储到本地的cookie
        with open('cookies.json', 'r', encoding='utf-8') as f:
            listCookies = json.loads(f.read())

        try:
            for cookie in listCookies:
                self.driver.add_cookie(cookie)
            # 再次访问页面，便可实现免登陆访问
            print('再次请求')
            self.driver.get(self.targer_url)
        except Exception as e:
            print(e)

```
