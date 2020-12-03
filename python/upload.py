# -*- coding=utf-8 -*-
import os
import requests


def upload_img(file, api):
    """
    :param file: 文件路径
    :param api:  上传接口
    """
    reads = open(file, 'rb')
    files = {'file': reads}
    data = {
        "tags": "缩略图"
    }
    headers = {
        'User-Agent': "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;SV1)",
        "Charsert": "UTF-8",
        "Authorization": "token"
    }
    try:
        response = requests.post(api, files=files, headers=headers, data=data)
        result = response.json()
        if result.get("status") == "ok":
            return True
    except Exception as e:
        print(e.args)
    finally:
        reads.close()


if __name__ == '__main__':
    api_img = "上传文件接口"
    path = r"E:/banlan/tu/"  # 图片地址
    file_list = os.listdir(path)
    if file_list:
        for files in file_list[482:]:
            files = path + files
            status = upload_img(file=files, api=api_img)
            if status:
                print("上传成功....")
            else:
                with open("a.txt", "a+", encoding="utf-8") as f:
                    f.write("图片上传失败：{} \n".format(files))
                continue
