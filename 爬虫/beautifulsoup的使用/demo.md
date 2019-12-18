```python
import requests
from bs4 import BeautifulSoup

headers = {
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

url = 'https://www.365sn.cn/Wechat/Index/showDiseases/termId/111/diseId/4330'
response = requests.get(url, headers=headers).text
soup = BeautifulSoup(response, 'lxml')
content = soup.select('body > div.content > div')
res = soup.find_all('p')[1:]
for c in res:
    print(c)
    if '英文名' in c.get_text():
        print(type(res[1]))
# for c in content:
#     p = c.get_text()
#     print(p)
# print(content)
```

