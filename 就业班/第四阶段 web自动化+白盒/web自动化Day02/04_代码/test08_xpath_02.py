from time import sleep

from selenium import webdriver
# 实例化浏览器
driver=webdriver.Firefox()
url="file://E:/课堂/WebDriver/注册A.html"
driver.get(url)

# 使用xpath相对路径定位
driver.find_element_by_xpath("//input[@id='userA']").send_keys("admin")
driver.find_element_by_xpath("//input[@id='passwordA']").send_keys("123456")


sleep(2)
driver.quit()