"""
使用超级鹰打码平台模拟登录12306
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from PIL import Image
from login_12306.chaojiying import Chaojiying_Client


bro = webdriver.Chrome()

bro.set_window_size(1680, 900)   # 设置浏览器大小

bro.get("https://kyfw.12306.cn/otn/resources/login.html")
time.sleep(1)
# 点击账号登录按钮
bro.find_element_by_xpath('//li[@class="login-hd-account"]').click()
time.sleep(2)
bro.save_screenshot('aa.png')

# 获取验证码对象
code_img_ele = bro.find_element_by_id('J-loginImg')
location = code_img_ele.location
size = code_img_ele.size
print('size:', size)

# 获取左上角和右下角坐标
rangle = (
    int(location['x']), int(location['y']), int(location['x'] + size['width']), int(location['y'] + size['height'])
)

i = Image.open('./aa.png')
code_img_name = 'code.png'
# 图片裁剪
frame = i.crop(rangle)
frame.save(code_img_name)


# 使用超级鹰识别验证码
chaojiying = Chaojiying_Client('kidword', '123456', '899370')
im = open('code.png', 'rb').read()
result = chaojiying.PostPic(im, 9004)['pic_str']
print()


# 根据识别结果，使用selenium点击对应图片
all_list = []
if '|' in result:
    list_1 = result.split('|')
    count_1 = len(list_1)
    for i in range(count_1):
        xy_list = []
        x = int(list_1[i].split(',')[0])
        y = int(list_1[i].split(',')[1])
        xy_list.append(x)
        xy_list.append(y)
        all_list.append(xy_list)
else:
    x = int(result.split(',')[0])
    y = int(result.split(',')[1])
    xy_list = []
    xy_list.append(x)
    xy_list.append(y)
    all_list.append(xy_list)


for l in all_list:
    x = l[0]
    y = l[1]
    ActionChains(bro).move_to_element_with_offset(code_img_ele, x, y).click().perform()
    time.sleep(0.5)

bro.quit()
