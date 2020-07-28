import time
from selenium import webdriver


driver = webdriver.Chrome()
driver.set_window_rect(width=1680, height=1080)


req_url = 'http://data.cma.cn/dataService/cdcindex/datacode/A.0012.0001/show_value/normal.html'
driver.get(req_url)

driver.find_element_by_xpath('//dd[@data="320"]/a').click()

time.sleep(2)
driver.find_element_by_id('area-choices-all').click()

driver.find_element_by_xpath('//input[@value="PRS"]').click()
driver.find_element_by_xpath('//input[@value="PRS_Sea"]').click()
driver.find_element_by_xpath('//input[@value="PRS_Max"]').click()


time.sleep(35)
driver.quit()
