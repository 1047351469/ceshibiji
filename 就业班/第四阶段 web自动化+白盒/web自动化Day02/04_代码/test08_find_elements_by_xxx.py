# 解决2.4使用tag_name定位密码框问题
from time import sleep

from selenium import webdriver
driver=webdriver.Firefox()
url="file://E:/课堂/WebDriver/注册A.html"
driver.get(url)

'''
elements:返回所有符合条件的元素
说明：返回的格式为列表，所以访问的时候必须指定下标，下标从零开始
'''
driver.find_elements_by_tag_name("input")[1].send_keys("123456")
sleep(2)
driver.quit()