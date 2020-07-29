#!/usr/bin/env python
# coding:UTF-8

"""
@version: python3.6
@author:kidword
@contact: 1594636097@qq.com
@software: PyCharm
@time: 2020/7/29 16:05
@msg: selenium 常用方法
"""
import time
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoAlertPresentException


class SeleniumAuto:
    def __init__(self):
        # 设置休眠时间
        self.sleep_time = 0.2
        # 设置浏览器检测navcat属性
        self.option = ChromeOptions()
        self.option.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.option.add_experimental_option("useAutomationExtension", False)
        self.driver = webdriver.Chrome(options=self.option)
        self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",
                                    {'source': 'Object.defineProperty(navigator, "webdriver",{get:() => undefined})'})

        # 配置无头浏览
        # self.option.add_argument('--headless')

        # 设置窗口大小
        self.driver.set_window_size(1680, 1080)

        # 设置等待时间
        self.wait = WebDriverWait(self.driver, 30)

        self.login_url = 'http://data.cma.cn/user/toLogin.html?backUrl=' \
                         'http://data.cma.cn/dataService/cdcindex/datacode/A.0012.0001/show_value/normal.html'

        # 图片名称
        self.web_png_name = 'web_login.png'  # 浏览器截图名称
        self.code_png_name = 'code.png'  # 验证码截图名称

    # 4~6位验证码登录
    def login(self):
        self.driver.get(self.login_url)
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'logIn-page')))
        self.driver.find_element_by_id('loginWeb-page').click()  # 切换到登录窗口
        self.driver.save_screenshot(self.web_png_name)  # 页面截图
        # 获取验证码
        code = ''

        # 获取页面中用户登录元素
        self.driver.find_element_by_id('userName-page').send_keys('')  # 用户名
        time.sleep(self.sleep_time)
        self.driver.find_element_by_id('password-page').send_keys('')  # 密码
        time.sleep(self.sleep_time)
        self.driver.find_element_by_id('verifyCode-page').send_keys(code)  # 验证码
        time.sleep(self.sleep_time)

        # 获取登录按钮
        button = self.driver.find_element_by_class_name('logIn-submit')
        button.click()
        time.sleep(self.sleep_time)

    # 检查登录状态
    def login_success(self):
        try:
            # 登录不成功时
            dig_alert = self.driver.switch_to.alert
            alert_text = dig_alert.text
            print('弹窗的提示信息为：', alert_text)
            dig_alert.accept()  # 忽略弹窗
            # 需要重新登录
            return False
        except NoAlertPresentException:
            # cookie = self.driver.get_cookies()
            # cookie = cookie_str(cookie)
            # write_cookie_txt(cookie)
            return True

    # 保存验证码图片
    def save_verify_img(self):
        code_img_ele = self.driver.find_element_by_id('yw0')
        location = code_img_ele.location
        size = code_img_ele.size
        rangle = (
            int(location['x']), int(location['y']), int(location['x'] + size['width']),
            int(location['y'] + size['height'])
        )
        i = Image.open(self.web_png_name)  # 打开页面截图
        code_img_name = self.code_png_name  # 保存验证码图片名称
        frame = i.crop(rangle)
        frame.save(code_img_name)

    # 切换浏览器窗口
    def switch_windows_tab(self):
        # 获取所有窗口
        windows_tabs = self.driver.window_handles
        self.driver.switch_to.window(windows_tabs[1])  # 切换到第二个窗口中去
        self.driver.close()  # 关闭当前窗口

    # 关闭chrome驱动，退出程序
    def close(self):
        self.driver.quit()
        exit()
