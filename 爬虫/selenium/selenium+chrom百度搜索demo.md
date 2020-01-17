```python
import time
from db.pgdb import PgSql
from selenium import webdriver


pg = PgSql()
driver = webdriver.Chrome()

url = 'https://www.baidu.com/'


# 从数据库中查询数据
def selectData():
    sql = 'select school from schools_yl'
    data = pg.select(sql)
    return data

# 请求百度
driver.get("https://www.baidu.com/")
no_link = []  # 获取不到的数据添加到数组中
for i in selectData():
    kw = driver.find_element_by_id('kw').send_keys(i[0])  # 获取文本并发送搜索字段
    driver.find_element_by_id('su').click()  # 获取百度一下按钮，并点击
    time.sleep(2) 
    # 获取url链接地址
    url_link = driver.find_element_by_xpath('//*[@id="1"]/h3/a[1]').get_attribute('href')
    if url_link:
        print(url_link)
    else:
        no_link.append(i[0])
        print("沒有獲取到", i[0])
    # 每次清空文本框，方便下次直接输入
    driver.find_element_by_id('kw').clear()

# 关闭数据库、selenium驱动
pg.close()
driver.close()
```