# 导入selenium
from selenium import webdriver
from time import sleep
# 实例化浏览器
driver=webdriver.Firefox()
# 打开项目-url
driver.get("D:\\register\\注册A.html")
# 找到用户名文本框-定位元素(用户)
element=driver.find_element_by_id("userA")
# 给用户文本框传值
element.send_keys("admin")
pwd=driver.find_element_by_id("passwordA")
pwd.send_keys("123456")
# 暂停3秒钟
sleep(3)
# 关闭浏览器
driver.quit()