import json
import time
import requests
from loguru import logger


class SuperUseProxy(object):
    def __init__(self):
        # 获取代理精灵api，一次提取一个
        self.dljl_proxy_api = 'http://ip.11jsq.com/api/entry?method=proxyServer.ipinfolist&packid=7&fa=5&fetch_key=&time=1&quantity=1&province=&city=&anonymous=1&ms=1&service=0&protocol=1&format=json&separator=1&separator_txt='
        self.proxy_list = self.get_proxy()  # 初始化ip的存储
        self.index = 0
        self.headers = {'User-Agent': 'Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) '
                                      'AppleWebKit/533.1(KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'}

    def request(self, url: str) -> str:
        if isinstance(url, str):
            proxies = {'http': str(self.proxy_list[self.index]['http'])}
            response = requests.get(url, headers=self.headers, proxies=proxies)
            if response.status_code == 200:
                if self.index + 1 < len(self.proxy_list):
                    self.index += 1
                else:
                    self.index = 0
                return response.text
            else:
                # 执行代理修改函数
                self.update_proxy(self.index)
                return self.request(url)

    def update_proxy(self, index: int) -> None:
        if isinstance(index, int):
            if len(self.proxy_list) > 0:
                if self.proxy_list[index]['score'] > 0:
                    self.proxy_list[index]['score'] = self.proxy_list[index]['score'] - 1
                else:
                    self.proxy_list.pop(index)
                    # 重新获取代理
                    if len(self.proxy_list) == 0:
                        self.proxy_list = self.get_proxy()
            else:
                # 重新获取代理
                self.proxy_list = self.get_proxy()

    def get_proxy(self) -> list:
        if self.dljl_proxy_api:
            response = requests.get(self.dljl_proxy_api)
            if response.status_code == 200:
                proxy_data = json.loads(response.text)
                if proxy_data['data']['code'] == 0:
                    proxy_list = proxy_data['data']['list']['ProxyIpInfoList']
                    proxy_result = []
                    for proxy in proxy_list:
                        proxy = 'http://' + proxy['IP'] + ":" + str(proxy['Port'])
                        proxy_obj = {'http': proxy, 'score': 5}
                        proxy_result.append(proxy_obj)
                    logger.info('成功获取网站ip代理')
                    return proxy_result
            else:
                logger.info('请检查代理api...')
                raise KeyError

    def engine(self):
        # 开始请求
        for i in range(50):
            print('检查代理ip使用状态：', self.proxy_list)
            # 测试ip频繁访问地址
            httpbin = self.request('http://www.porters.vip/features/rate.html')
            print(httpbin)
            # time.sleep(1)


if __name__ == '__main__':
    proxy = SuperUserProxy()
    proxy.engine()
