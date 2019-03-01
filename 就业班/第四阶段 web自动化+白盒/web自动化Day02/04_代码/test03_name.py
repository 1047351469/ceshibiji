# 导包
from time import sleep

from selenium import webdriver
# 实例化浏览器对象
driver=webdriver.Firefox()
url="file://E:/课堂/WebDriver/注册A.html"
# 打开url
driver.get(url)
# 定位用户及操作
driver.find_element_by_name("userA").send_keys("admin")
# 定位密码及操作
driver.find_element_by_name("passwordA").send_keys("123456")
sleep(2)
# 关闭浏览器
driver.quit()