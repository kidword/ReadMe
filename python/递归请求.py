import re
import pymysql
import json
import requests

# 数据接口
base_url = 'http://127.0.0.1:8081/browse/taxa_tree_children'


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
            if len(data) > 0:
                for item in data:
                    if params.__contains__("id"):
                        item["parentid"] = params["id"]
                return data
            else:
                return None
        except Exception as e:
            print(e)
    else:
        return 'url为空'


# 递归函数
def recursive(count, result, parentId):
    if count == 0:
        params = {
            'otherParam': 'zTreeAsyncTest'
        }
    else:
        params = {
            'id': parentId,
            'otherParam': 'zTreeAsyncTest'
        }
    # 得到<k,v>的列表list
    data = request(base_url, params)
    if len(data) > 0:
        # 得到所有数据[<k,v>,<k,v>]
        # for item in data:
        getChild(result, 'a2a668d8-1caf-4763-8b79-ef00e1c7368d', 0)
        count += 1
    return result


def getChild(treelst, parentId, lv):
    params = {
        'id': parentId,
        'otherParam': 'zTreeAsyncTest',
        'lv': lv
    }
    lv += 1
    data = request(base_url, params)
    if isinstance(data, list) and len(data) > 0:
        treelst += data
        for i in data:
            if i["isParent"]:
                getChild(treelst, i["id"], lv)
            else:
                lv = 0


def rules(text):
    """
    正则匹配
    :return: 返回匹配后的中文和英文名称
    """
    s1 = re.sub('<.*?>', "", text)
    s2 = re.sub(r'\(.*?\)', '', s1)
    zh = ''.join(re.findall('[\u4e00-\u9fa5]', text, re.S))
    s3 = s2.split('\t')
    ename = ''
    if len(s3) == 0:
        return
    elif len(s3) == 2:
        ename = s3[0]
    else:
        for s in range(0, len(s3)-1):
            ename += s3[s] + " "
    return [zh, ename]


def con():
    db = pymysql.connect(host='192.168.1.130', user='root', password='hh226752', db='crawl', charset='utf8')
    return db


def writeMysql(data):
    conn = con()
    cursor = conn.cursor()
    if data:
        try:
            for r in data:
                name = rules(r['name'])
                sql = "insert into catalogue(id, name, ename, parentid, isparent, pinyin)" \
                      " VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')".format(r['id'], name[0], name[1],
                                                                            r['parentid'], r['isParent'], r['pinyin'])
                cursor.execute(sql)
                print('正在写入:', name[0] + name[1])
            conn.commit()
        except Exception as e:
            print(e)
    else:
        return '无数据'


# 调度
def scheduler():
    result = []
    res = recursive(0, result, "0")
    writeMysql(res)


def main():
    scheduler()


if __name__ == '__main__':
    main()
