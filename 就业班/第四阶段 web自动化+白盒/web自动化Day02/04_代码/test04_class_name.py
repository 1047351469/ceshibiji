from time import sleep
from selenium import webdriver
# 实例化浏览器
driver=webdriver.Firefox()
url="file://E:/课堂/WebDriver/注册A.html"
driver.get(url)
# 定位使用 class属性
driver.find_element_by_class_name("telA").send_keys("18611111111")
sleep(3)
# 关闭方法
driver.quit()