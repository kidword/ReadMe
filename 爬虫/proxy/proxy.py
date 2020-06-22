import json
import time
import requests
from loguru import logger


class SuperUseProxy(object):
    def __init__(self):
        # 获取代理精灵api，一次提取一个
        self.dljl_proxy_api = 'http://ip.11jsq.com/api/entry?method=proxyServer.ipinfolist&packid=7&fa=5&fetch_key=&time=1&quantity=1&province=&city=&anonymous=1&ms=1&service=0&protocol=1&format=json&separator=1&separator_txt='
        self.proxy_list = []  # 初始化ip的存储
        self.index = 0
        self.headers = {'User-Agent': 'Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) '
                                      'AppleWebKit/533.1(KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'}

    def request(self, url: str) -> str:
        if isinstance(url, str):
            print('索引为：', self.index)
            print('全局代理列表:', self.proxy_list)
            proxies = {'http': str(self.proxy_list[self.index]['http'])}
            try:
                response = requests.get(url, headers=self.headers, proxies=proxies, timeout=2)
                if response.status_code == 200:
                    if self.index + 1 < len(self.proxy_list):
                        self.index += 1
                    else:
                        self.index = 0
                    print('使用ip为：', self.proxy_list[self.index])
                    # print(response.text)
                    return response.text
                else:
                    # 执行代理修改函数
                    self.update_proxy(self.index)
                    return self.request(url)
            except Exception as e:
                print(e.args)
                if self.index + 1 < len(self.proxy_list):
                    self.index += 1
                else:
                    self.index = 0
                self.update_proxy(self.index)
                return self.request(url)

    def update_proxy(self, index: int) -> None:
        if isinstance(index, int):
            if len(self.proxy_list) > 0:
                # 如果分数大于0时，将分数-1
                if self.proxy_list[index]['score'] > 0:
                    self.proxy_list[index]['score'] = self.proxy_list[index]['score'] - 1
                else:
                    self.proxy_list.pop(index)
                    self.index -= 1
                    if self.index < 0:
                        self.index = 0

                    # 重新获取代理
                    if len(self.proxy_list) == 0:
                        self.index = 0
                        self.get_proxy()
            else:
                # 重新获取代理
                self.proxy_list = self.get_proxy()
                self.index = 0

    def get_proxy(self) -> None:
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
                    self.proxy_list = proxy_result
            else:
                logger.info('请检查代理api...')
                raise KeyError

    def engine(self):
        self.get_proxy()
        # 开始请求
        for i in range(100):
            # print('检查代理ip使用状态：', self.proxy_list)
            # 测试ip频繁访问地址
            httpbin = self.request('http://www.porters.vip/features/rate.html')
            print('Steamboat-反爬虫练习' in httpbin)
            # time.sleep(1)


class LocalProxy(SuperUseProxy):
    def get_proxy(self):
        if self.dljl_proxy_api:
            proxy_result = []
            for i in range(3):
                response = requests.get('http://127.0.0.1:5555/random')
                if response.status_code == 200:
                    proxy_data = response.text
                    proxy = 'http://' + str(proxy_data)
                    proxy_obj = {'http': proxy, 'score': 2}
                    proxy_result.append(proxy_obj)
                    logger.info('成功获取网站ip代理')
                else:
                    logger.info('请检查代理api...')
                    raise KeyError
            self.proxy_list = proxy_result


if __name__ == '__main__':
    proxy = LocalProxy()
    proxy.engine()
