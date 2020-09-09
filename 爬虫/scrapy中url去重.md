### 根据url判断

```
# redis
import redis
import hashlib


class ExistSaveRedis(object):
    '''判断是否存在，保存url,'''

    def __init__(self):
        self.coon = redis.Redis(host="127.0.0.1", port=6379, db=0)

    def select_url(self, urls):
        '''判断url_list是否存在,返回不存在的url列表（即待爬取）'''
        redis_exist_url = self.coon.lrange("url", 0, -1)
        redis_exist_url = [i.decode("UTF-8") for i in redis_exist_url]
        hash_url = hashlib.md5(urls.encode(encoding='UTF-8')).hexdigest() #md5加密
        if hash_url not in redis_exist_url:
            self.coon.rpush("url", hash_url)
            return urls

if __name__ == '__main__':
    a = ExistSaveRedis().select_url('1')
    print(a)
```

