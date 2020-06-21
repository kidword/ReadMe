import requests
import json
from loguru import logger

target_url = 'http://httpbin.org/get'

response_proxy = {
    "code": "0",
    "msg": [
        {"port": "40932", "ip": "212.85.5.118"},
        {"port": "17654", "ip": "212.20.20.108"},
        {"port": "87678", "ip": "212.79.254.73"},
        {"port": "87678", "ip": "212.79.254.73"},
        {"port": "87678", "ip": "212.79.254.73"},
        {"port": "87678", "ip": "212.79.254.73"}
    ]
}

global_proxy = []


def export_proxy(proxy_list: dict) -> list:
    data = []
    if isinstance(proxy_list, dict):
        # ip返回正常
        if proxy_list['code'] == '0':
            for pro in proxy_list['msg']:
                score = 5  # 定义每个ip得分为5
                proxy = {'http': 'http://' + pro['ip'] + ':' + pro['port']}
                data.append({"proxy": proxy, "score": score})
    return data


# 定义请求
def request(url: str, proxy: dict, index: int) -> dict:
    global global_proxy
    if isinstance(url, str) and isinstance(proxy, dict):
        print(url, proxy, index)
        if len(global_proxy) >= 1:
            try:
                print(proxy)
                response = requests.get(target_url, proxies=proxy)
                if response.status_code == 200:
                    return response.text
                else:
                    index += 1
                    print('请求状态码为：', response.status_code)
                    if global_proxy[index]['score'] == 0:
                        global_proxy.remove(global_proxy[index])
                    else:
                        global_proxy[index]['score'] -= 1
                    return request(url, proxy, index)
            except requests.exceptions.ProxyError:
                print('代理请求错误')
                if global_proxy[index]['score'] == 0:
                    global_proxy.remove(global_proxy[index])
                else:
                    global_proxy[index]['score'] -= 1
        else:
            print('代理次数已经重试完成，需要重新获取IP')
            global_proxy = export_proxy(response_proxy)
            return request(url, proxy, index)


def test_proxy():
    global global_proxy
    if isinstance(global_proxy, list) and len(global_proxy) >= 1:
        # print(global_proxy)
        for i in range(10):
            result = request(target_url, global_proxy[i]['proxy'], i)
            global_proxy[i]['score'] += 1


class SuperUserProxy(object):
    def __init__(self):
        # 获取代理api
        self.mogu_proxy_api = 'mogu_api'
        self.proxy_list = []  # 代理ip本地存储
        self.index = 0
        self.headers = {}

    def request(self, url: str) -> str:
        if isinstance(url, str):
            response = requests.get(url, headers=self.headers, proxies=self.proxy_list[self.index])
            if response.status_code == 200:
                if self.index < len(self.proxy_list):
                    self.index += 1
                else:
                    self.index = 0
                return response.text
            else:
                # 执行代理修改函数
                self.update_proxy(self.index)

    def update_proxy(self, index: int) -> None:
        if isinstance(index, int):
            if len(self.proxy_list) > 0:
                if self.proxy_list[index]['score'] > 0:
                    self.proxy_list[index]['score'] = self.proxy_list[index]['score'] - 1
                else:
                    self.proxy_list.pop(index)
            else:
                # 重新获取代理
                self.get_proxy()

    def get_proxy(self) -> list:
        if self.mogu_proxy_api:
            response = requests.get(self.mogu_proxy_api, headers=self.headers)
            if response.status_code == 200:
                proxy_data = json.loads(response.text)
                if proxy_data['data']['code'] == '0':
                    proxy_list = proxy_data['data']['list']['ProxyIpInfoList']
                    proxy_result = []
                    for proxy in proxy_list:
                        proxy = 'http://' + proxy['ip'] + ":" + str(proxy['Port'])
                        proxy_obj = {'http': proxy, 'score': 5}
                        proxy_result.append(proxy_obj)
                    logger.info('成功获取网站ip代理')
                    return proxy_result
            else:
                logger.info('请检查代理api...')
                raise KeyError


if __name__ == '__main__':
    global_proxy = export_proxy(response_proxy)
    # print(global_proxy)
    test_proxy()
