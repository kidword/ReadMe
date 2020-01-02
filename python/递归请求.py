import re
import json
import requests


def request(url, params):
    """
    发送请求
    :param url: string 请求URL
    :param params: 请求参数
    :return: 列表
    """
    if url:
        try:
            response = requests.post(url=url, data=params)
            data = json.loads(response.text)
            return data
        except Exception as e:
            print(e)
    else:
        return 'url为空'


def conversion(data):
    """
    数据处理，数据转换
    :param data: list 数据
    :return: item字典
    """
    if data:
        try:
            layer = 5  # 层级 无实际意义
            item = {}
            for d in data:
                item['id'] = d['id']
                item['name'] = d['name']
                item['lv'] = layer
                item['isParent'] = d['isParent']
                item['pinyin'] = d['pinyin']
                item['otherParam'] = 'zTreeAsyncTest'
            return item
        except Exception as e:
            print(e)
    else:
        return '无数据'


# 递归函数

def recursive(count, result, parentId):
    url = 'http://127.0.0.1:8081/browse/taxa_tree_children'
    isParent = True
    while isParent:
        if count == 0:
            params = {
                'otherParam': 'zTreeAsyncTest'
            }
        else:
            params = {
                'id': parentId,
                'otherParam': 'zTreeAsyncTest'
            }
        # 第一次请求
        data = request(url, params)
        res = conversion(data)
        res['parentId'] = str(parentId)
        isParent = res['isParent']
        id = res['id']
        result.append(res)
        count += 1
        if count == 2:
            return
        recursive(count, result, str(res['parentId']))
    s = len(result)
    print(result)


def getChild(child):
    pass


def scheduler():
    result = []

    recursive(0, result, "0")
    s = 2


def main():
    scheduler()


if __name__ == '__main__':
    main()
