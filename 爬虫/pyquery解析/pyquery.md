```python
import requests
from pyquery import PyQuery as pq
from retrying import retry

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}


def request(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.content.decode()


url = 'http://www.yanquecao.com/detail/5039'

html = request(url)
doc = pq(html)
table_list = doc('.content table').items()
table_len = doc('.content table')
content = []

for index in table_list:
    content.append(index.text())

content = content[1:]
# print(content)
for con in content:
    print(con)



```

```python
import requests
from pyquery import PyQuery as pq
from retrying import retry

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}


def request(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.content.decode()


url = 'https://baike.baidu.com/item/%E5%B0%8F%E4%B8%BD%E4%B8%9D%E8%97%BB'

html = request(url)
doc = pq(html)
title1 = doc('.main-content .para')
title = title1.find('a').remove()
# print(len(title1))
# for t in title1.items():
#     print(t.text())
```

