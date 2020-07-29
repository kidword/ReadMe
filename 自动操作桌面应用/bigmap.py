import os
import time
import pymouse
import pyautogui


def open_bigmap(bigmap_exe_file: str):
    if bigmap_exe_file:
        os.startfile(bigmap_exe_file)


if __name__ == "__main__":
    # 启动bigmap
    app_dir = r'H:/tools/BIGEMAP地图下载器/MapDownloader.exe'  # 指定应用程序目录
    open_bigmap(app_dir)

    time.sleep(20)

    sleep_time = 2
    m = pymouse.PyMouse()  # 获取鼠标指针对象
    x = 1466
    y = 73
    m.move(x, y)  # 鼠标移动(x,y)坐标

    time.sleep(sleep_time)
    x1 = 1464
    y1 = 150
    # 点击省或者直辖市
    m.click(x1, y1)

    # 选择省
    y2 = y1 + 25
    m.click(x1, y2)

    # 选择市
    time.sleep(sleep_time)
    x2 = 1569
    m.click(x2, y1)
    y3 = y1 + 25
    m.click(x2, y3)

    # 选择县
    time.sleep(sleep_time)
    x3 = 1687
    m.click(x3, y1)
    y4 = y1 + 25
    m.click(x3, y4)

    # 选择乡
    time.sleep(sleep_time)
    x4 = 1785
    m.click(x4, y1)
    y5 = y1 + 25
    m.click(x4, y5)

    # 点击中心点
    time.sleep(sleep_time)
    cent_point = [1000, 600]
    pyautogui.doubleClick(x=cent_point[0], y=cent_point[1], interval=0.0, button='left', duration=0.0,
                          tween=pyautogui.linear)
    # m.click(cent_point[0], cent_point[1])

    # 点击poi菜单
    time.sleep(sleep_time)
    poimenu = [1000, 310]
    m.click(poimenu[0], poimenu[1])

    # 切换高德poi
    m.click(916, 350)
    time.sleep(5)

    # 点击查询按钮
    button = [1080, 380]
    m.click(button[0], button[1])

    # 点击查询按钮
    time.sleep(5)
    export = [1076, 870]
    m.click(export[0], export[1])

    # 输入文字
    time.sleep(25)
    pyautogui.click(x=851, y=777, clicks=1, button='left')  # 绝对位置点击
    pyautogui.typewrite("test.xls")  # 键盘输入

    # 保存数据
    time.sleep(sleep_time)
    save = [1500, 845]
    m.click(save[0], save[1])
