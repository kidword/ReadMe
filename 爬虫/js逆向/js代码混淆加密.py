"""
js 加密混淆
"""
import hashlib
import time
import base64
from typing import List, Any
import requests

INDEX_URL = 'https://dynamic6.scrape.cuiqingcai.com/api/movie?limit={limit}&offset={offset}&token={token}'
LIMIT = 10
OFFSET = 0


def get_token(args: List[Any]):
    """
    先将/api/movie放到列表里面；
    列表中加入时间戳
    将列表内容用逗号拼接
    将拼接结果进行SHA1编码
    将编码结果和时间戳再次拼接
    将拼接后结果进行base64编码
    """
    timestamp = str(int(time.time()))
    args.append(timestamp)
    sign = hashlib.sha1(','.join(args).encode('utf-8')).hexdigest()
    return base64.b64encode(','.join([sign, timestamp]).encode('utf-8')).decode('utf-8')


args = ['/api/movie']
token = get_token(args=args)
index_url = INDEX_URL.format(limit=LIMIT, offset=OFFSET, token=token)
response = requests.get(index_url)
print(response.text)
